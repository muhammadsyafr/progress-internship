import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://www.harianjogja.com/rss"

resp = requests.get(url)

soup = BeautifulSoup(resp.content, features="xml")

items = soup.findAll('item')
news_items = []

for item in items:
    news_item = {}
    news_item['title'] = item.title.text
    news_item['link'] = item.link.text
    news_item['pubDate'] = item.pubDate.text
    news_item['desc'] = item.description.text
    news_item['img'] = item.enclosure.text
    news_items.append(news_item)

# print(news_items)
df = pd.DataFrame(news_items)
f =  'test.csv'
# df.to_csv(f) 
print(news_items)

