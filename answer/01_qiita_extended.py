import requests
from bs4 import BeautifulSoup

r = requests.get('http://qiita.com/advent-calendar/2016/crawler')
soup = BeautifulSoup(r.content, 'html.parser')

for td in soup.select('.adventCalendarCalendar_day'):
    a = td.select_one('.adventCalendarCalendar_comment a')
    author = td.select_one('.adventCalendarCalendar_author').text.strip()
    print(author, a['href'], a.string)
