#fixture
import pytest
from selenium import webdriver

@pytest.fixture(scope="function")
def browser():
    print("opening the broswer")
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get('https://webdriveruniversity.com/')
    yield driver
    driver.quit()

@pytest.fixture(scope="class")
def browser2():
    print("\n opening browser for test class ....")
    driver= webdriver.Chrome()
    driver.maximize_window()
    yield driver
    print("Closing a browser for test class")
    driver.quit()

@pytest.fixture(scope="module")
def browser3():
    print("\n opening browser for test class ....")
    driver= webdriver.Chrome()
    driver.maximize_window()
    driver.get('https://www.google.com')
    yield driver
    print("Closing a browser for test class")
    driver.quit()
