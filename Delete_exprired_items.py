from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common import exceptions
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.expected_conditions import staleness_of
import time
import re


# initialize automated browser window, specify the browser we want to use
# store the path of the driver file in the brackets
driver = webdriver.Chrome("C:/zadachki/Different_Upwork_Projects/chromedriver_win32/chromedriver.exe")
# open the url you would like to request
driver.get("https://accounts.zalando.com/authenticate?request=eyJjbGllbnRfaWQiOiJmYXNoaW9uLXN0b3JlLXdlYiIsInJlc3BvbnNlX3R5cGUiOiJjb2RlIiwic2NvcGVzIjpbIm9wZW5pZCJdLCJyZWRpcmVjdF91cmkiOiJodHRwczovL3d3dy56YWxhbmRvLnNlL3Nzby9jYWxsYmFjayIsInN0YXRlIjoiZXlKdmNtbG5hVzVoYkY5eVpYRjFaWE4wWDNWeWFTSTZJbWgwZEhCek9pOHZkM2QzTG5waGJHRnVaRzh1YzJVdmJYbGhZMk52ZFc1MEx5SXNJblJ6SWpvaU1qQXlNUzB3T1Mwek1GUXhOVG94TURvek5sb2lmUT09Iiwibm9uY2UiOiIyNjNlMTc0ZC1kZGIzLTQ1ODEtOWJjMC04MDQ5ODZmNzFiYjYiLCJ1aV9sb2NhbGVzIjpbInN2LVNFIl0sInBrY2VfY2hhbGxlbmdlIjpudWxsLCJsb2dpbl9oaW50IjpudWxsLCJyZXF1ZXN0X2lkIjoieDI4MytWSUluT0FyaWljMTphNDk2ZWRkYi1mMjllLTQ4NTUtYTJiZi0xMzFkYjUyNTIwY2M6VE5oZDB2eXg4UWk0ZnZtbCIsImFjcl92YWx1ZXMiOltdLCJwcmVtaXNlIjpudWxsfQ==&preferred_language=sv-SE&available_languages=sv-SE&sales_channel=091dcbdd-7839-4f39-aa05-324eb4599df0")
driver.set_page_load_timeout(10)
time.sleep(2)

username = driver.find_element_by_xpath("//input[@name='login.email']")
password = driver.find_element_by_xpath("//input[@name='login.secret']")

username.send_keys("someusername,gmail.com")
password.send_keys("somepassword")
submit = driver.find_element_by_xpath("//button[@data-testid='login_button']").click()
time.sleep(4)

liked_clothes = driver.find_element_by_xpath("//a[@title='Önskelista']").click()
time.sleep(4)

num_liked_pieces = driver.find_element_by_xpath('//html/body/div/div/div/div/div/div/div/div/div/div/span').get_attribute("innerText") # long comment
NUM_raw = re.match("(^\d*)", num_liked_pieces)
Num_liked_final = int(NUM_raw.group(1))
print("There are {} items in your list at the website".format(Num_liked_final))

driver.find_element_by_xpath("//h3[text()='Gillade artiklar']").click()
time.sleep(4)


i = 1
while i <= int(Num_liked_final/20)+1:
    driver.execute_script("window.scrollTo(0, window.scrollY + 2478)")
    print("Scrolling down...")
    time.sleep(5)
    i = i + 1

items_list = driver.find_elements_by_css_selector("div.v9kdwN")
print('You are scraping information about {} items.'.format(len(items_list)))

sold_items = []
expired_items = []
for item in items_list:
    try:
        expired = item.find_element_by_xpath(".//*[text()='Inte tillgänglig']")
        expired_items.append(expired)
    except:
        pass

for item in items_list:
    try:
        sold = item.find_element_by_xpath(".//*[text()='Slutsåld']")
        sold_items.append(sold)
    except:
        pass

print("From {} liked items there are\n{} expired items\n and\n{} sold out items.".format(len(items_list), expired_items, sold_items))

while True:
    try:
        driver.find_element_by_xpath("//*[text()='Inte tillgänglig']").find_element_by_xpath('..').find_element_by_xpath('..').find_element_by_tag_name("button").click() #long comment
        time.sleep(11)
    except ElementClickInterceptedException:
        driver.execute_script("window.scrollTo(0, window.scrollY + 500)")
        print("Scrolling down...")
        continue
    except TimeoutException:
        print("Can't find any expired items.")
        break
    except NoSuchElementException:
        print("No such Element")
        break


