# Launch with python twitter_login.py
# or python twitter_login.py parrt@antlr.org
import time
import sys
from login import login
from selenium import webdriver

# If twitter detects unusual login activity it might ask for your email address
email = sys.argv[1] if len(sys.argv)>1 else "unknown@foo.com"
user,password = login()

driver = webdriver.Chrome('/usr/local/bin/chromedriver')
driver.get('https://twitter.com/i/flow/login')
time.sleep(4.0) # wait for JavaScript to execute

# ENTER USER
userfield = driver.find_element_by_name("username")
userfield.send_keys(user)
time.sleep(2.0)
next = driver.find_element_by_xpath("//*[contains(text(),'Next')]")
#print("button:", next)
next.click()
time.sleep(4.0)

# ENTER EMAIL if they have been detecting "unusual login activity"
try:
    enterphone = driver.find_element_by_name("text")
    print("Entering email")
    enterphone.send_keys(email)
    time.sleep(2.0)
    next = driver.find_element_by_xpath("//*[contains(text(),'Next')]")
    next.click()
    time.sleep(4.0)
except:
    # didn't need to enter our email address
    pass

# ENTER PASSWORD
passwordfield = driver.find_element_by_name("password")
passwordfield.send_keys(password)
time.sleep(2.0)
login = driver.find_element_by_xpath("//*[contains(text(),'Log in')]")
#print("Log in:", login)
time.sleep(2.0)
login.click()

input("Press Enter to quit")

driver.quit()
