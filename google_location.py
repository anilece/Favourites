from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import selenium.common.exceptions
import time
import pyttsx3
engine=pyttsx3.init()
def wait_exp(xpath):
    wait=WebDriverWait(driver,20)
    element=wait.until(EC.element_to_be_clickable((By.XPATH,xpath)))
    return element


options=Options()
options.add_experimental_option("prefs", { "profile.default_content_setting_values.geolocation": 1})
driver= webdriver.Chrome(options=options)

driver.get("https://www.google.com/maps")
driver.implicitly_wait(10)
time.sleep(10)
#driver.find_element_by_xpath('/html/body/jsl/div[3]/div[9]/div[3]/div[1]/div[2]/div/div[3]/div[1]/div[2]/div[2]/button[1]').click()
#
#driver.find_element_by_xpath('//*[@id="section-directions-trip-0"]/div[2]/div[3]/div[4]/button').click()
wait_exp('//*[@id="searchbox-directions"]').click()

wait_exp('/html/body/jsl/div[3]/div[9]/div[3]/div[1]/div[2]/div/div[3]/div[1]/div[1]/div[2]/div/div/input').send_keys("")
wait_exp('/html/body/jsl/div[3]/div[9]/div[3]/div[1]/div[2]/div/div[3]/div[1]/div[2]/div[2]/div/div/input').send_keys("avadi")
wait_exp("/html/body/jsl/div[3]/div[9]/div[3]/div[1]/div[2]/div/div[2]/div/div/div[1]/div[4]/button/div[1]").click()
wait_exp('/html/body/jsl/div[3]/div[9]/div[8]/div/div[1]/div/div/div[5]/div[1]/div[2]/div[3]/div[4]/button').click()
print("Got input = police station nearby")
print("DIRECTIONS ARE ==>")
directions=wait_exp('//*[@id="pane"]/div/div[1]/div/div/div[5]/div/div/div[1]/div/div[2]/div[3]/div[1]').text

directions=directions.split("\n")
for line in directions:
    try :
        print(line)
        re=''
        for i in line.split():
            if i.isdigit():
                re+=i
                print(re)
        res=re
        print("number "+res)
        engine.say(res)
        #time.sleep(int(res))
        engine.runAndWait()
    except:
        pass
driver.close()