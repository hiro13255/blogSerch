import requests
import webbrowser
import shelve
from bs4 import BeautifulSoup
import pyperclip as py


# 指定文字列意外入力された時の表示関数
class GoogleSerch():
    num = 3

    # グーグル検索関数
    def googleSarch(self, num, sarch_texts):
        url = 'https://www.google.com/search?q=' + sarch_texts
        result = requests.get(url).text
        soup = BeautifulSoup(result, 'html.parser')
        tags = soup.select('.kCrYT a')

        for i in range(0, int(num)):
            url = tags[i].get('href').replace('/url?q=', '')
            after_url = url[:url.find('&')]
            webbrowser.open(after_url)

