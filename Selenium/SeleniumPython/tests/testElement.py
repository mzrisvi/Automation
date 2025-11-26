# This is Element locator test script in Python
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
# Initialize the WebDriver
driver = webdriver.Chrome()

# Open a webpage
driver.get("https://trytestingthis.netlify.app/")
# Find an element by its ID attribute
element = driver.find_element(By.ID, "fname").send_keys("Mohammad")
element = driver.find_element(By.ID, "lname").send_keys("Risvi")

# Wait for a few seconds to see the results
time.sleep(5)
driver.find_element(By.XPATH, "/html[1]/body[1]/div[3]/div[2]/form[1]/fieldset[1]/button[1]").click()

# Close the browser
driver.quit()