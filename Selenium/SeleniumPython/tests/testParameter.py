# This is a Parameterized test example using pytest and Selenium
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

@pytest.fixture
def driver():
    # Initialize the WebDriver
    driver = webdriver.Chrome()
    yield driver
    # Close the browser after test
    driver.quit()
    
@pytest.mark.parametrize("first_name, last_name", [
    ("Mohammad", "Risvi"),
    ("Jane", "Smith"),
    ("Alice", "Johnson"),
])

def test_parameterized_form(driver, first_name, last_name):
    # Open a webpage
    driver.get("https://trytestingthis.netlify.app/")
    
    # Find elements by their ID attributes and fill the form
    driver.find_element(By.ID, "fname").send_keys(first_name)
    driver.find_element(By.ID, "lname").send_keys(last_name)
    
    # Wait for a few seconds to see the results
    time.sleep(3)
    
    # Click the submit button
    driver.find_element(By.XPATH, "/html[1]/body[1]/div[3]/div[2]/form[1]/fieldset[1]/button[1]").click()
