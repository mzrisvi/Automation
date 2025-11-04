import re
from playwright.sync_api import Page, expect

def test_google_title(page: Page):
    page.wait_for_timeout(2000)  # Wait for 2 seconds to ensure the page is fully loaded
    # Navigate to Google
    page.goto("https://www.google.com/ncr")
    try:
        page.get_by_role("button", name="Not Interested").click()
    except:
        pass  # If the button is not found, continue without failing the test
    
    page.get_by_role("combobox", name="Search").fill("Playwright Python")
    page.keyboard.press("Enter")
    
    expect(page).to_have_title(re.compile("Playwright", re.IGNORECASE))
    