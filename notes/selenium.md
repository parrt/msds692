# Selenium 

## Installation

```bash
pip install -U selenium
pip install chromedriver
```

Download [Chrome driver binary](https://sites.google.com/a/chromium.org/chromedriver/downloads) as well. The pip stuff just makes the python packages but the real meat is in the binary download. I stored that executable binary in a standard place:

```bash
mv ~/Downloads/chromedriver /usr/local/bin
```

```python
import time
from selenium import webdriver

driver = webdriver.Chrome('/usr/local/bin/chromedriver')  # Optional argument, if not specified will search path.
driver.get('http://www.google.com');
search_box = driver.find_element_by_name('q')
search_box.send_keys('ChromeDriver')
search_box.submit()
time.sleep(5) # Let the user actually see something!
driver.quit()
```


to get the next page of results. This of course is not complete because it doesn’t get the actual data but it should give you something to start looking at and trying out. 

Basically it launches a Firefox browser and you can watch it “type” stuff in and click until it reaches the search results page. Then it will print all of that crap out and close the browser.

It turns out that there is quite a bit to learn in order to do this and it might be useful for others and so maybe we should all get together and I walk through how to do data acquisition when the output is complicated:

1. requires logging in
2. requires clicking on a bunch of stuff to dig into the middle of a website somewhere without a clear URL to jump to
3. requires executing JavaScript to get the generated HTML in order to scrape data

This might be enough to get you going so play around a bit and figure out what doesn’t make sense :) Naturally there’s a bunch of weird crap in there like XPath. Yet another skill to learn like regular expressions.
