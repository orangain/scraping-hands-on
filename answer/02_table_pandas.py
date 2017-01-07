# 要 pandas, lxml, html5lib
import pandas

df = pandas.read_html('https://www.mizuhobank.co.jp/rate/interest.html')[0]  # ページ内で1番目の表
print(df)
