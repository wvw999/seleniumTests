# will run a selenium/python test in firefox against your local install of diaspora*
import time
from selenium import webdriver

driver = webdriver.Firefox()

try:

    driver.get('http://127.0.0.1:3000/')
    element = driver.find_element_by_id("user_username")
    element.send_keys("YOURLOGINID")
    element = driver.find_element_by_id("user_password")
    element.send_keys("YOURPASSWORD")
    element = driver.find_element_by_name("commit")
    element.click()
    #Creates a test post, waits for page to refresh, stores screenshot
    element = driver.find_element_by_id("status_message_text")
    element.send_keys("antelope")
    element = driver.find_element_by_id("submit")
    element.click()
    time.sleep(5)
    driver.save_screenshot("result.png")
    
finally:

    driver.quit()