#Yahoo_RSS_ 主要ニュースの見出しスクレイピング（XML）

import requests
from bs4 import BeautifulSoup
import csv
from datetime import datetime

#スクレイピング先の設定。topisc以外にも、フォルダ名を変更すれば、国内、国際、経済、エンタメ、スポーツ、IT、科学、地域など設定できます。
#参照　https://news.yahoo.co.jp/rss
xml = requests.get("https://news.yahoo.co.jp/rss/topics/top-picks.xml")
soup =  BeautifulSoup(xml.text, 'xml')

#保存先ファイルを設定
with open("****.csv", mode="a", encoding="utf_8_sig",newline="") as f:
  writer = csv.DictWriter(f, ['Category','Title', 'Link','PubDate','Description'])
  writer.writeheader()

#ニュース毎のスクレイピング設定
  for news in soup.findAll('item'):
    d = {}
    d['Category'] = 'topics'
    d['Title'] = news.title.string
    d['Link'] = news.link.string
    d['PubDate']  = news.pubDate.string
    d['Description']  = news.description.string
    writer.writerow(d)
