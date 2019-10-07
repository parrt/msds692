from login import login
import time
from selenium import webdriver

user,password = login()

driver = webdriver.Chrome('/usr/local/bin/chromedriver')
driver.get('http://www.twitter.com/login')
userfield = driver.find_element_by_class_name("js-username-field")
userfield.send_keys(user)
passwordfield = driver.find_element_by_class_name("js-password-field")
passwordfield.send_keys(password)
passwordfield.submit()

input("Press Enter to quit")

driver.quit()
