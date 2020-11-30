# slack is a "single-page app" that uses JavaScript
# to display data, rather than sending HTML with data
# to your browser.
import re

from login import login
import time
from selenium import webdriver

driver = webdriver.Chrome('/usr/local/bin/chromedriver')
# driver.implicitly_wait(10) # seconds

def login_and_show_channel(channel):
    user,password = login()
    
    driver.get('https://msan-usf.slack.com/')
    userfield = driver.find_element_by_id('email')
    time.sleep(3)
    userfield.send_keys(user)
    passwordfield = driver.find_element_by_id('password')
    passwordfield.send_keys(password)
    passwordfield.submit()

    driver.get('https://msan-usf.slack.com/messages/'+channel)

def parse_slack():
    "Return list of (user,messages)"
    time.sleep(5) # have to wait for slack app to pull data from server and render it.
    msg_wrappers = driver.find_elements_by_class_name('c-message_kit__message')
    data = []
    for wrapper in msg_wrappers:
        print(wrapper)
        try:
            msg = wrapper.find_element_by_class_name("p-rich_text_block")
        except:
            print("can't find message body")
            continue
        try:
            user_link = wrapper.find_element_by_class_name("c-message__sender")
            user = user_link.text
        except:
            # no user just means "previous user"
            user = "previous-user"
        data.append((user,msg.text))
    return data

login_and_show_channel("general")
msgs = parse_slack()
for user,msg in msgs:
    if user!='previous user':
        print()
    print(f"{user}: {msg}")

input("Press Enter to quit")
driver.quit() # close browser
