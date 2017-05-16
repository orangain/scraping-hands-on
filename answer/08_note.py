import sys

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


def main():
    """
    メインの処理。
    """

    options = Options()
    # Chromeのパス（Stableチャネルで--headlessが使えるようになったら不要なはず）
    options.binary_location = '/Applications/Google Chrome Canary.app/Contents/MacOS/Google Chrome Canary'
    # ヘッドレスモードを有効にする（次の行をコメントアウトすると画面が表示される）。
    options.add_argument('--headless')
    # ChromeのWebDriverオブジェクトを作成する。
    driver = webdriver.Chrome(chrome_options=options)

    driver.get('https://note.mu/')  # noteのトップページを開く。
    assert 'note' in driver.title  # タイトルに'note'が含まれていることを確認する。

    # 10秒でタイムアウトするWebDriverWaitオブジェクトを作成する。
    wait = WebDriverWait(driver, 10)
    # 記事（class="p-post--basic"）が表れるまで待つ。
    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'a.p-post--basic')))

    posts = scrape_posts(driver)  # 文章コンテンツのリストを取得する。

    # コンテンツの情報を表示する。
    for post in posts:
        print(post['title'])
        print(post['url'])


def scrape_posts(driver):
    """
    文章コンテンツのURL、タイトルを含むdictのリストを取得する。
    """

    posts = []

    # すべての文章コンテンツを表すa要素について反復する。
    for a in driver.find_elements_by_css_selector('a.p-post--basic'):
        # URL、タイトルを取得して、dictとしてリストに追加する。
        posts.append({
            'url': a.get_attribute('href'),
            'title': a.find_element_by_css_selector('h4').text,
        })

    return posts


if __name__ == '__main__':
    main()
