import os,random,sys,time
import pause, datetime
from selenium.webdriver.common.keys import Keys
from urllib.parse import urlparse
from selenium import webdriver
from countdown import countdown
# from bs4 import BeautifulSoup

class waktu():
    #Edit time to 60 second (+-5s) before flash-sale
    def waktumundur1():
        Year    = 2020
        Month   = 12
        Day     = 11
        Hour    = 22
        Minute  = 16
        Second  = 00
        dt = datetime.datetime(Year, Month, Day, Hour, Minute, Second, 000000)
        print("> START TIME ")
        print(datetime.datetime.now())
        print("> ACTION TIME ")
        print(dt)
        pause.until(dt)
    #Your time to login before flash sale
    def waktumundur2():
        print("\n> LOGIN NOW!")
        menit = 0
        detik = 5
        countdown(menit,detik)

class Autocheck():
    def autocheck(self):
        print("Bot Running!\n")
        waktu.waktumundur1()

        targetFile = open("target.txt")
        readFile = targetFile.readlines()
        targetUrl = readFile[0]
        
        global browser
        global browser2
        options = webdriver.ChromeOptions()
        options.add_argument("--incognito")
        # options.add_argument("--disable-infobars")
        capabilities = options.to_capabilities()
        browser = webdriver.Chrome('webdriver/chromedriver_87', options=options)

        executor_url = browser.command_executor._url
        session_id = browser.session_id
        # browser.get("https://shopee.co.id/buyer/login")
        browser.get("https://www.google.com")

        waktu.waktumundur2()

        browser.find_element_by_tag_name('body').send_keys(Keys.COMMAND + 't') 

        browser.get("https://www.youtube.com")
        
        # options2 = webdriver.ChromeOptions()
        # options2.add_argument("--incognito")
        # options2.add_argument("--disable-infobars")
        # options2.add_argument("--enable-file-cookies")
        # options2.add_experimental_option("detach", True)
        # capabilities2 = options2.to_capabilities()
        # browser = webdriver.Remote(command_executor=executor_url, desired_capabilities=capabilities2)
        # # browser.close()
        # browser.session_id = session_id
        # # browser2.get(targetUrl)
        # browser.get("https://www.youtube.com")

        # checkoutid = browser.find_element_by_css_selector('button.YtgjXY')
        # print(checkoutid)
        # checkoutid.click()
        # print("\n> Checkout!")

run = Autocheck()
run.autocheck()