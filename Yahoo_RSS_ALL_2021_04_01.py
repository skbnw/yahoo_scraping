#Yahoo_RSS_Media 見出しスクレイピング(html)

import pandas as pd
import requests
from bs4 import BeautifulSoup
import csv

#ヤフー出稿メディア別のページ一覧を読み込み
df = pd.read_csv('yahoo_rss_all_list_2021_04_01.csv')

#保存先ファイルを開き、列を作成
with open("***.csv", mode="a", encoding="utf_8_sig", newline='') as f:
  writer = csv.DictWriter(f, ['Media', 'Title', 'Pubdate', 'Link'])
  writer.writeheader()
  
#スクレイピングの設定
  for index, row in df.iterrows():
    url = row['url']
    html = requests.get( url )
    soup = BeautifulSoup(html.text, 'html.parser' )

    for news in soup.find_all(class_='newsFeed_item'):
      d = {}
      d["Media"]  = row['media_online']
      d["Title"] = news.select_one('.newsFeed_item_title').text
      d["Pubdate"] = news.select_one('.newsFeed_item_date').text
      d["Link"] = news.a['href']
      writer.writerow(d)
    
 

