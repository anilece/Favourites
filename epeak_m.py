from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import os
import time
# instantiate a chrome options object so you can set the size and headless preference
chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--window-size=1920x1080")

# download the chrome driver from https://sites.google.com/a/chromium.org/chromedriver/downloads and put it in the
# current directory
chrome_driver = os.getcwd() +"\\chromedriver.exe"

# go to Google and click the I'm Feeling Lucky button
driver = webdriver.Chrome(chrome_options=chrome_options)
driver.get("https://voicenotebook.com/")
start=driver.find_element_by_xpath('//*[@id="recbtn"]')
print(start)
start.click()
print(start.text)
time.sleep(5)
driver.get_screenshot_as_file("capture6.png")
#start.click()
print(start.text)
result=driver.find_element_by_xpath('//*[@id="content"]/div[7]/input[1]')
result.click()
print(result.text)
driver.get_screenshot_as_file("capture5.png")