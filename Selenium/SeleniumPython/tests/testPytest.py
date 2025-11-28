# File: test_google_search.py

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

def test_google_search():
    # 1. Launch Chrome browser
    driver = webdriver.Chrome()  # Make sure chromedriver is in PATH or in same folder
    
    try:
        # 2. Open Google
        driver.get("https://www.google.com")

        # 3. Find the search box and type "pytest"
        search_box = driver.find_element(By.NAME, "q")
        search_box.send_keys("pytest")
        search_box.send_keys(Keys.RETURN)

        # 4. Wait a little for results to load
        time.sleep(2)

    finally:
        # 7. Close the browser
        driver.quit()
