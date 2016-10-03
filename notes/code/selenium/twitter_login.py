from login import login
import time
from selenium import webdriver

user,password = login()

driver = webdriver.Chrome('/usr/local/bin/chromedriver')
driver.get('https://lang-wichteam.slack.com/')
userfield = driver.find_element_by_id('email')
userfield.send_keys(user)
userfield = driver.find_element_by_id('email')
passwordfield = driver.find_element_by_id('password')
passwordfield.send_keys(password)
passwordfield.submit()

driver.get('https://lang-wichteam.slack.com/messages/general/')

raw_input("Press Enter to quit")

driver.quit() # close browser
