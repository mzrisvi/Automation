import re
from playwright.sync_api import Page, expect


def test_example(page: Page) -> None:
    page.goto("https://dxc.com/")
    expect(page.get_by_role("navigation", name="Primary")).to_be_visible()

    page.get_by_label("Primary").get_by_role("link", name="Contact Us").click()
    expect(page.get_by_role("navigation", name="Primary")).to_be_visible()

    page.get_by_role("link", name="DXC Technology | A leading").click()
