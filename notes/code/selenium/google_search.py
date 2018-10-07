import time
from selenium import webdriver

driver = webdriver.Chrome('/usr/local/bin/chromedriver')  # Optional argument, if not specified will search path.
driver.get('http://www.google.com')
search_box = driver.find_element_by_name('q')
search_box.send_keys('USF data science')
search_box.submit()

input("Press Enter to quit")

driver.quit() # close browser
