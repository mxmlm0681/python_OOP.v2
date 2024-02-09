import json
from pprint import pprint

with open("newsafr.json", encoding="utf-8") as f:
    json_data = json.load(f)

#pprint(json_data)

news_list = json_data["rss"]["channel"]["items"]
news_str = []
for row in news_list:
    news_str.append(row["title"])

print(news_str)





