import re
from playwright.sync_api import Page, expect


def test_example(page: Page) -> None:
    page.goto("https://www.orangehrm.com/")
    expect(page.get_by_role("dialog", name="This website uses cookies")).to_be_visible()

    page.get_by_role("link", name="Solutions", exact=True).click()
    page.get_by_role("link", name="Starter (Open Source)").click()
    expect(page.get_by_role("dialog", name="This website uses cookies")).to_be_visible()

    page.locator("#navbarNav").get_by_role("button", name="Contact Sales").click()
