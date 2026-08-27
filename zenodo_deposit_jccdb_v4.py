#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
JCCDB v3.1 を Zenodo に「データセット」として登録する

背景:
  Zenodo 10.5281/zenodo.20019572 / 20019573 と engrXiv 10.31224/7007 は
  いずれも解説論文の PDF であって、データセットではない。サイトと MCP は
  2026-08-11〜12 にその記述を全部直した。残っているのは「では、データセットに
  引用可能な DOI を付けるならどうするか」で、その答えがこのスクリプト。

やること:
  1. ローカルの v3.1 ファイル9本の SHA-256 を JCCDB_v3_1_RELEASE_DECLARATION.md と照合
     （1バイトでも違えば即停止。Bitcoin に錨を打った宣言と同じバイト列だけを上げる）
  2. Zenodo に deposition を作成
  3. ファイルをアップロード
  4. アップロード後、Zenodo 側が返す checksum(md5) と手元の md5 を再照合
  5. メタデータを設定
  6. **ここで止まる。** 下書きの URL を表示する

やらないこと:
  - publish（DOI の発行）。--publish を付けたときだけ実行する。
    DOI は取り消せない。目で見てから確定すること。

使い方:
  export ZENODO_TOKEN=xxxxxxxx          # zenodo.org/account/settings/applications/tokens/new
                                        # 必要スコープ: deposit:write deposit:actions
  python3 zenodo_deposit_jccdb.py                 # 下書きを作る（推奨）
  python3 zenodo_deposit_jccdb.py --publish       # 下書きを確認したあと、発行する
  ZENODO_HOST=sandbox.zenodo.org python3 zenodo_deposit_jccdb.py   # 練習用
"""

import hashlib
import json
import os
import re
import sys
import urllib.error
import urllib.request
from pathlib import Path

SRC = Path.home() / "Desktop" / "jccdb"
DECLARATION = "JCCDB_v4_RELEASE_DECLARATION.md"
HOST = os.environ.get("ZENODO_HOST", "zenodo.org")
TOKEN = os.environ.get("ZENODO_TOKEN", "").strip()
STATE = Path.home() / "Desktop" / "zenodo-jccdb-v4-deposition.json"

# 宣言に digest が載っている9本。この順で上げる。
DECLARED = [
    "jccdb-v4-full.csv",
    "jccdb-v4-verified.csv",
    "jccdb-v4-extended.csv",
    "jccdb-v4-provenance.csv",
    "jccdb-v4-schema.json",
    "jccdb-v4-catalog-additions.csv",
]

# 宣言には無いが、文脈として同梱するもの
EXTRA = [DECLARATION, "LICENSE", "README.md", "README.ja.md", "CITATION.cff"]

GH = "https://github.com/ogasurfproject-jpg/japan-construction-cost-database"

DESCRIPTION = """
<p><strong>JCCDB is a catalogue of construction and renovation line items used in Japan:
item name, category and unit. It contains no prices.</strong> Price data lives in a separate
layer (souba-db) and is not part of this deposit.</p>

<p>Japanese construction estimates are written differently by every contractor, so two quotes
for the same job cannot be compared line by line. JCCDB is the shared item catalogue that makes
that comparison possible.</p>

<h4>Composition, as measured</h4>
<ul>
<li><strong>65,520 items</strong> total; zero duplicate rows on category + item_name + unit.</li>
<li><strong>Verified 13,207</strong> — checked against manufacturer catalogues.
Of these, roughly 11,250 came from the v2.0 hand-check and <strong>do not carry per-item
evidence URLs</strong>. The remainder were promoted during the v3.0 and v3.1 verification rounds
and <em>those</em> carry per-item evidence URLs in <code>jccdb-v3-provenance.csv</code>
(2,243 rows). The two are not the same kind of record, and the distinction is stated here
rather than averaged away.</li>
<li><strong>Extended 52,313</strong> — matrix-generated combinations
(manufacturer x series x size x colour). <strong>Individual SKU existence is NOT verified.</strong>
This tier is kept separate precisely so that the unverified part is not presented as verified.</li>
<li>Verified + Extended = 65,520, exactly the total.</li>
<li><strong>Retracted 608</strong> — items proven not to exist, removed from the totals and kept
in <code>jccdb-v3-retracted.csv</code> with reasons and evidence URLs, so the removal itself can
be checked.</li>
<li>Categories exist at two granularities: <strong>72</strong> in the CSV <code>category</code>
column, <strong>402</strong> in the fine-grained <code>jccdb-v3-schema.json</code>. Both describe
the same 65,520 items at different resolutions.</li>
<li>Columns: <code>category, item_name, unit</code>. UTF-8 with BOM, quoted CSV.</li>
</ul>

