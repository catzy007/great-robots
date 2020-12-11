import os,random,sys,time
import pause, datetime
from selenium.webdriver.common.keys import Keys
from urllib.parse import urlparse
from selenium import webdriver
from countdown import countdown

class waktu():
    #Edit time to -120 second (+-5s) before flash-sale
    def waktumundur1():
        Year    = 2020
        Month   = 12
        Day     = 11
        Hour    = 58
        Minute  = 00
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
        detik = 118
        countdown(menit,detik)

class Autocheck():
    def autocheck(self):
        print("Bot Running!\n")
        waktu.waktumundur1()

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

        waktu.waktumundur2()

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