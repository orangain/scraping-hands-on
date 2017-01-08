import requests

r = requests.get('http://weather.livedoor.com/forecast/webservice/json/v1?city=280010')
weather = r.json()  # JSON形式のレスポンスをパースする
forecast = weather['forecasts'][1]  # 明日の天気

print('{0}の{1}の天気は{2}、最高気温は{3}℃です。'.format(
    weather['location']['city'],  # 都市
    forecast['dateLabel'],  # 予報日
    forecast['telop'],  # 天気
    forecast['temperature']['max']['celsius']))  # 最高気温（摂氏）
