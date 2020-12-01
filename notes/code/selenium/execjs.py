import time
from selenium import webdriver

driver = webdriver.Chrome('/usr/local/bin/chromedriver')  # Optional argument, if not specified will search path.
driver.get('file:///tmp/gendom.html')
p = driver.find_element_by_id('stuff')
print("TEXT:",p.text)

input("Press Enter to quit")

driver.quit() # close browser
