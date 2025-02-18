# Fixtures
# function 
# class
# module 
# session
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# Set up the WebDriver (e.g., Chrome)
def test_verify_title(browser):
    actual = browser.title
    assert actual == 'WebDriverUniversity.com'
    

def test_verify_link(browser):
    actual =  browser.find_element(By.CSS_SELECTOR,"#contact-us > div > div.section-title > h1").is_displayed()
    assert actual == True
    



