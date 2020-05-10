
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import selenium.common.exceptions

import time
options=Options()
options.add_argument("--use--fake-ui-for-media-stream")
driver=webdriver.Chrome(options=options)
driver.get("https://www.where-am-i.net/")
wait=WebDriverWait(driver,20)
element=wait.until(EC.element_to_be_clickable((By.XPATH,"//*[@id='location']")))
print(driver.find_element_by_xpath('//*[@id="location"]').text)