import time
from selenium import webdriver

driver = webdriver.Chrome('/usr/local/bin/chromedriver')  # Optional argument, if not specified will search path.
# or, fill in your ANACONDA_INSTALL_DIR and try this:
# driver = webdriver.Chrome('ANACONDA_INSTALL_DIR/chromedriver-Darwin')

driver.get('http://www.google.com')

# here is where some useful work would typically happen

input("Press Enter to quit")
driver.quit() # close browser
