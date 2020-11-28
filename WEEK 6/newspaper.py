# from newspaper import Article
import feedparser

url = 'https://www.harianjogja.com/rss'
d = feedparser.parse(url)

print(d.entries[1].title) 
print(d.entries[1].enclosures[0].url) 

def parseRSS( rss_url ):
    return feedparser.parse( rss_url )
 
def getFeed(rss_url):
    headlines = []
 
    feed = parseRSS(rss_url)
    for newsitem in feed['items']:
        headlines.append('Title : ' + newsitem['title'])
        headlines.append('Category : ' + newsitem['category'])
        headlines.append('Description : ' + newsitem['description'])
    
    return headlines
 
allheadlines = []
 
newsurls = {
    'https://www.harianjogja.com/rss',
}
 
 
for url in newsurls:
    allheadlines.extend(getFeed(url))


# print(allheadlines)


