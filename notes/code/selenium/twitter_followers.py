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

driver.execute_script("window.scrollTo(0, 10000);") # scroll down
driver.execute_script("window.scrollTo(0, 10000);") # scroll down some more

links = driver.find_elements_by_class_name('ProfileNameTruncated-link')

links = [(link.get_attribute('href'),link.text) for link in links]

print links

raw_input("Press Enter to quit")

driver.quit() # close browser
