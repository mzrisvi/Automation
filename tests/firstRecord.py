import re
from playwright.sync_api import Page, expect


def test_record(page: Page) -> None:
    page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    page.get_by_role("textbox", name="Username").click()
    page.get_by_role("textbox", name="Username").fill("admin")
    page.get_by_role("textbox", name="Username").press("Tab")
    page.get_by_role("textbox", name="Password").fill("admin123")
    page.get_by_role("button", name="Login").click()
    page.get_by_role("listitem").filter(has_text="Hello Div").locator("i").click()
    page.get_by_role("menuitem", name="Logout").click()
    page.get_by_role("textbox", name="Username").click()
