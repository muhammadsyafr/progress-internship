from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
import time
import json
from account import *

browser = webdriver.Chrome()

public_url = 'https://www.instagram.com/accounts/login/?next=/gnfi/'

browser.get(public_url)
time.sleep(1)
urlnow = browser.current_url.split("/")
time.sleep(1)

data_posters = []
jumlahall_global = 0

def xpathselector(xpath):
    return browser.find_element_by_xpath(xpath)

def check_exists_by_class(classname):
    try:
        browser.find_element_by_class_name(classname)
    except NoSuchElementException:
        return False
    return True

def check_exists_by_xpath(xpath):
    try:
        browser.find_element_by_xpath(xpath)
    except NoSuchElementException:
        return False
    return True

username = xpathselector('//*[@id="loginForm"]/div/div[1]/div/label/input').send_keys(account[0])
password = xpathselector('//*[@id="loginForm"]/div/div[2]/div/label/input').send_keys(account[1])
btn_login = xpathselector('//*[@id="loginForm"]/div/div[3]/button').click()
time.sleep(6)
xpathselector('//*[@id="react-root"]/section/main/div/div/div/div/button').click()
time.sleep(3)
if(check_exists_by_class('_54f4m') == True):
    print('private')
else:
    pathhighlight = f'//*[@id="react-root"]/section/main/div/div[1]/div/div/div/ul/li[{3}]'
    if(check_exists_by_xpath(pathhighlight)):
        # swipe to right
        while check_exists_by_xpath('//*[@id="react-root"]/section/main/div/div[1]/div/button') != False:
            xpathselector('//*[@id="react-root"]/section/main/div/div[1]/div/button').click()

        time.sleep(6)

        #swipe to left
        while check_exists_by_xpath('//*[@id="react-root"]/section/main/div/div[1]/div/button[1]') != False:
            # print(check_exists_by_xpath('//*[@id="react-root"]/section/main/div/div[1]/div/button'))
            xpathselector('//*[@id="react-root"]/section/main/div/div[1]/div/button').click()
        
        highlight_count = browser.find_elements_by_class_name('Ckrof')
        print('jumlah highlight', len(highlight_count))
        jumlahall = 0
        if(len(highlight_count) >= 7 ):
            count = 0
            while (count < 6):
                # print('before 7')
                time.sleep(2)
                currentpath = f'ul.vi798 li:nth-child({count + 3})'
                WebDriverWait(browser, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, currentpath))).click()
                time.sleep(5)
                stories_count = browser.find_elements_by_class_name('_7zQEa')
                # print(count + 1, len(stories_count))
                close = xpathselector('//*[@id="react-root"]/section/div[3]/button/div').click()
                count += 1
                time.sleep(2)
                jumlahall += len(stories_count)
                if(count == 7):
                    print('sampee sini')
                    break

            time.sleep(5)

            aftercount = 6
            state = 0
            while (state < (len(highlight_count) - aftercount)):
                # print('State : ', state)
                time.sleep(2)
                if (aftercount + state) == 7:
                    # print('===== GESER TEROOS ======')
                    xpathselector('//*[@id="react-root"]/section/main/div/div[1]/div/button').click()
                if (aftercount + state) == 14:
                    # print('===== GESER TEROOS ======')
                    xpathselector('//*[@id="react-root"]/section/main/div/div[1]/div/button').click()
                    time.sleep(2)
                    xpathselector('//*[@id="react-root"]/section/main/div/div[1]/div/button').click()
                time.sleep(3)
                nopath = aftercount + state
                currentpath = f'ul.vi798 li:nth-child({ nopath + 3})'
                WebDriverWait(browser, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, currentpath))).click()
                time.sleep(4)
                stories_count = browser.find_elements_by_class_name('_7zQEa')
                # print((aftercount + state + 1), len(stories_count))
                close = xpathselector('//*[@id="react-root"]/section/div[3]/button/div').click()
                state += 1
                time.sleep(2)
                jumlahall += len(stories_count)
                jumlahall_global = jumlahall
                if(state == (len(highlight_count) - aftercount)):
                    break
        
        elif(len(highlight_count) < 7):
            print('kurang dari 7')

        elif(len(highlight_count) == 1):
            print('stories cuma 1')
        
    else: 
        print('tidak ada highlight')

_current_stories = 0
print('jumlah semua story', jumlahall)
currentpath = f'ul.vi798 li:nth-child({3})'
WebDriverWait(browser, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, currentpath))).click()

while _current_stories <= jumlahall_global:
    print(check_exists_by_xpath('//*[@id="react-root"]/section/div[1]/div/section/div/header/div[2]/div[1]/div/div/div/time'))
    if(check_exists_by_xpath('//*[@id="react-root"]/section/div[1]/div/section/div/header/div[2]/div[1]/div/div/div/time') == False):
        break
    stories_date = xpathselector('//*[@id="react-root"]/section/div[1]/div/section/div/header/div[2]/div[1]/div/div/div/time').get_attribute('datetime')
    stories_poster = xpathselector('//*[@id="react-root"]/section/div[1]/div/section/div/div[1]/div/div/img').get_attribute('srcset')
    url = str(stories_poster)
    data = url.split(" ")
    collect = {}
    collect['url']    = data[0]
    collect['date']   = stories_date

    try:
        xpathselector('//*[@id="react-root"]/section/div[1]/div/section/div/div[1]/div/div/video')
        stories_video = xpathselector('//*[@id="react-root"]/section/div[1]/div/section/div/div[1]/div/div/video/source').get_attribute('src')
        url_video = str(stories_video)
        collect['vid_url']  = url_video
    except:
        pass

    data_posters.append(collect)
    next = xpathselector('//*[@id="react-root"]/section/div[1]/div/section/div/button[2]').click()
    _current_stories += 1
    print(_current_stories)
    if _current_stories == jumlahall_global:
        break

with open("highlight.json", "w") as outfile:  
    json.dump(data_posters, outfile) 
time.sleep(1)

print(data_posters)

    







