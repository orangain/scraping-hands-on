import requests
from bs4 import BeautifulSoup

r = requests.get('http://qiita.com/advent-calendar/2016/crawler')
soup = BeautifulSoup(r.content, 'html.parser')

for a in soup.select('.adventCalendarCalendar_comment a'):
    print(a['href'], a.string)
