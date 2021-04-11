# yahoo_scraping　2021-04-１１更新

ヤフージャパンのニュースやアクセスランキングをスクレイピングするコードです。
https://news.yahoo.co.jp/rss
https://news.yahoo.co.jp/media/
https://news.yahoo.co.jp/ranking/access/news

ファイルごとの機能は下記です

「トピックス主要」を抽出するコード（xml)  Yahoo_RSS_Topics.py
「ニュース提供社」毎ページから抽出するコード(html) Yahoo_RSS_ALL.py　（参照　yahoo_rss_all_list.csv）
「アクセスランキング」から抽出するコード(html) 　Yahoo_Ranking.ipynb　（参照　yahoo_ranking_url.csv)
 
自動実行のcron 設定 cron_auto

2021-04-11更新　ヤフー特有の日時表記を、datetime形式に変更するなどしました。