<h4>Verifying this without trusting the author</h4>
<p>The SHA-256 of every published file is listed in
<code>JCCDB_v3_1_RELEASE_DECLARATION.md</code>, included in this deposit. The digest of that
declaration is appended to the JIDEC public ledger and timestamped into the Bitcoin blockchain
through OpenTimestamps. A third party can therefore establish, without asking the author for
anything, that these files had these contents at or before the anchored time.</p>
<p>Ledger: <a href="https://ledger.horizonshield.dev">https://ledger.horizonshield.dev</a></p>

<h4>Relationship to the papers</h4>
<p><strong>The Zenodo record 10.5281/zenodo.20019572 and the engrXiv record 10.31224/7007 are
the accompanying papers (PDF), not this dataset.</strong> Until this deposit, no item-level
snapshot of JCCDB was deposited on Zenodo. The canonical repository is
<a href="%s">GitHub</a>, with a machine-readable mirror on
<a href="https://huggingface.co/datasets/ogasurfproject/jccdb">Hugging Face</a>.</p>

<h4>日本語</h4>
<p>JCCDB は日本の建設・リフォーム工事の<strong>品目名・カテゴリ・単位</strong>のオープンデータです。
<strong>価格は含みません。</strong>65,520品目・重複ゼロ。検証済み 13,207 と、マトリクス生成で
個別の実在確認をしていない Extended 52,313 を分離してあります。非実在と証明された608件は
理由と証拠URL付きで別ファイルに retract しています。全ファイルの SHA-256 はリリース宣言に記載し、
JIDEC 台帳経由で Bitcoin にタイムスタンプしています。Zenodo と engrXiv の既存 DOI は
<strong>解説論文</strong>であって、データセットではありません。</p>
""" % GH

METADATA = {
    "upload_type": "dataset",
    "title": "Japan Construction Cost Database (JCCDB) v4.0 — 95,403 construction and renovation line items (no prices)",
    "creators": [{
        "name": "Oga, Toshikatsu",
        "affiliation": "The HORIZONs Co., Ltd.",
        "orcid": "0009-0000-9180-903X",
    }],
    "description": DESCRIPTION.strip(),
    "access_right": "open",
    "license": "cc-by-4.0",
    "version": "4.0",
    "language": "jpn",
    "publication_date": "2026-07-27",
    "keywords": [
        "construction", "renovation", "Japan", "cost estimation",
        "open data", "item catalogue", "consumer protection",
        "construction economics", "reference data",
    ],
    "related_identifiers": [
        {"identifier": "10.5281/zenodo.20019572", "relation": "isDocumentedBy",
         "resource_type": "publication-preprint", "scheme": "doi"},
        {"identifier": "10.31224/7007", "relation": "isDocumentedBy",
         "resource_type": "publication-preprint", "scheme": "doi"},
        {"identifier": GH, "relation": "isSupplementTo", "scheme": "url"},
    ],
    "notes": (
        "This deposit contains the dataset itself. The Zenodo and engrXiv DOIs listed under "
        "related identifiers are the accompanying papers, not a snapshot of the data. "
        "Per-file SHA-256 digests are in JCCDB_v3_1_RELEASE_DECLARATION.md, anchored to Bitcoin "
        "through the JIDEC ledger."
    ),
}


def die(msg):
    print("\n[STOP] " + msg)
    sys.exit(1)


def api(method, path, data=None, headers=None, raw=None, timeout=300):
    url = path if path.startswith("http") else "https://%s/api%s" % (HOST, path)
    h = {"Authorization": "Bearer " + TOKEN}
    if headers:
        h.update(headers)
    body = raw
    if data is not None:
        body = json.dumps(data).encode("utf-8")
        h["Content-Type"] = "application/json"
    req = urllib.request.Request(url, data=body, headers=h, method=method)
    try:
        with urllib.request.urlopen(req, timeout=timeout) as r:
            t = r.read()
            return json.loads(t) if t else {}
    except urllib.error.HTTPError as e:
        detail = e.read().decode("utf-8", "replace")[:900]
        die("%s %s → HTTP %s\n       %s" % (method, url, e.code, detail))


def sha256(p):
    h = hashlib.sha256()
    with open(p, "rb") as f:
        for c in iter(lambda: f.read(1 << 20), b""):
            h.update(c)
    return h.hexdigest()


def md5(p):
    h = hashlib.md5()
    with open(p, "rb") as f:
        for c in iter(lambda: f.read(1 << 20), b""):
            h.update(c)
    return h.hexdigest()


def main():
    publish = "--publish" in sys.argv

    if not TOKEN:
        die("ZENODO_TOKEN が設定されていません。\n"
            "         https://%s/account/settings/applications/tokens/new\n"
            "         スコープ: deposit:write と deposit:actions\n"
            "         export ZENODO_TOKEN=xxxxxxxx" % HOST)
    if not SRC.is_dir():
        die("%s がありません。" % SRC)

    print("Zenodo ホスト: %s" % HOST)
    who = api("GET", "/deposit/depositions?size=1")
    print("トークン: 有効（deposition の一覧を取得できた）\n")

    # ---- 1. 宣言との照合（fail-closed） ----
    print("=== 1. リリース宣言と SHA-256 を照合 ===")
    decl = (SRC / DECLARATION).read_text(encoding="utf-8")
    declared = {fn: sha for sha, fn in
                re.findall(r"^([0-9a-f]{64})\s+(\S+)$", decl, flags=re.M)}
    if not declared:
        die("宣言からダイジェストを読み取れませんでした。")
    for name in DECLARED:
        p = SRC / name
        if not p.is_file():
            die("%s がありません。" % p)
        got, want = sha256(p), declared.get(name)
        if want is None:
            die("%s が宣言に載っていません。" % name)
        if got != want:
            die("%s のSHA-256が宣言と一致しません。\n       宣言: %s\n       実物: %s\n"
                "       Bitcoin に錨を打った宣言と違うバイト列は上げない。" % (name, want, got))
        print("  [ok] %-40s %s…" % (name, got[:16]))
    print("  → 9ファイルすべて宣言と一致\n")

    files = DECLARED + [f for f in EXTRA if (SRC / f).is_file()]
    missing = [f for f in EXTRA if not (SRC / f).is_file()]
    if missing:
        print("  （同梱をスキップ: %s）\n" % ", ".join(missing))

    # ---- 2. deposition ----
    if STATE.is_file():
        dep = json.loads(STATE.read_text(encoding="utf-8"))
        print("=== 2. 既存の下書きを再利用: id=%s ===" % dep["id"])
        dep = api("GET", "/deposit/depositions/%s" % dep["id"])
    else:
        print("=== 2. deposition を作成 ===")
        dep = api("POST", "/deposit/depositions", data={})
        STATE.write_text(json.dumps({"id": dep["id"], "host": HOST}, indent=2), encoding="utf-8")
    dep_id = dep["id"]
    bucket = dep["links"]["bucket"]
    print("  id=%s\n" % dep_id)

    # ---- 3. アップロード（再開可能・リトライ付き） ----
    import time as _t
    print("=== 3. ファイルをアップロード（%d本）===" % len(files))
    try:
        already = {f["filename"]: f["checksum"].replace("md5:", "")
                   for f in api("GET", "/deposit/depositions/%s/files" % dep_id)}
    except Exception:
        already = {}
    local_md5 = {}
    for name in files:
        p = SRC / name
        local_md5[name] = md5(p)
        if already.get(name) == local_md5[name]:
            print("  [==] %-40s 既にZenodo側に同一のものがある（スキップ）" % name)
            continue
        body = open(p, "rb").read()
        for attempt in range(1, 6):
            try:
                req = urllib.request.Request(
                    "%s/%s" % (bucket, name), data=body,
                    headers={"Authorization": "Bearer " + TOKEN,
                             "Content-Type": "application/octet-stream"},
                    method="PUT")
                with urllib.request.urlopen(req, timeout=1800) as r:
                    r.read()
                print("  [up] %-40s %8d bytes" % (name, len(body)))
                break
            except Exception as e:
                if attempt == 5:
                    die("%s のアップロードが5回とも失敗しました: %s\n"
                        "       すでに上がった分は残っています。同じコマンドをもう一度実行すれば、\n"
                        "       上がっている分を飛ばして続きから再開します。" % (name, e))
                wait = 10 * attempt
                print("  [..] %-40s 失敗 %s — %d秒待って再試行 (%d/4)"
                      % (name, type(e).__name__, wait, attempt))
                _t.sleep(wait)

    # ---- 4. 転送後の再照合 ----
    print("\n=== 4. ★関門 — Zenodo 側の checksum と手元を再照合 ===")
    remote = api("GET", "/deposit/depositions/%s/files" % dep_id)
    rmap = {f["filename"]: f["checksum"].replace("md5:", "") for f in remote}
    bad = []
    for name in files:
        r = rmap.get(name)
        if r is None:
            bad.append("%s: Zenodo 側に存在しない" % name)
        elif r != local_md5[name]:
            bad.append("%s: md5 不一致 手元=%s Zenodo=%s" % (name, local_md5[name][:12], r[:12]))
        else:
            print("  [ok] %-40s %s…" % (name, r[:16]))
    if bad:
        die("転送でファイルが変わっています。publish しないでください。\n       " + "\n       ".join(bad))
    print("  → %d本すべて一致\n" % len(files))

    # ---- 5. メタデータ ----
    print("=== 5. メタデータを設定 ===")
    api("PUT", "/deposit/depositions/%s" % dep_id, data={"metadata": METADATA})
    print("  [ok] title / creators / license / related_identifiers を設定\n")

    edit_url = "https://%s/uploads/%s" % (HOST, dep_id)
    if not publish:
        print("""=== 下書きができました（まだ DOI は発行されていません）===

