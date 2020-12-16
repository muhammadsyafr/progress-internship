from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import json
# import urllib.request
import urllib3, shutil
from account import *

browser = webdriver.Chrome()
public_url = 'https://www.instagram.com/stories/cnbcindonesia/'

browser.get(public_url)
time.sleep(1)
urlnow = browser.current_url.split("/")
time.sleep(1)

data_posters = []

def xpathselector(xpath):
    return browser.find_element_by_xpath(xpath)

def dlposter(url):
    urllib.request.urlretrieve(url, "lastposter.jpg") 

def dlvideo(url):
    urllib.request.urlretrieve(url, "video.mp4") 

if not urlnow[3] == "stories":
    print('tidak ada stories atau akun di private')
    browser.quit()
else:
    _current_stories = 1
    username = xpathselector('//*[@id="loginForm"]/div/div[1]/div/label/input').send_keys(account[0])
    password = xpathselector('//*[@id="loginForm"]/div/div[2]/div/label/input').send_keys(account[1])
    btn_login = xpathselector('//*[@id="loginForm"]/div/div[3]/button').click()
    time.sleep(4)
    browser.execute_script("window.history.go(-1)")
    time.sleep(4)
    clcktoplay = xpathselector('//*[@id="react-root"]/section/div[1]/div/section/div').click()
    stories_count = browser.find_elements_by_class_name('_7zQEa')

    if len(stories_count) == 1:
        stories_poster = xpathselector('//*[@id="react-root"]/section/div[1]/div/section/div/div[1]/div/div/img').get_attribute('srcset')
        url = str(stories_poster)
        data = url.split(" ")
        data_posters.append(data[0])
        # dlposter(data[0])

        try:
            vid = xpathselector('//*[@id="react-root"]/section/div/div/section/div[2]/div[1]/div/div/video')
            stories_video = xpathselector('//*[@id="react-root"]/section/div/div/section/div[2]/div[1]/div/div/video/source[1]').get_attribute('src')
            url_video = str(stories_video)
            # dlvideo(url_video)
            print(stories_video)
        except:
            pass

    else:
        while _current_stories <= len(stories_count):
            stories_date = xpathselector('//*[@id="react-root"]/section/div[1]/div/section/div/header/div[2]/div[1]/div/div/div/time').get_attribute('datetime')
            stories_poster = xpathselector('//*[@id="react-root"]/section/div[1]/div/section/div/div[1]/div/div/img').get_attribute('srcset')
            url = str(stories_poster)
            data = url.split(" ")
            # print(data[0])
            collect = {}
            collect['url']    = data[0]
            collect['date']   = stories_date
        
            try:
                xpathselector('//*[@id="react-root"]/section/div[1]/div/section/div/div[1]/div/div/video')
                stories_video = xpathselector('//*[@id="react-root"]/section/div[1]/div/section/div/div[1]/div/div/video/source').get_attribute('src')
                url_video = str(stories_video)
                # dlvideo(url_video)
                collect['vid_url']  = url_video
            except:
                pass

            data_posters.append(collect)
            next = xpathselector('//*[@id="react-root"]/section/div[1]/div/section/div/button[2]').click()
            _current_stories += 1
    
    # for x in data_posters:
    #     c = urllib3.PoolManager()
    #     filename = x
        # with c.request('GET', x, preload_content=False) as res, open(filename, 'wb') as out_file:
        #     shutil.copyfileobj(res, out_file)

    # print(data_posters)
    with open("sample.json", "w") as outfile:  
        json.dump(data_posters, outfile) 
    time.sleep(3)
    browser.quit()






