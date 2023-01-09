import requests as rq
import json
import os

API_KEY = os.getenv("NEWS_API")
dev_api = "d31b94c3b8064aac8e83528f9029db5e"
# print(MY_KEY)

url = (
    "https://newsapi.org/v2/everything?q=python&"
    "from=2022-12-09&sortBy=publishedAt&"
    f"apiKey={API_KEY}"
)


request = rq.get(url)
content = request.json()

# TODO: Clean up output path to ensure exists on clean run of app
with open("data/news.json", "w", encoding="utf-8") as nfile:
    json.dump(content, nfile, ensure_ascii=False, indent=4, sort_keys=True)
