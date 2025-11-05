from playwright.sync_api import Page

class LoginPage:
    def __init__(self, page: Page):
        self.page = page
        self.username_field = page.get_by_role("textbox", name="Username")
        self.password_field = page.get_by_role("textbox", name="Password")
        self.login_button = page.get_by_role("button", name="Login")

    def enter_username(self, username):
        username_field = self.username_field
        username_field.clear()
        username_field.fill(username)
        
    def enter_password(self, password):
        password_field = self.password_field
        password_field.clear()
        password_field.fill(password)

    def click_login(self):
        login_button = self.login_button
        login_button.click()
        
    def login(self, username, password):
        self.enter_username(username)
        self.enter_password(password)
        self.click_login()