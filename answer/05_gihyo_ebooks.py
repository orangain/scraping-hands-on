import time
import re
from urllib.parse import urljoin

import requests
from bs4 import BeautifulSoup


def main():
    """
    クローラーのメインの処理。
    """

    session = requests.Session()
    response = session.get('https://gihyo.jp/dp')  # 一覧ページを取得する。
    urls = scrape_list_page(response)  # 詳細ページのURL一覧を得る。
    for url in urls:
        time.sleep(1)
        response = session.get(url)
        ebook = scrape_detail_page(response)
        print(ebook)  # 電子書籍の情報を表示する。


def scrape_list_page(response):
    """
    一覧ページのResponseから詳細ページのURLを抜き出す。
    """
    soup = BeautifulSoup(response.content, 'html.parser')

    for a in soup.select('#listBook a[itemprop="url"]'):
        url = urljoin(response.url, a.get('href'))
        yield url


def scrape_detail_page(response):
    """
    詳細ページのResponseから電子書籍の情報をdictで取得する。
    """
    soup = BeautifulSoup(response.content, 'html.parser')
    ebook = {
        'url': response.url,  # URL
        'title': soup.select_one('#bookTitle').text,  # タイトル
        'price': soup.select_one('.buy').text.strip(),  # 価格
        'content': [normalize_spaces(h3.text) for h3 in soup.select('#content > h3')],  # 目次
    }
    return ebook


def normalize_spaces(s):
    """
    連続する空白を1つのスペースに置き換え、前後の空白を削除した新しい文字列を取得する。
    """
    return re.sub(r'\s+', ' ', s).strip()


if __name__ == '__main__':
    main()
