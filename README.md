# Delete expired items from Zalando list

This small Python program was created to automate a process of deleting expired and sold out items from [Zalando](https://www.zalando.se) personal account.

## Installation of necessary libraries and modules

You need just 3 libraries to be installed in the same directory with the code.
Use the package manager [pip](https://pip.pypa.io/en/stable/)


 Libraries:
- selenium
- re
- time
Packages:
- webdriver
- ElementClickInterceptedException
- TimeoutException
- NoSuchElementException

```python
from selenium import webdriver
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException
```

## User's variables
There are 3 variables that must be set in the beginning

```python
# choose driver you want to use (here I use Chrome) and put the path to it in brackets
driver = webdriver.Chrome("C:/path_to_the_driver/chromedriver.exe")

# your personal account info
username.send_keys("someusername.gmail.com")
password.send_keys("somepassword")
```

## User's input

if program finds any sold out or expired items it will ask if the user wants to delete them 
and proceed according to the answer.

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.