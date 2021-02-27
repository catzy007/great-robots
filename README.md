# Great Bot

### Dependency

#### Software version
```
python 3.8.5
pip 20.0.2
chrome 87.0.4280.88
chrome web driver 87.0.4280.88
```

#### Python library
```
pip install pause
pip install selenium
pip install beautifulsoup4
```

#### Chrome + web Driver
<https://chromedriver.chromium.org/downloads>

<https://www.google.com/chrome/>

### How to use?
* Install all dependency and software stack
* Download install and check your `Chrome version`
* Download `Chrome Web driver` matched with your `Chrome version`
* Move downloaded `Chrome Web Driver` to `webdriver`
* Open `bot.py` and change `webdriver.Chrome('webdriver/chromedriver_XY'` to `webdriver.Chrome('webdriver/chromedriver_XY.exe'` if you use MS-Windows (change XY to your `Chrome Webdriver Version`)
* Make sure all things installed and work properly
* Go to `target.txt` and paste `product link`
* Open `Bot.py` and adjust `loginTime()` to login time (-60 to -120 second before checkout)
* Then adjust `checkoutTime()` to checkout time (+- 1 to 5 second to load)
* Run `Bot.py` and wait
* After login window appear, proceed to login
* Wait few second and purchase window wil appear
* Then finish your payment

> This code is build and modified from many sources!
