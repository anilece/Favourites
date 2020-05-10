from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
import selenium.common.exceptions
from selenium.webdriver.support import expected_conditions as EC
def find_element(id):
    return driver.find_element_by_id(id)

def wait_exp(xpath):
    wait=WebDriverWait(driver,20)
    element=wait.until(EC.element_to_be_clickable((By.XPATH,xpath)))
    return element


#driver=webdriver.Chrome(executable_path="/Users/anilrz/Downloads/chromedriver")
driver=webdriver.Chrome(executable_path="/Users/anilrz/Downloads/chromedriver")
driver.get("https://www.amazon.com/ap/signin?_encoding=UTF8&openid.assoc_handle=usflex&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.mode=checkid_setup&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0&openid.ns.pape=http%3A%2F%2Fspecs.openid.net%2Fextensions%2Fpape%2F1.0&openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon.com%2Fgp%2Fyourstore%2Fhome%3Fie%3DUTF8%26action%3Dsign-out%26path%3D%252Fgp%252Fyourstore%252Fhome%26ref_%3Dnav_youraccount_signout%26signIn%3D1%26useRedirectOnSuccess%3D1")
#//*[@id="ordersContainer"]/div[@class="a-box-group a-spacing-base order"]/div[1]/div/div/div/div[1]/div/div[2]/div[2]/span
find_element(id="ap_email").send_keys("priyann+vermont2@amazon.com")
find_element(id="continue").click()
find_element(id="ap_password").send_keys("123456")
find_element(id="signInSubmit").click()
wait_exp('//*[@id="nav-orders"]/span[2]').click() #your orders
wait_exp('//*[@id="orderTypeMenuContainer"]/ul/li[5]').click() # digital or
#ordername= driver.find_elements_by_xpath('//*[@id="ordersContainer"]/div[@class="a-box-group a-spacing-base order"]/div[2]/div/div/div[1]')
ordercost= driver.find_elements_by_xpath('//*[@id="ordersContainer"]/div[@class="a-box-group a-spacing-base order"]/div[1]/div/div/div/div[1]/div/div[2]/div[2]/span')
orders=driver.find_elements_by_class_name("a-fixed-left-grid-inner")
ordername=[]
for i in range(len(ordercost)):
    print(ordercost[i].text)
for i in range(len(orders)):
        p=(orders[i].text.split("\n"))
        if p[0]!="":
            ordername.append(p[0])

print(ordername)






# orders_current_page=driver.find_elements_by_xpath("//span[@class='a-color-secondary value']")
# print(len(orders_current_page),len(ordername))