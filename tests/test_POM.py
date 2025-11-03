import re
from playwright.sync_api import Page, expect
from pages.orange_login import LoginPage
from pages.orange_home import HomePage

def test_POM(page: Page) -> None:
    login_page = LoginPage(page)
    home_page = HomePage(page)
    
    page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    login_page.enter_username("admin")
    login_page.enter_password("admin123")
    login_page.click_login()