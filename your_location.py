from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
# INIT CHROME OPTIONS
chrome_options = Options()
# 0 - Default, 1 - Allow, 2 - Block

# SET CHROME OPTIONS
chrome_options.add_experimental_option("prefs", { "profile.default_content_setting_values.geolocation": 1})

driver=webdriver.Chrome(options=chrome_options)
driver.get("https://the-internet.herokuapp.com/geolocation")
driver.find_element_by_xpath('//*[@id="content"]/div/button').click()
time.sleep(5)
print(driver.find_element_by_xpath('//*[@id="demo"]').text)
