from playwright.sync_api import sync_playwright
from playwright.sync_api import expect
import re


def test_google_search(page):
    page.wait_for_timeout(1000)  # Wait for the page to load
    # Navigate to Google
    page.goto("https://www.google.com/ncr")

    try:
        page.get_by_role("button", name="I agree").click(timeout=5000)
    except:
        print("No consent button found or already accepted.")

    page.get_by_role("combobox", name="Search").fill("Playwright")
    page.keyboard.press("Enter")

    expect(page).to_have_title(re.compile("Playwright", re.IGNORECASE))
