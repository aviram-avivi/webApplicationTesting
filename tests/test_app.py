import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest

@pytest.fixture
def browser():
    from selenium import webdriver
    from selenium.webdriver.chrome.options import Options
    from selenium.webdriver.chrome.service import Service
    from webdriver_manager.chrome import ChromeDriverManager

    chrome_options = Options()
    chrome_options.add_argument("--headless")  # Run in headless mode
    chrome_options.add_argument("--no-sandbox")  # Bypass OS security model
    chrome_options.add_argument("--disable-dev-shm-usage")  # Overcome limited resource problems

    service = Service(ChromeDriverManager().install())
    browser = webdriver.Chrome(service=service, options=chrome_options)
    yield browser
    browser.quit()


def test_valid_input(browser):
    valid_names = ["Alice", "Bob", "Charlie"]
    for name in valid_names:
        browser.get('http://127.0.0.1:5000/')
        name_input = browser.find_element(By.NAME, 'name')
        name_input.send_keys(name)
        name_input.send_keys(Keys.RETURN)
        greeting = browser.find_element(By.TAG_NAME, 'h1').text
        assert greeting == f'Hello, {name}!'
        # Optionally, add more assertions here if you want to check other aspects of the response


def test_empty_input(browser):
    browser.get('http://127.0.0.1:5000/')
    name_input = browser.find_element(By.NAME, 'name')
    name_input.send_keys('')
    name_input.send_keys(Keys.RETURN)

    # Check if the browser has navigated to the /greet page
    assert 'greet' in browser.current_url

    # Check if the greeting is as expected (Hello,!)
    greeting = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.TAG_NAME, 'h1'))
    ).text
    assert greeting == 'Hello, !'

