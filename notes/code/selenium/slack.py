# slack is a "single-page app" that uses JavaScript
# to display data, rather than sending HTML with data
# to your browser.

from login import login
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

driver.get('https://lang-wichteam.slack.com/messages/lang-wich/')

raw_input("Press Enter to quit")

driver.quit() # close browser
