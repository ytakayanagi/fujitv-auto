import sys
import os
import random
import string
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.support import ui
from selenium.webdriver.common.keys import Keys
import time
from ctypes import *

def page_is_loaded(driver):
    return driver.find_element_by_tag_name("body") != None

# Generate random combination of letters and digits
random = ''.join([random.choice(string.ascii_lowercase + string.digits) for n in xrange(20)])
file = open('random.txt','w')
file.write(random)
file.close()
file = open('random.txt','r')
random = file.read()
file.close()

# Account information
emailStr = random + '@harakirimail.com'
passwordStr = '0411'

# Open the register page and create an account
driver = webdriver.Chrome("chromedriver.exe")
driver.get(("https://fujitv.live/register"))
wait = ui.WebDriverWait(driver, 10)
wait.until(page_is_loaded)

email = driver.find_element_by_name("account")
email.send_keys(emailStr)

password = driver.find_element_by_name("password")
password.send_keys(passwordStr)

conpassword = driver.find_element_by_name("conpassword")
conpassword.send_keys(passwordStr)

agreement = driver.find_element_by_id("agree")
agreement.click()

create = driver.find_element_by_class_name("btn")
create.click()

time.sleep(2)

driver.close()

# Open the email to verify account
driver = webdriver.Chrome("chromedriver.exe")
driver.get(("https://harakirimail.com/inbox/" + random))
wait = ui.WebDriverWait(driver, 10)
wait.until(page_is_loaded)

subject = driver.find_element_by_link_text("Fujitv.live account activation")
subject.click()

driver.get = driver.current_url

verify = driver.find_element_by_partial_link_text("https://crm.fujitv.live/activate")
verify.click()

time.sleep(2)

driver.close()

# Login to FujiTV
driver = webdriver.Chrome("chromedriver.exe")
driver.get(("https://fujitv.live/logon"))
wait = ui.WebDriverWait(driver, 10)
wait.until(page_is_loaded)

email = driver.find_element_by_name("account")
email.send_keys(emailStr)

password = driver.find_element_by_name("password")
password.send_keys(passwordStr)

login = driver.find_element_by_class_name('login')
login.click()
