#Yahoo_RSS_ 見出しスクレイピング

import requests
from bs4 import BeautifulSoup
import csv
from datetime import datetime

xml = requests.get("https://news.yahoo.co.jp/rss/topics/top-picks.xml")
soup =  BeautifulSoup(xml.text, 'xml')

with open("/Users/skbnw/Documents/Python-cron/Yahoo_RSS_topics.csv", mode="a", encoding="utf_8_sig",newline="") as f:
  writer = csv.DictWriter(f, ['Category','Title', 'Link','PubDate','Description'])
  writer.writeheader()

  for news in soup.findAll('item'):
    d = {}
    d['Category'] = 'topics'
    d['Title'] = news.title.string
    d['Link'] = news.link.string
    d['PubDate']  = news.pubDate.string
    d['Description']  = news.description.string
    writer.writerow(d)