ブラウザで開いて確認してください:
  %s

見るところ:
  - Upload type が Dataset になっているか
  - ファイルが %d本 揃っているか
  - Related identifiers の2件の DOI が「isDocumentedBy(＝解説論文)」になっているか
  - License が CC BY 4.0 か

納得できたら発行してください。**DOI は取り消せません。**
  python3 %s --publish
""" % (edit_url, len(files), Path(__file__).name))
        return

    # ---- 6. publish ----
    print("=== 6. 発行 ===")
    print("DOI を発行します。取り消せません。実行するには PUBLISH と入力してください。")
    if input("> ").strip() != "PUBLISH":
        die("中止しました。下書きは残っています。")
    out = api("POST", "/deposit/depositions/%s/actions/publish" % dep_id)
    doi = out.get("doi") or out.get("metadata", {}).get("prereserve_doi", {}).get("doi")
    print("""
=== 発行しました ===

  DOI:    %s
  Record: %s

このあとやること（今日直した記述と整合させる）:
  1. jccdb リポジトリの README / CITATION.cff にデータセット DOI を追記する
     （論文 DOI とは別物として書く。「解説論文DOI」「データセットDOI」と書き分ける）
  2. Hugging Face のカードにも同様に追記
  3. サイトの JSON-LD の Dataset に identifier としてこの DOI を入れてよい
     ← これで初めて「Zenodo にデータセットがある」が真になる
""" % (doi, out.get("links", {}).get("record_html", edit_url)))


if __name__ == "__main__":
    main()
