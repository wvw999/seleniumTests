# will run a selenium/python test in firefox against your local install of diaspora*
import time
from selenium import webdriver

driver = webdriver.Firefox()

try:
    config_file = open('config.json')
    data = json.load(config_file)

    driver.get('http://127.0.0.1:3000/')
    element = driver.find_element_by_id("user_username")
    element.send_keys(data['login'])
    element = driver.find_element_by_id("user_password")
    element.send_keys(data['password'])
    element = driver.find_element_by_name("commit")
    element.click()
    #looks for proof of login
    time.sleep(5)
    assert "Log out" in driver.page_source
    driver.save_screenshot("LoginResult.png")
    
finally:

    driver.quit()