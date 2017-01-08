import os
import sys
import time
import re
from urllib.parse import urljoin

import requests
from bs4 import BeautifulSoup

r = requests.get('http://www.apple.com/jp/itunes/charts/free-apps/')
soup = BeautifulSoup(r.content, 'html.parser')

for li in soup.select('#main li'):
    time.sleep(1)  # 1秒スリープ
    rank = li.strong.text.strip()  # 順位
    name = li.h3.text.strip()  # アプリ名
    image_url = urljoin(r.url, li.img['src'])  # 相対URLを絶対URLに変換

    _, ext = os.path.splitext(image_url)  # 画像の拡張子を取得
    filename = rank + re.sub(r'\W+', '_', name) + ext  # ファイル名を組み立てる
    image_path = os.path.join('images', filename)  # 画像の保存先
    os.makedirs(os.path.dirname(image_path), exist_ok=True)  # ディレクトリがない場合は作成する

    print('Downloading', image_url, file=sys.stderr)
    r2 = requests.get(image_url)  # 画像を取得
    with open(image_path, 'wb') as f:
        f.write(r2.content)  # ファイルに保存
