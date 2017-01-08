import os
import time
from urllib.parse import urljoin

import requests
from bs4 import BeautifulSoup

url = 'http://www.apple.com/jp/itunes/charts/free-apps/'
r = requests.get(url)
soup = BeautifulSoup(r.content, 'html.parser')

for img in soup.select('#main img'):
    image_url = urljoin(url, img['src'])

    image_path = os.path.join('images', os.path.basename(image_url))
    os.makedirs(os.path.dirname(image_path), exist_ok=True)

    r = requests.get(image_url)
    with open(image_path, 'wb') as f:
        f.write(r.content)

    time.sleep(1)
