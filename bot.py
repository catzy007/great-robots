import os,random,sys,time
import pause, datetime
from selenium.webdriver.common.keys import Keys
from urllib.parse import urlparse
from selenium import webdriver
# from bs4 import BeautifulSoup

class waktu():
   def waktumundur():
        Year    = 2020
        Month   = 12
        Day     = 11
        Hour    = 21
        Minute  = 56
        Second  = 00
        dt = datetime.datetime(Year, Month, Day, Hour, Minute, Second, 000000)
        print("Start Time ")
        print(datetime.datetime.now())
        print("Action Time ")
        print(dt)
        pause.until(dt)

class Autocheck():
    def autocheck(self):
        print("Bot Running\n")
        waktu.waktumundur()
        
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--incognito")
        global browser
        browser = webdriver.Chrome('webdriver/chromedriver_87', options=chrome_options)
        targetFile = open("target.txt")
        readFile = targetFile.readlines()
        targetUrl = readFile[0]
        browser.get(targetUrl)

        #checkoutid = browser.find_element_by_class_name('btn btn-solid-primary btn--l YtgjXY')
        #checkoutid = browser.find_element_by_link_text("Beli Sekarang")
        checkoutid = browser.find_element_by_css_selector('button.YtgjXY')
        print(checkoutid)
        checkoutid.click()
        # checkoutid.send_keys('btn btn-solid-primary btn--l YtgjX')
        print("\nCheckout!")

run = Autocheck()
run.autocheck()