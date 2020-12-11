import os,random,sys,time
import pause, datetime
from selenium.webdriver.common.keys import Keys
from urllib.parse import urlparse
from selenium import webdriver
from countdown import countdown

class Autocheck():
    def autocheck(self):
        targetFile = open("target.txt")
        readFile = targetFile.readlines()
        targetUrl = readFile[0]
        
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--incognito")
        global browser
        browser = webdriver.Chrome('webdriver/chromedriver_87', options=chrome_options)
        executor_url = browser.command_executor._url
        session_id = browser.session_id
        browser.get("https://shopee.co.id/buyer/login")
        print("Copy Session ID to other instance!")
        print(executor_url)
        print(session_id)

run = Autocheck()
run.autocheck()