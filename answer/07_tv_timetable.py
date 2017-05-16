from urllib.parse import urlencode
from datetime import date

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

options = Options()
# Chromeのパス（Stableチャネルで--headlessが使えるようになったら不要なはず）
options.binary_location = '/Applications/Google Chrome Canary.app/Contents/MacOS/Google Chrome Canary'
# ヘッドレスモードを有効にする（次の行をコメントアウトすると画面が表示される）。
options.add_argument('--headless')
# ChromeのWebDriverオブジェクトを作成する。
driver = webdriver.Chrome(chrome_options=options)

# 最初にトップ画面を表示する。（これをしないと番組表が読み込めなかった）
driver.get('https://tv.yahoo.co.jp/')

# 番組表のURLを組み立てる（42は兵庫）。
url = 'https://tv.yahoo.co.jp/listings/42/?' + urlencode({
    'd': date.today().strftime('%Y%m%d'),  # 今日の日付をYYYYMMDD形式で
    'st': '4',  # 開始時刻: 4時
    'va': '24',  # 表示範囲: 24時間
    'vb': '1',  # 番組内容: チェックあり
    'vc': '0',  # 不明
    'vd': '0',  # カレンダー: チェックなし
    've': '0',  # 見たい！ボタン: チェックなし
})

print('Navigating', url)
driver.get(url)

# 10秒でタイムアウトするWebDriverWaitオブジェクトを作成する。
wait = WebDriverWait(driver, 10)
# 読み込み中の表示（class="load_data"）が消えるまで待つ。
wait.until(EC.invisibility_of_element_located((By.CSS_SELECTOR, '.load_data')))

# 番組一覧を表示する。
for td in driver.find_elements_by_css_selector('.turnup'):
    try:
        program_time = td.find_element_by_css_selector('.time').text  # 時刻
        program_title = td.find_element_by_css_selector('.title').text  # タイトル

        print(program_time, program_title)  # 時刻とタイトルを表示
    except NoSuchElementException:
        pass  # 要素が見つからない場合は無視

driver.quit()  # ブラウザーを終了する。
