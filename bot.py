import os,random,sys,time
import pause, datetime
from selenium.webdriver.common.keys import Keys
from urllib.parse import urlparse
from selenium import webdriver
from countdown import countdown

class waktu():
    #Time to login (+-60s before flash sale)
    def loginTime():
        Year    = 2020
        Month   = 12
        Day     = 12
        Hour    = 13
        Minute  = 58
        Second  = 00
        dt = datetime.datetime(Year, Month, Day, Hour, Minute, Second, 000000)
        print("> START TIME ")
        print(datetime.datetime.now())
        print("> ACTION TIME ")
        print(dt)
        pause.until(dt)
        print("> LOGIN NOW! ")
    #Time to checkout (+-5 to load)
    def checkoutTime():
        Year    = 2020
        Month   = 12
        Day     = 12
        Hour    = 13
        Minute  = 59
        Second  = 59
        dt = datetime.datetime(Year, Month, Day, Hour, Minute, Second, 000000)
        print("> CHECKOUT TIME ")
        print(dt)
        pause.until(dt)

class Autocheck():
    def autocheck(self):
        print("Bot Running!\n")
        waktu.loginTime()

        targetFile = open("target.txt")
        readFile = targetFile.readlines()
        targetUrl = readFile[0]
        
        global browser
        options = webdriver.ChromeOptions()
        options.add_argument("--incognito")
        capabilities = options.to_capabilities()
        browser = webdriver.Chrome('webdriver/chromedriver_87', options=options)
        browser.get("https://shopee.co.id/buyer/login")
        # browser.get("https://www.google.com")

        waktu.checkoutTime()

        browser.find_element_by_tag_name('body').send_keys(Keys.COMMAND + 't') 
        browser.get(targetUrl)
        # browser.get("https://www.youtube.com")
        # print(browser.find_element_by_class_name('yt-simple-endpoint'))

        checkoutid = browser.find_element_by_css_selector('button.YtgjXY')
        print(checkoutid)
        checkoutid.send_keys('btn btn-solid-primary btn--l YtgjX')
        print("\n> Checkout!")

run = Autocheck()
run.autocheck()
