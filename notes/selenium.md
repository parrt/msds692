# Selenium 

We have seen how to use Python programs to scrape data from websites, but there are three scenarios that make it more challenging

1. Accessing data behind login screens
2.  Having to click through a bunch of stuff to dig into the middle of a website somewhere without a clear URL to jump to
3. Accessing data that is the result of executing JavaScript

[Selenium](http://www.seleniumhq.org/) is a tool that lets us automate actions within a browser as if we were clicking or typing as a human. This lets us login and do anything else a human can do when using the browser. Perhaps most importantly, it allows us to scrape data from webpages that generate HTML using JavaScript executing within the browser; i.e., there are some webpages that are pure JavaScript and no HTML.

## Installation

```bash
pip install -U selenium
pip install chromedriver # if you plan on automating chrome usage
```

Download [Chrome driver binary](https://sites.google.com/a/chromium.org/chromedriver/downloads) as well and/or [FireFox's gecko driver](https://github.com/mozilla/geckodriver/releases). Get `geckodriver-v0.9.0` not v0.10. The pip stuff just makes the python packages but the real meat is in the binary download. I stored the executable binaries in a standard place:

```bash
mv ~/Downloads/chromedriver /usr/local/bin
mv ~/Downloads/geckodriver /usr/local/bin
```

Oh wait. ok, a serious bug prevents firefox usage for 0.9 but 0.10 didn't work either. Ok, Chrome it is. 

## Launching a Chrome Browser

Here is the boilerplate code that launches a chrome browser to the Google search page, waits 5 seconds, and then closes the browser.

```python
import time
from selenium import webdriver

driver = webdriver.Chrome('/usr/local/bin/chromedriver')  # Optional argument, if not specified will search path.
driver.get('http://www.google.com')
# where some useful work would typically happen
time.sleep(5)
driver.quit()
```

Notice that this is creating an entirely new instance of the browser (You'll see more a new chrome icon appear).

## Puppeteering with Chrome Browser

Let's start by asking chrome to perform a search for `USF Analytics`. The
[Selenium python API doc](http://selenium-python.readthedocs.io/locating-elements.html#locating-elements) shows us that we can find elements by name. Conveniently the name of the search entry box is `q`, determined by using `inspect` functionality in the chrome browser itself:

<img src=figures/google-searchbox.png width=500>

Using the boilerplate code from the previous section, we would add the following functionality.

```python
search_box = driver.find_element_by_name('q')
search_box.send_keys('USF Analytics')
search_box.submit()
```