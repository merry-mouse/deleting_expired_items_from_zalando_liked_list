# necessary libraries and modules

from selenium import webdriver
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException
import time
import re

# open the browser
print("Openning browser...\n\n")

# initialize automated browser window, specify the browser we want to use
# store the path of the driver file in the brackets
driver = webdriver.Chrome("C:/zadachki/Different_Upwork_Projects/chromedriver_win32/chromedriver.exe")
# open the url you would like to request
driver.get("https://accounts.zalando.com/authenticate?request=eyJjbGllbnRfaWQiOiJmYXNoaW9uLXN0b3JlLXdlYiIsInJlc3BvbnNlX3R5cGUiOiJjb2RlIiwic2NvcGVzIjpbIm9wZW5pZCJdLCJyZWRpcmVjdF91cmkiOiJodHRwczovL3d3dy56YWxhbmRvLnNlL3Nzby9jYWxsYmFjayIsInN0YXRlIjoiZXlKdmNtbG5hVzVoYkY5eVpYRjFaWE4wWDNWeWFTSTZJbWgwZEhCek9pOHZkM2QzTG5waGJHRnVaRzh1YzJVdmJYbGhZMk52ZFc1MEx5SXNJblJ6SWpvaU1qQXlNUzB3T1Mwek1GUXhOVG94TURvek5sb2lmUT09Iiwibm9uY2UiOiIyNjNlMTc0ZC1kZGIzLTQ1ODEtOWJjMC04MDQ5ODZmNzFiYjYiLCJ1aV9sb2NhbGVzIjpbInN2LVNFIl0sInBrY2VfY2hhbGxlbmdlIjpudWxsLCJsb2dpbl9oaW50IjpudWxsLCJyZXF1ZXN0X2lkIjoieDI4MytWSUluT0FyaWljMTphNDk2ZWRkYi1mMjllLTQ4NTUtYTJiZi0xMzFkYjUyNTIwY2M6VE5oZDB2eXg4UWk0ZnZtbCIsImFjcl92YWx1ZXMiOltdLCJwcmVtaXNlIjpudWxsfQ==&preferred_language=sv-SE&available_languages=sv-SE&sales_channel=091dcbdd-7839-4f39-aa05-324eb4599df0")
driver.set_page_load_timeout(10)
time.sleep(2)

# login to the acoount
print("Login to the account...\n\n")
username = driver.find_element_by_xpath("//input[@name='login.email']")
password = driver.find_element_by_xpath("//input[@name='login.secret']")
username.send_keys("someusername.gmail.com")
password.send_keys("somepassword")
submit = driver.find_element_by_xpath("//button[@data-testid='login_button']").click()
time.sleep(4)

# clicking on list of favorite items
print("Clicking on the list of favorite items...\n\n")
liked_clothes = driver.find_element_by_xpath("//a[@title='Önskelista']").click()
time.sleep(4)

# checking how many items in your list on the website
print("Checking how many liked items in your list...\n\n")
num_liked_pieces = driver.find_element_by_xpath('//html/body/div/div/div/div/div/div/div/div/div/div/span').get_attribute("innerText") # long comment
NUM_raw = re.match("(^\d*)", num_liked_pieces)
Num_liked_final = int(NUM_raw.group(1))
print("There are {} items in your list at the website. Check if matches with the number on the website.".format(Num_liked_final))

# open the list of liked items (there are also "bought items" there but we don't need them)
print("Openning the list of liked items...\n\n")
driver.find_element_by_xpath("//h3[text()='Gillade artiklar']").click()
time.sleep(4)

# scrolling until the end of the page to scrape all the info
print("Getting info about all the pieces by scrolling until the bottom of the page...\n\n")
i = 1
while i <= int(Num_liked_final/20)+1:
    driver.execute_script("window.scrollTo(0, window.scrollY + 2478)")
    print("Scrolling down...")
    time.sleep(5)
    i = i + 1

# checking the number of items to scrape, also checking if there are any sold out or expired items
items_list = driver.find_elements_by_css_selector("div.v9kdwN")
all_items_length = len(items_list)
print("You are scraping information about {} items.\n\n".format(all_items_length))
print("Counting the number of expired and sold out items...\n\n")
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
length_expired = len(expired_items)
length_soldout = len(sold_items)
# print out the result for the user
print("From {} liked items there are\n{} expired items\n and\n{} sold out items.\n\n".format(all_items_length, length_expired, length_soldout))

def delete_expired_items():
    print("deleting all the expired items...\n\n")
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


def delete_soldout_items():
    print("deleting all the sold out items...\n\n")
    while True:
        try:
            driver.find_element_by_xpath("//*[text()='Slutsåld']").find_element_by_xpath('..').find_element_by_xpath('..').find_element_by_xpath('..').find_element_by_xpath('..').find_element_by_xpath('..').find_element_by_xpath('..').find_element_by_xpath('..').find_element_by_tag_name("button").click() #long comment
            time.sleep(11)
        except ElementClickInterceptedException:
            driver.execute_script("window.scrollTo(0, window.scrollY + 500)")
            print("Scrolling down...")
            continue
        except TimeoutException:
            print("TimeoutException\nCan't find any expired items.")
        except NoSuchElementException:
            print("No such Element")
            break
    print("Done with all the tasks!\n\n")

# initiating function depends on results of the count and user's input
def check_if_expired_or_soldout():
    if length_soldout > 0:
        should_delete_soldout = input(("There are {} sold out items found. Would you like to remove them from the list?"
                              "\nanswer 'y' for yes, 'n' for no.\nPRINT ANSWER: ").format(length_soldout))
        if should_delete_soldout == "y":
            delete_soldout_items()
        else:
            print("okay, I won't remove them then =)...\nContinue with the code...\n\n")
    elif length_soldout == 0:
        print("There are 0 sold items, nothing to remove.")
    if length_expired > 0:
        should_delete_expired = input(("There are {} expired items found. Would you like to remove them from the list?"
                                      "\nanswer 'y' for yes, 'n' for no.\nPRINT ANSWER: ").format(length_expired))
        if should_delete_expired == "y":
            delete_expired_items()
        else:
            print("okay, I won't remove them then =)...\nContinue with the code...\n\n")
    elif len(expired_items) == 0:
        print("There are 0 expired items, nothing to remove.\n\n")


check_if_expired_or_soldout()
# ending the program
print("All done! See you next time!")