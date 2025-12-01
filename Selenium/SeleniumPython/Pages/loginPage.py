# This is Login Page Class
from selenium.webdriver.common.by import By


class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.usernmae_input = (By.ID, "uname")
        self.password_input = (By.ID, "pwd")
        self.login_button = (By.XPATH, "/html[1]/body[1]/div[3]/div[1]/fieldset[1]/form[1]/div[1]/input[3]")
    
    def open_Page(self, url):
        self.driver.get(url)
        
    def enter_username(self, username):
        self.driver.find_element(*self.usernmae_input).send_keys(username)

    def enter_password(self, password):
        self.driver.find_element(*self.password_input).send_keys(password)

    def click_login(self):
        self.driver.find_element(*self.login_button).click()
        
    def login(self, username, password):
        self.enter_username(username)
        self.enter_password(password)
        self.click_login()
        
# End of Login Page Class