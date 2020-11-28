from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import urllib.request
from account import *

browser = webdriver.Chrome()
public_url = 'https://www.instagram.com/stories/dagelan/'

browser.get(public_url)
time.sleep(1)
urlnow = browser.current_url.split("/")
time.sleep(1)

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
    time.sleep(3)
    browser.execute_script("window.history.go(-1)")
    time.sleep(2)
    clcktoplay = xpathselector('//*[@id="react-root"]/section/div/div/section/div[2]').click()
    stories_count = browser.find_elements_by_class_name('_7zQEa')

    if len(stories_count) == 1:
        stories_poster = xpathselector('//*[@id="react-root"]/section/div/div/section/div[2]/div[1]/div/div/img').get_attribute('srcset')
        url = str(stories_poster)
        data = url.split(" ")
        print(data[0])
        dlposter(data[0])

        try:
            vid = xpathselector('//*[@id="react-root"]/section/div/div/section/div[2]/div[1]/div/div/video')
            stories_video = xpathselector('//*[@id="react-root"]/section/div/div/section/div[2]/div[1]/div/div/video/source[1]').get_attribute('src')
            url_video = str(stories_video)
            dlvideo(url_video)
            print(url_video)
        except:
            pass
    else:
        while _current_stories <= len(stories_count):
            stories_poster = xpathselector('//*[@id="react-root"]/section/div/div/section/div[2]/div[1]/div/div/img').get_attribute('srcset')
            url = str(stories_poster)
            data = url.split(" ")
            print(data[0])
            dlposter(data[0])

            try:
                vid = xpathselector('//*[@id="react-root"]/section/div/div/section/div[2]/div[1]/div/div/video')
                stories_video = xpathselector('//*[@id="react-root"]/section/div/div/section/div[2]/div[1]/div/div/video/source[1]').get_attribute('src')
                url_video = str(stories_video)
                dlvideo(url_video)
                print(url_video)
            except:
                pass

            next = xpathselector('//*[@id="react-root"]/section/div/div/section/div[2]/button[2]/div').click()
            _current_stories += 1
    
    time.sleep(3)
    browser.quit()






