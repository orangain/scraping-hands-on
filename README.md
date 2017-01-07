# Pythonクローリング&スクレイピング ハンズオン

このハンズオンでは、Yahoo!ニュースのトップニュースを題材として、Pythonによるスクレイピングを学びます。

サードパーティライブラリのRequestsとBeautiful Soupを使います。

## 0. 動作環境

* macOS/Linux/Windows
* Python 3.4以降

## 1. 仮想環境の作成

`scraping`という名前の仮想環境を作成し、仮想環境を有効化します。※わかる方は仮想環境を作成せずに薦めても構いません。

### macOS/Linux

```
$ python3 -m venv scraping
$ . scraping/bin/activate
```

### Windows

```
> python -m venv scraping
> scraping\bin\activate
```

## 2. サードパーティライブラリのインストール

* [Requests](http://docs.python-requests.org/en/master/): Webページを取得する
* [Beautiful Soup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/): Webページからスクレイピングする
* [Chardet](https://github.com/chardet/chardet): エンコーディングを自動判別する

```
(scraping) $ pip install requests beautifulsoup4 chardet
```

## 3. インタラクティブシェルの起動

※わかる方はIPythonやJupyter Notebookでも構いません。

```
(scraping) $ python
```

## 4. スクレイピングの実施

インタラクティブシェルを使って、Yahoo!ニュースのトップニュース一覧を取得します。

※RSSを使えばもっと簡単ですが、これは練習ですので。

```python
# requestsモジュールをインポート
>>> import requests
# Yahoo!ニュースのトップページをGETで取得
>>> r = requests.get('http://news.yahoo.co.jp/')
# ステータスコードを確認
>>> r.status_code
200
# エンコーディングを確認
>>> r.encoding
'UTF-8'
# レスポンスボディ（bytes型）を確認
>>> r.content
b'<!DOCTYPE html>\n<html lang="ja"\n    xmlns:og="http://ogp.me/ns#"\n    xmlns:fb="http://ogp.me/ns/fb#">\n<head>\n<meta http-equiv="Content-Type" content="text/html; charset=utf-8">...

# bs4モジュールからBeautifulSoupクラスをインポート
>>> from bs4 import BeautifulSoup
# BeautifulSoupオブジェクトを作成
# 第1引数はパースするHTML、第2引数は使用するパーサー
>>> soup = BeautifulSoup(r.content, 'html.parser')
# title属性でtitle要素を表すTagオブジェクトを取得
>>> soup.title
<title>Yahoo!ニュース</title>
# Tagオブジェクトのstring属性で直下の文字列を取得
>>> soup.title.string
'Yahoo!ニュース'
# select()でCSSセレクターにマッチする要素のリストを取得
>>> soup.select('.topics .ttl a')
[<a href="http://news.yahoo.co.jp/pickup/6226459" onmousedown="this.href='http://news.yahoo.co.jp/pickup/6226459'">空中給油再開か 米軍明かさず<span class="icPhoto">写真</span></a>, <a href="http://news.yahoo.co.jp/pickup/6226465" onmousedown="this.href='http://news.yahoo.co.jp/pickup/6226465'">シリアの露軍 規模縮小を開始<span class="icPhoto">写真</span><span class="icNew">new</span></a>, <a href="http://news.yahoo.co.jp/pickup/6226466" onmousedown="this.href='http://news.yahoo.co.jp/pickup/6226466'">老人ホーム 入浴中に女性死亡<span class="icVideo">映像</span><span class="icNew">new</span></a>, <a href="http://news.yahoo.co.jp/pickup/6226461" onmousedown="this.href='http://news.yahoo.co.jp/pickup/6226461'">「一風堂」マザーズ上場へ<span class="icPhoto">写真</span></a>, <a href="http://news.yahoo.co.jp/pickup/6226440" onmousedown="this.href='http://news.yahoo.co.jp/pickup/6226440'">セイウチは鳥で遊ぶ 初の報告<span class="icPhoto">写真</span><span class="icNew">new</span></a>, <a href="http://news.yahoo.co.jp/pickup/6226455" onmousedown="this.href='http://news.yahoo.co.jp/pickup/6226455'">スノボ5選手 強化指定を解除</a>, <a href="http://news.yahoo.co.jp/pickup/6226463" onmousedown="this.href='http://news.yahoo.co.jp/pickup/6226463'">7kg減の梅宮辰夫 復調を宣言<span class="icPhoto">写真</span><span class="icNew">new</span></a>]
# ニュースのURL（a要素のhref属性）とタイトル（a要素内の文字列の内最初のもの）を表示
>>> for a in soup.select('.topics .ttl a'):
...     print(a['href'], list(a.strings)[0])
...
http://news.yahoo.co.jp/pickup/6226454 韓国外相 日本大使を呼び出し
http://news.yahoo.co.jp/pickup/6226459 空中給油再開か 米軍明かさず
http://news.yahoo.co.jp/pickup/6226465 シリアの露軍 規模縮小を開始
http://news.yahoo.co.jp/pickup/6226466 老人ホーム 入浴中に女性死亡
http://news.yahoo.co.jp/pickup/6226461 「一風堂」マザーズ上場へ
http://news.yahoo.co.jp/pickup/6226440 セイウチは鳥で遊ぶ 初の報告
http://news.yahoo.co.jp/pickup/6226455 スノボ5選手 強化指定を解除
http://news.yahoo.co.jp/pickup/6226463 7kg減の梅宮辰夫 復調を宣言
```

## 参考

* [Requests: HTTP for Humans — Requests 2.12.4 documentation](http://docs.python-requests.org/en/master/)
* [Beautiful Soup Documentation — Beautiful Soup 4.4.0 documentation](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)

## 次のステップ

[exercises.md](./exercises.md)に練習問題を用意しています。

回答例は[answer](./answer)ディレクトリ内にあります。
