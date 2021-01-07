from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
import time
import json
from account import *
import sys

browser = webdriver.Chrome()
username = sys.argv[1]
public_url = f'https://www.instagram.com/accounts/login/?next=/{username}'

browser.get(public_url)
time.sleep(1)
urlnow = browser.current_url.split("/")
time.sleep(1)

data_highlight = []
# state for all stories count // sama dengan jumlahall_global
global_count_stories = 0

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
time.sleep(5)
xpathselector('//*[@id="react-root"]/section/main/div/div/div/div/button').click()
time.sleep(3)
if(check_exists_by_class('_54f4m') == True):
    print('private')
else:
    pathhighlight = f'//*[@id="react-root"]/section/main/div/div[1]/div/div/div/ul/li[{3}]'
    # check highlight count
    if(check_exists_by_xpath(pathhighlight)):
        # swipe right & left to check all highlight count
        while check_exists_by_xpath('//*[@id="react-root"]/section/main/div/div[1]/div/button') != False:
            xpathselector('//*[@id="react-root"]/section/main/div/div[1]/div/button').click()
        time.sleep(5)
        while check_exists_by_xpath('//*[@id="react-root"]/section/main/div/div[1]/div/button[1]') != False:
            xpathselector('//*[@id="react-root"]/section/main/div/div[1]/div/button').click()

        highlight_count = browser.find_elements_by_class_name('Ckrof')
        print('Jumlah Highlight : ', len(highlight_count))
        #wrap per highligh_count == jumlahall
        wrap_perhiglight_count = 0

        #if highlight count lebih dari 7
        if(len(highlight_count) >= 7 ):
            # buat while untuk ambil stories per highlight
            print('log : highlight lebih dari 7, butuh di swipe left')
            count = 0
            while (count < 6):
                currentpath = f'ul.vi798 li:nth-child({count + 3})'
                WebDriverWait(browser, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, currentpath))).click()
                time.sleep(5)
                stories_count = browser.find_elements_by_class_name('_7zQEa')
                print(count + 1, len(stories_count))
                close = xpathselector('//*[@id="react-root"]/section/div[3]/button/div').click()
                count += 1
                time.sleep(2)
                wrap_perhiglight_count += len(stories_count)
                if(count == 7):
                    break

            # wait 5
            time.sleep(5)
            # wait 5

            aftercount = 6
            state = 0
            while (state < (len(highlight_count) - aftercount)):
                time.sleep(2)
                if (aftercount + state) == 7:
                    xpathselector('//*[@id="react-root"]/section/main/div/div[1]/div/button').click()
                if (aftercount + state) == 14:
                    xpathselector('//*[@id="react-root"]/section/main/div/div[1]/div/button').click()
                    time.sleep(2)
                    xpathselector('//*[@id="react-root"]/section/main/div/div[1]/div/button').click()
                time.sleep(3)
                nopath = aftercount + state
                currentpath = f'ul.vi798 li:nth-child({ nopath + 3})'
                WebDriverWait(browser, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, currentpath))).click()
                time.sleep(4)
                stories_count = browser.find_elements_by_class_name('_7zQEa')
                print((aftercount + state + 1), len(stories_count))
                close = xpathselector('//*[@id="react-root"]/section/div[3]/button/div').click()
                state += 1
                time.sleep(2)
                wrap_perhiglight_count += len(stories_count)
                global_count_stories = wrap_perhiglight_count
                if(state == (len(highlight_count) - aftercount)):
                    break
            
        #if highlight count kurang dari 7
        elif(len(highlight_count) < 7):
            print('log : highlight kurang dari 7, tidak usah di swipe')
            count = 0
            # ambil stories di dalam highlight 1 1
            count = 0
            while (count < len(highlight_count)):
                time.sleep(2)
                currentpath = f'ul.vi798 li:nth-child({count + 3})'
                WebDriverWait(browser, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, currentpath))).click()
                time.sleep(5)
                stories_count = browser.find_elements_by_class_name('_7zQEa')
                time.sleep(1)
                close = xpathselector('//*[@id="react-root"]/section/div[3]/button/div').click()
                print(count, len(stories_count))  
                count += 1              
                wrap_perhiglight_count += len(stories_count)
                global_count_stories = wrap_perhiglight_count
        
    else: 
        print('tidak ada highlight')
    
_current_stories = 0
currentpath = f'ul.vi798 li:nth-child({3})'
# WebDriverWait(browser, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, currentpath))).click()
browser.find_element_by_css_selector(currentpath).click()
print('Jumlah Semua Story :', global_count_stories)
time.sleep(3)

while _current_stories <= global_count_stories:
    if(check_exists_by_xpath('//*[@id="react-root"]/section/div[1]/div/section/div/header/div[2]/div[1]/div/div/div/time') == False):
        break
    stories_date = xpathselector('//*[@id="react-root"]/section/div[1]/div/section/div/header/div[2]/div[1]/div/div/div/time').get_attribute('datetime')
    stories_poster = xpathselector('//*[@id="react-root"]/section/div[1]/div/section/div/div[1]/div/div/img').get_attribute('srcset')
    highlight_name = xpathselector('//*[@id="react-root"]/section/div[1]/div/section/div/header/div[2]/div[1]/div/div/div/div/a').text 
    url = str(stories_poster)
    data = url.split(" ")
    collect = {}
    collect['url']          = data[0]
    collect['date']         = stories_date
    collect['username']     = sys.argv[1]
    collect['highlight_name'] = highlight_name
   
    try:
        xpathselector('//*[@id="react-root"]/section/div[1]/div/section/div/div[1]/div/div/video')
        stories_video = xpathselector('//*[@id="react-root"]/section/div[1]/div/section/div/div[1]/div/div/video/source').get_attribute('src')
        url_video = str(stories_video)
        collect['vid_url']  = url_video
    except:
        pass

    data_highlight.append(collect)
    next = xpathselector('//*[@id="react-root"]/section/div[1]/div/section/div/button[2]').click()

with open("highlight.json", "w") as outfile:  
    json.dump(data_highlight, outfile) 
    