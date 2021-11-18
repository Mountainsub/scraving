
#必要なライブラリをインポート
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
import os
import signal
#ここで、バージョンなどのチェックをします。
chrome = webdriver.Chrome(ChromeDriverManager().install())
 
#Google Chromeでページを立ち上げます。

url = "https://scraping-for-beginner.herokuapp.com/login_page"

try:
    chrome.get(url)
    sleep(2)
    elem_username = chrome.find_element_by_id('username')
    elem_username.send_keys('imanishi')
    sleep(3)
    elem_password = chrome.find_element_by_id('password')
    elem_password.send_keys('kohei')
    sleep(4)
    elem_login_btn = chrome.find_element_by_id('login-btn')
    elem_login_btn.click()
    print(elem_username.text)
finally:
    os.kill(chrome.service.process.pid,signal.SIGTERM)
