import os
import sys
import time
from urllib.parse import urljoin

import requests
from bs4 import BeautifulSoup

r = requests.get('http://www.apple.com/jp/itunes/charts/free-apps/')
soup = BeautifulSoup(r.content, 'html.parser')

for img in soup.select('#main img'):
    time.sleep(1)  # 1秒スリープ
    image_url = urljoin(r.url, img['src'])  # 相対URLを絶対URLに変換

    image_path = os.path.join('images', os.path.basename(image_url))  # 画像の保存先
    os.makedirs(os.path.dirname(image_path), exist_ok=True)  # ディレクトリがない場合は作成する

    print('Downloading', image_url, file=sys.stderr)
    r2 = requests.get(image_url)  # 画像を取得
    with open(image_path, 'wb') as f:
        f.write(r2.content)  # ファイルに保存
