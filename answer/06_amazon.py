# 要robobrowser
import sys
import os

from robobrowser import RoboBrowser

# 認証の情報は環境変数から取得する。
AMAZON_EMAIL = os.environ['AMAZON_EMAIL']
AMAZON_PASSWORD = os.environ['AMAZON_PASSWORD']

# RoboBrowserオブジェクトを作成する。
browser = RoboBrowser(
    parser='html.parser',  # Beautiful Soupで使用するパーサーを指定する。
    # Cookieが使用できないと表示されてログインできない問題を回避するため、
    # 通常のブラウザーのUser-Agent（ここではFirefoxのもの）を使う。
    user_agent='Mozilla/5.0 (Macintosh; Intel Mac OS X 10.10; rv:45.0) Gecko/20100101 Firefox/45.0')


def main():
    # 注文履歴のページを開く。
    print('Navigating...', file=sys.stderr)
    browser.open('https://www.amazon.co.jp/gp/css/order-history')

    # サインインページにリダイレクトされていることを確認する。
    assert 'Amazonサインイン' in browser.parsed.title.string

    # name="signIn" というサインインフォームを埋める。
    # フォームのname属性の値はブラウザーの開発者ツールで確認できる。
    form = browser.get_form(attrs={'name': 'signIn'})
    form['email'] = AMAZON_EMAIL  # name="email" という入力ボックスを埋める。
    form['password'] = AMAZON_PASSWORD  # name="password" という入力ボックスを埋める。

    # フォームを送信する。正常にログインするにはRefererヘッダーとAccept-Languageヘッダーが必要。
    print('Signing in...', file=sys.stderr)
    browser.submit_form(form, headers={
        'Referer': browser.url,
        'Accept-Language': 'ja,en-US;q=0.7,en;q=0.3',
    })

    # ログインに失敗する場合は、次の行のコメントを外してHTMLのソースを確認すると良い。
    # print(browser.parsed.prettify())

    # ページャーをたどる。
    while True:
        assert '注文履歴' in browser.parsed.title.string  # 注文履歴画面が表示されていることを確認する。

        print_order_history()  # 注文履歴を表示する。

        link_to_next = browser.get_link('次へ')  # 「次へ」というテキストを持つリンクを取得する。
        if not link_to_next:
            break  # 「次へ」のリンクがない場合はループを抜けて終了する。

        print('Following link to next page...', file=sys.stderr)
        browser.follow_link(link_to_next)  # 「次へ」というリンクをたどる。


def print_order_history():
    """
    現在のページのすべての注文履歴を表示する。
    """
    # ページ内のすべての注文履歴について反復する。ブラウザーの開発者ツールでclass属性の値を確認できる。
    for line_item in browser.select('.order-info'):
        order = {}  # 注文の情報を格納するためのdict。
        # 注文の情報のすべての列について反復する。
        for column in line_item.select('.a-column'):
            label_element = column.select_one('.label')
            value_element = column.select_one('.value')
            # ラベルと値がない列は無視する。
            if label_element and value_element:
                label = label_element.get_text().strip()
                value = value_element.get_text().strip()
                order[label] = value  # 注文の情報を格納する。

        print(order['注文日'], order['合計'])  # 注文の情報を表示する。

if __name__ == '__main__':
    main()
