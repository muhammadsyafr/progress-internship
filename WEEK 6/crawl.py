import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://www.harianjogja.com/rss"

resp = requests.get(url)

soup = BeautifulSoup(resp.content, features="xml")

items = soup.findAll('item')
news_items = []
news_item_details = []

def spider(link):
    news_item_detail = {}
    resp_detail = requests.get(link)
    soup = BeautifulSoup(resp_detail.content, features="xml")

    #for news_item_detail['img']
    img_list = soup.find_all("a", class_="popup_link")
    for img in img_list:
        news_item_detail['img'] = img.get('href')

    # for news_item_detail['tag']
    tags = soup.find("div", class_="entry_tags shareR")

    #store to object
    news_item_detail['link'] = link
    news_item_detail['title'] = soup.find('h1').text
    news_item_detail['tag'] = tags.find('a').text
    news_item_details.append(news_item_detail)

    # print(news_item_details)

    df = pd.DataFrame(news_item_details)
    f =  'news_details.csv'
    df.to_csv(f) 

#looping a xml feed
for item in items:
    news_item = {}
    news_item['title'] = item.title.text
    news_item['link'] = item.link.text
    news_item['pubDate'] = item.pubDate.text
    news_item['desc'] = item.description.text
    news_item['img'] = item.enclosure
    news_items.append(news_item)
    spider(item.link.text)  

print(news_items)
df = pd.DataFrame(news_items)
f =  'rss.csv'
df.to_csv(f) 


