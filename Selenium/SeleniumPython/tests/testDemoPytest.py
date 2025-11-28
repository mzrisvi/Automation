# This is Pytest script for Selenium in Python
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
    
def test_fill_form(driver):
    # Open a webpage
    driver.get("https://trytestingthis.netlify.app/")
    
    # Find elements by their ID attributes and fill the form
    driver.find_element(By.ID, "fname").send_keys("Mohammad")
    driver.find_element(By.ID, "lname").send_keys("Risvi")
    
    # Wait for a few seconds to see the results
    time.sleep(5)
    
    # Click the submit button
    driver.find_element(By.XPATH, "/html[1]/body[1]/div[3]/div[2]/form[1]/fieldset[1]/button[1]").click()

