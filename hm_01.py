import time
from appium import webdriver
capabilities = {
"platformName": "Android",
    "platformVersion": "5.1",
    "deviceName": "iPhone 7",
    "appPackage": "com.android.settings",
    "appActivity": ".Settings",
    "resetKeyboard": True,
    "unicodeKeyboard": True
}
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub',desired_capabilities=capabilities)
time.sleep(3)
driver.quit()
