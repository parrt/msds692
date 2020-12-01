import sys
import time
from selenium import webdriver

query = "USF data science"
if len(sys.argv)>1:
	query = sys.argv[1]

driver = webdriver.Chrome('/usr/local/bin/chromedriver')  # Optional argument, if not specified will search path.
driver.get('http://www.google.com')
search_box = driver.find_element_by_name('q')
search_box.send_keys(query)
search_box.submit()

input("Press Enter to quit")

driver.quit() # close browser
