# Running web-based tests with Selenium

See the Selenium [documentation](http://selenium-python.readthedocs.io/).

Install geckodriver for Firefox. See the Selenium [download page](http://www.seleniumhq.org/download/). Works with v0.19.1.

Install the pytest-selenium package, which automatically includes dependencies.

```
$ pip3 install pytest-selenium
```

See its [documentation](http://pytest-selenium.readthedocs.io/en/latest/index.html) for usage instructions. The 'selenium' object is an instance of the WebDriver.
