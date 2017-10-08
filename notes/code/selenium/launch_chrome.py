import time
from selenium import webdriver

driver = webdriver.Chrome('/usr/local/bin/chromedriver')  # Optional argument, if not specified will search path.
#driver = webdriver.Chrome('/Users/parrt/anaconda2/chromedriver-Darwin')  # Optional argument, if not specified will search path.
driver.get('http://www.google.com')

raw_input("Press Enter to quit")
# OR:
# time.sleep(3) # let the user see something
driver.quit()
