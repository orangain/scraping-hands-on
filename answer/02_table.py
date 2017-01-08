import requests
from bs4 import BeautifulSoup

r = requests.get('https://www.mizuhobank.co.jp/rate/interest.html')
soup = BeautifulSoup(r.content, 'html.parser')

table = soup.select_one('table[summary="外貨普通預金金利・為替相場"]')
for tr in table.select('tr'):
    cell1, cell2 = tr.select('*')  # すべての子要素を取得
    print(cell1.string.strip(), cell2.string.strip())
