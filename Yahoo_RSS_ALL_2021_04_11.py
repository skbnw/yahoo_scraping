#Yahoo_RSS_Media 見出しスクレイピング 2021-04-11現在
#対象約640サイト　yahoo特有の時間文字列を追加

import pandas as pd
import requests
from bs4 import BeautifulSoup
import csv
from datetime import datetime
import time   # タイマーを使うため

# yahoo特有の時間文字列をdatetime型変数に変換する関数
import re

def dateString2Datetime(_string):
  cleaned_string = re.sub('\([月火水木金土日]\)', "", _string)
  # 2020年は2020/12/31と表示、2021年の場合は年数が省略される
  if cleaned_string.startswith("20"):
    # 2020年の場合、2020は自然発生
    return datetime.strptime(cleaned_string, "%Y/%m/%d %H:%M")
  else:
    # 2021年の場合、2021を追加して変換
    return datetime.strptime("2021/" + cleaned_string, "%Y/%m/%d %H:%M")

# data-ylk属性のposの次の数字を取得する関数
def getPosNumber(_string):
  first_cadidate = re.findall(r'pos:\d+', _string)[0]
  return int(first_cadidate.split(":")[1])

#ヤフー出稿メディア別のページ一覧を読み込み
df = pd.read_csv('/Users/skbnw/Documents/Python-cron/yahoo_rss_all_list_2021_04_01.csv')

#保存先ファイルを開き
fout = open("/Users/skbnw/Documents/Python-cron/yahoo_rss_all_media.csv",mode="a", encoding="utf_8_sig", newline='')
# 列を決め、列名を書き出す
writer = csv.DictWriter(fout, ['Media', 'Title', 'Pubdate', 'Link', 'Pos'])
writer.writeheader()

#スクレイピングの設定
for index, row in df.iterrows():
  url = row['url']
  # エチケットとして3秒待つ
  time.sleep(3)
  # 進行がわかるように
  print(index)
  html = requests.get(url)
  soup = BeautifulSoup(html.text, 'html.parser')
  # 取得したデータの中にある、class="newsFeed_item"が設定されている要素を抜き出す
  for news in soup.find_all(class_='newsFeed_item'):
    item = {}
    item["Media"] = row["media_online"]
    item["Title"] = news.select_one('.newsFeed_item_title').text
    item["Pubdate"] = dateString2Datetime(
        news.select_one('.newsFeed_item_date').text)
    item["Link"] = news.a['href']
    item["Pos"] = getPosNumber(news.a['data-ylk'])
    writer.writerow(item)
