from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
import time
import urllib3, shutil
from account import *

browser = webdriver.Chrome()
action = ActionChains(browser)
public_url = 'https://www.instagram.com/accounts/login/?next=/gnfi/'

browser.get(public_url)
time.sleep(1)
urlnow = browser.current_url.split("/")
time.sleep(1)

data_posters = []

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
    _current_highlight = 1
    highlight_count = browser.find_elements_by_class_name('Ckrof')
    if len(highlight_count) > 3:
        while _current_highlight <= len(highlight_count): 
            currentpath = f'//*[@id="react-root"]/section/main/div/div[1]/div/div/div/ul/li[{_current_highlight + 2}]'  
            try:
                xpathselector(currentpath).click()
                time.sleep(3)
                _current_stories = 0
                stories_count = browser.find_elements_by_class_name('_7zQEa')
                print(_current_highlight, len(stories_count))
                xpathselector('//*[@id="react-root"]/section/div[3]/button').click()
                if _current_highlight == highlight_count:
                    break
                if _current_highlight >= 8:
                    nexthighlight = xpathselector('//*[@id="react-root"]/section/main/div/div[1]/div/button').click()
                    xpathselector(currentpath).click()
                    time.sleep(3)
                    _current_stories = 0
                    stories_count = browser.find_elements_by_class_name('_7zQEa')
                    print(_current_highlight, len(stories_count))
                    xpathselector('//*[@id="react-root"]/section/div[3]/button').click()
                _current_highlight += 1
            except:
                pass 
    else:
        currentpath = f'//*[@id="react-root"]/section/main/div/div[1]/div/div/div/ul/li[{_current_highlight + 2}]'
        xpathselector(currentpath).click()
        time.sleep(2)
        stories_count = browser.find_elements_by_class_name('_7zQEa')
        print(len(stories_count))
        # browser.quit()
    
# try:
#     nexthighlight = xpathselector('//*[@id="react-root"]/section/main/div/div[1]/div/button')
#     action.double_click(nexthighlight).perform()
# except:
#     pass
       


            







  



            

     


    
    








