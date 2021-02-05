# will run a selenium/python test in firefox against your local install of diaspora*
import time
import json
from selenium import webdriver

driver = webdriver.Firefox()   

try:
    config_file = open('config.json')
    data = json.load(config_file)

    print(data['password'])
    driver.get('http://127.0.0.1:3000/')
    element = driver.find_element_by_id("user_username")
    element.send_keys(data['login'])
    element = driver.find_element_by_id("user_password")
    element.send_keys(data['password'])
    element = driver.find_element_by_name("commit")
    element.click()
    #Creates a test post, waits for page to refresh, stores screenshot
    element = driver.find_element_by_id("status_message_text")
    element.send_keys("antelope")
    element = driver.find_element_by_id("submit")
    element.click()
    time.sleep(5)
    assert "antelope" in driver.page_source
    driver.save_screenshot("result.png")
    
finally:

    driver.quit()