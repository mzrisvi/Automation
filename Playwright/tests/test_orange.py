import re
from playwright.sync_api import Page, expect
from pages.orangehome_page import HomePage
from pages.orangelogin_page import LoginPage

def test_example(page: Page) -> None:
    login_page = LoginPage(page)
    home_page = HomePage(page)
    
    page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    login_page.login("Admin", "admin123")
    home_page.is_upgrade_button_visible()
    
    home_page.is_performance_button_visible
    home_page.click_performance()
    
    home_page.is_dashboard_button_visible()
    home_page.click_dashboard()
    