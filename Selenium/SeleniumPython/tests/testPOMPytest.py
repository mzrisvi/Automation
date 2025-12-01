# This is POM with Pytest
import pytest
import time
from selenium import webdriver
from Pages.loginPage import LoginPage

@pytest.fixture
def driver():
    # Initialize the WebDriver
    driver = webdriver.Chrome()
    yield driver
    # Close the browser after test
    driver.quit()
    
@pytest.mark.parametrize("username, password", [
    ('test', 'test'),
    ("testuser1", "password1"),
    ("testuser2", "password2"),
])


def test_POM_form(driver, username, password):
    # Create an instance of LoginPage
    login_page = LoginPage(driver)
    
    # Open a webpage
    login_page.open_Page("https://trytestingthis.netlify.app/")
    
    # Find elements by their ID attributes and fill the form
    login_page.enter_username(username)
    login_page.enter_password(password)
    
    # Wait for a few seconds to see the results
    time.sleep(5)
    
    # Click the Login button
    login_page.click_login()
    
    # Add assertions as needed
    assert "Successful" in driver.page_source
# End of POM with Pytest

