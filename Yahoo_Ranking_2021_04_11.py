import pandas as pd
import requests
from bs4 import BeautifulSoup
import csv
import datetime
from datetime import datetime
import time   # タイマーを使うため
import pytz

# 時間文字列をdatetime型変数に変換する関数
import re

def dateString2Datetime(_string):
  cleaned_string = re.sub('\([月火水木金土日]\)', "", _string)
  # 2020年の日付にはちゃんと2020/12/31と表示され、2021年の場合は年数が省略されるようだ
  if cleaned_string.startswith("20"):
    # 2020年のケース
    return datetime.strptime(cleaned_string, "%Y/%m/%d %H:%M")
  else:
    # 2021年のケース。冒頭に2021追加
    return datetime.strptime("2021/" + cleaned_string, "%Y/%m/%d %H:%M")

# #ヤフー出稿メディア別のページ一覧を読み込み
df = pd.read_csv('***/yahoo_ranking_url.csv')

#保存先ファイルを開き、列を作成
with open("***/yahoo_ranking.csv", mode="a", encoding="utf_8_sig", newline='') as f:
  writer = csv.DictWriter(f, ['date_rank', 'category',
                              'rankNum', 'title', 'media', 'pubdate', 'link'])
  writer.writeheader()


#スクレイピングの設定
  for index, row in df.iterrows():
    url = row['url']
    # エチケット3秒待
    time.sleep(3)
    # 進行チェック
    print(index)
    html = requests.get(url)
    soup = BeautifulSoup(html.text, 'html.parser')
    now = datetime.now(pytz.timezone('Asia/Tokyo'))

    for news in soup.find_all(class_='newsFeed_item newsFeed_item-normal newsFeed_item-ranking'):
      d = {}
      d['date_rank'] = now.strftime("%Y/%m/%d %H:%M")
      d['category'] = row['category']
      d['rankNum'] = news.select_one('.newsFeed_item_rankNum').text
      d['title'] = news.select_one('.newsFeed_item_title').text
      d['media'] = news.select_one('.newsFeed_item_media').text
      d['pubdate'] = dateString2Datetime(
          news.select_one('.newsFeed_item_date').text)
      d['link'] = news.a['href']
      writer.writerow(d)
