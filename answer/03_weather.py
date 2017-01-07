import requests

r = requests.get('http://weather.livedoor.com/forecast/webservice/json/v1?city=280010')
weather = r.json()
forecast = weather['forecasts'][1]  # 明日の天気

print('{0}の{1}の天気は{2}、最高気温は{3}℃です。'.format(
    weather['location']['city'],
    forecast['dateLabel'],
    forecast['telop'],
    forecast['temperature']['max']['celsius']))
