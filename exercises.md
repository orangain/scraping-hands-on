# Pythonクローリング&スクレイピング 練習問題

これはPythonでクローリング・スクレイピングを行うための練習問題です。
好きな問題をやってみてください。

1. [初級] QiitaアドベントカレンダーのURL一覧を取得する
2. [初級] みずほ銀行の外貨普通預金を取得する（表のスクレイピング）
3. [中級] 明日の天気を取得する（APIによるデータ取得）

回答例は[answer](./answer)ディレクトリ内にあります。


## 1. [初級] QiitaアドベントカレンダーのURL一覧を取得する

アドベントカレンダーはすっかり年末の風物詩となりました。
Qiitaの「クローラー／Webスクレイピング Advent Calendar 2016」に登録された記事の一覧を取得します。気になるものがあれば読んでみても良いでしょう。

### 問題

以下のページから25日分の記事のURLとタイトルを取得して表示してください。

クローラー／Webスクレイピング Advent Calendar 2016 - Qiita
http://qiita.com/advent-calendar/2016/crawler

### 期待する出力例

```
http://amacbee.hatenablog.com/entry/2016/12/01/210436 scrapy-splashを使ってJavaScript利用ページを簡単スクレイピング
http://qiita.com/Azunyan/items/9b3d16428d2bcc7c9406 Python Webスクレイピング 実践入門
http://qiita.com/spaceprobe/items/7f90cb3a3d5a4f5ac5af ウェブクローラN本ノック
http://blog.takuros.net/entry/2016/12/05/082533 非エンジニアでも何とか出来るクローラー／Webスクレイピング術
http://qiita.com/hanaken_Nirvana/items/fc1505ede087d0119883 Scrapy&Twitter Streaming APIを使ったTweetのクローリング
http://qiita.com/checkpoint/items/0c8ad814c25e85bbcfa2 Scrapy入門（３）
http://qiita.com/rllllho/items/cb1187cec0fb17fc650a 便利なXPathまとめ
http://qiita.com/massa142/items/a48e2deb09bca5407afd tseを使って未投稿があるQiita Advent Calendarをさらす
http://qiita.com/hotu_ta/items/592f751044ed9219db97 Selenium Builderでスクレイピング/クローラー入門・実践
http://blog.mudatobunka.org/entry/2016/12/18/205833 Scrapy+AWS LambdaでWeb定点観測のイレギュラーに立ち向かう
http://qiita.com/TakesxiSximada/items/39b905ef628b22f963e4 Pythonのseleniumライブラリからphantomjsを使ったらzombieになった
http://anoninoni.hateblo.jp/entry/2016/12/12/020558 AWS上にサーバレスな汎用クローラを展開するぞ。
http://happyou-info.hatenablog.com/entry/2016/12/13/000000 中華人民共和国大使館のスクレイピング
http://qiita.com/Hassan/items/ca55b84a093dd6935c56 Twitter Streaming APIを使った【夢】のクローリング
http://blog.takuros.net/entry/2016/12/25/173900 Pythonクローラー本の決定版か！？　『Pythonクローリング&スクレイピング』
http://orangain.hatenablog.com/entry/duktape PhantomJSとか使わずに簡単なJavaScriptを処理してスクレイピング
http://qiita.com/imunew/items/0786fd5c9255d4c9a18c Scrapy Cloudでスクレイピングした成果物をS3にアップロードする
http://blog.takuros.net/entry/2016/12/12/022750 ServerLessで、Amazonのほしい物リストから安売り情報を通知するBotを作ったよ
http://qiita.com/yamitzky/items/44a3ea178c750f356b4a mitmproxyを使ってどんなサイトでもクローリング・スクレイピングする
http://qiita.com/mpppk/items/5e8ac21274e9431afbbe JavaScriptでブラウザを自動操作できるnightmarejsを使ってガストのクーポンを自動発行する
http://leko.jp/archives/908 Selenium IDEで作ったテストをCLIで動かす方法
http://happyou-info.hatenablog.com/entry/2016/12/22/002439 やはり普及してはならないアンチスクレイピングサービス
http://blog.takuros.net/entry/2016/11/18/102815 「データを集める技術」という本を執筆しました
http://blog.takuros.net/entry/2016/10/24/080959 Amazonのほしい物リストをRSS化するAPIを作ってみた
http://shinyorke.hatenablog.com/entry/2016/12/25/172917 Pythonを用いたWebスクレイピングの開発ノウハウ〜スポーツデータの場合(野球風味)
```

### ボーナス

余裕があれば記事の著者も出力してみましょう。

## 2. [初級] みずほ銀行の外貨普通預金を取得する（表のスクレイピング）

金融機関のWebサイトにはいろいろな表が掲載されています。
毎日自動で取得したら、景気の変動と連動していることがわかるかもしれません。

### 問題

以下のページから外貨普通預金の通貨ごとの金利を取得して表示してください。

みずほ銀行 : 外貨預金金利
https://www.mizuhobank.co.jp/rate/interest.html

### 期待する出力例

```
 外貨普通預金金利（％）（年率・税引前）
米ドル 0.350
英ポンド 0.100
ユーロ 0.001
豪ドル 0.300
ニュージーランドドル 0.300
スイスフラン 0.001
```

### ボーナス

pandasを使っている場合は、pandas.read_html()関数を使うとHTMLの表を簡単にデータフレームに変換できます。
良かったら試してみてください。

pandas.read_html — pandas 0.19.2 documentation
http://pandas.pydata.org/pandas-docs/stable/generated/pandas.read_html.html


## 3. [中級] 明日の天気を取得する（APIによるデータ取得）

明日は晴れるでしょうか？APIが使える場合は、APIを使ったほうが楽だし相手のサーバーの負荷も低くなります。

### 問題

Livedoorのお天気Webサービスを使って、神戸の明日の天気と最高気温を表示してください。

お天気Webサービス仕様 - Weather Hacks - livedoor 天気情報
http://weather.livedoor.com/weather_hacks/webservice

以下のURLで神戸の天気予報をJSON形式で取得できます。

http://weather.livedoor.com/forecast/webservice/json/v1?city=280010

### 期待する出力例

```
神戸の明日の天気は曇時々雨、最高気温は8℃です。
```

### ヒント

* Requestsのレスポンスで`r.json()`とすると、JSONをPythonのdictに変換できます。
* 明日の天気は`forecasts`の2番目にあると仮定して構いません。