import os
import time
import re
from urllib.parse import urljoin

import requests
from bs4 import BeautifulSoup

url = 'http://www.apple.com/jp/itunes/charts/free-apps/'
r = requests.get(url)
soup = BeautifulSoup(r.content, 'html.parser')

for li in soup.select('#main li'):
    rank = li.strong.text.strip()
    name = li.h3.text.strip()
    image_url = urljoin(url, li.img['src'])

    _, ext = os.path.splitext(image_url)
    filename = rank + re.sub(r'\W+', '_', name) + ext
    image_path = os.path.join('images', filename)
    os.makedirs(os.path.dirname(image_path), exist_ok=True)

    r = requests.get(image_url)
    with open(image_path, 'wb') as f:
        f.write(r.content)

    time.sleep(1)
