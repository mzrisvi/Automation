# This is a sample Selenium test script in Python
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Initialize the WebDriver
driver = webdriver.Chrome()
# Open a webpage
driver.get("https://www.google.com")

# Find an element by its name attribute and perform actions
search_box = driver.find_element(By.NAME, "q")
search_box.send_keys("Selenium WebDriver")
search_box.send_keys(Keys.RETURN)
# Wait for a few seconds to see the results
time.sleep(5)

# Close the browser
driver.quit()
