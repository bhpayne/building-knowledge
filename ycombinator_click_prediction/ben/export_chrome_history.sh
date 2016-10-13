cp ~/Library/Application\ Support/Google/Chrome/Default/History ~/temp

sqlite3 chrome_history '.schema urls' | tr , '\n'

sqlite3 chrome_history  'select url from "urls"' > history.log

cat history.log | grep news.ycombinator > clicked_news_article_comments
