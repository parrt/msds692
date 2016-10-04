from login import login
import time
from selenium import webdriver

user,password = login()

driver = webdriver.Chrome('/usr/local/bin/chromedriver')
driver.get('http://www.twitter.com/login')
userfield = driver.find_element_by_css_selector('.js-username-field.email-input.js-initial-focus')
userfield.send_keys(user)
passwordfield = driver.find_element_by_css_selector('.js-password-field')
passwordfield.send_keys(password)
passwordfield.submit()

driver.get('https://twitter.com/DataInstituteSF/following')

raw_input("Press Enter to quit")

driver.quit() # close browser
