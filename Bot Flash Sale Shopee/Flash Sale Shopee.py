
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

import time 

PATH = "D:/bot_shopee/chromedriver.exe" 
driver = webdriver.Chrome(PATH)

email = "email saya"
password = "password saya"

login_link = "https://shopee.co.id/buyer/login"

product_link = "https://shopee.co.id/V8-Full-Hd-Webcam-1080P-With-Microphone-Web-cam-FULL-HD-1080-P-i.61050481.3238894052"

driver.get(login_link)

time.sleep(3)

user = driver.find_element_by_class_name('_56AraZ')
user.send_keys(email)

time.sleep(1)

pwd = driver.find_element_by_xpath("//input[@name='password']")
pwd.send_keys(password)

time.sleep(1)

login_button = driver.find_element_by_xpath("//button[@class='_35rr5y _32qX4k _1ShBrl _3z3XZ9 _2iOIqx _2h_2_Y']")
login_button.click()

time.sleep(2)

driver.get(product_link)

time.sleep(2)

buy_out = driver.find_element_by_xpath("//button[@class='btn btn-solid-primary btn--l YtgjXY']")
buy_out.click()
