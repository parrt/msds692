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
    driver.get('https://lang-wichteam.slack.com/')
    userfield = driver.find_element_by_id('email')
    userfield.send_keys(user)
    passwordfield = driver.find_element_by_id('password')
    passwordfield.send_keys(password)
    passwordfield.submit()

    driver.get('https://lang-wichteam.slack.com/messages/'+channel)

def parse_slack():
    "Return list of (user,messages)"
    time.sleep(5) # have to wait for slack app to pull data from server and render it.
    msgs = driver.find_elements_by_tag_name('ts-message')
    # msgs = driver.find_elements_by_xpath("//*[@data-member-id]")
    data = []
    for wrapper in msgs:
        msg = wrapper.find_element_by_class_name("message_body").text
        user_icon_div = wrapper.find_element_by_class_name("message_icon")
        user_link = user_icon_div.find_element_by_tag_name('a')
        href = user_link.get_attribute('href')
        user = re.search(r'/team/([a-zA-Z0-9]+)', href).group(1)
        data.append((user,msg))
    return data

login_and_show_channel("lang-wich")
msgs = parse_slack()
for user,msg in msgs:
    print "%s: %s" % (user, msg)

raw_input("Press Enter to quit")
driver.quit() # close browser
