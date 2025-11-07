import pytest
from playwright.sync_api import Page, expect

from conftest import page

def get_csv_data(file_path: str):
    import csv
    data = []
    with open(file_path, newline='') as csvfile:
        reader = csv.reader(csvfile)
        next(reader)  # Skip header row
        for row in reader:
            data.append((row[0], row[1]))
    return data

@pytest.mark.parametrize(
    "username,password",
    get_csv_data("./tests/test_data.csv")
)

def get_json_data(file_path: str):
    import json
    data = []
    with open(file_path, "r") as jsonfile:
        json_data = json.load(jsonfile)
        for entry in json_data:
            data.append((entry["username"], entry["password"]))
        return data

@pytest.mark.parametrize(
    "username,password",
    get_json_data("./tests/test_jasondata.json")
)

def test_example(page: Page, username: str, password: str) -> None:
    page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    expect(page.get_by_role("img", name="company-branding")).to_be_visible()

    page.get_by_role("textbox", name="username").click()
    page.get_by_role("textbox", name="username").fill(username)
    page.get_by_role("textbox", name="username").press("Tab")
    page.get_by_role("textbox", name="password").fill(password)
    page.get_by_role("button", name="Login").click()

    expect(page.get_by_role("link", name="Dashboard")).to_be_visible()
    page.get_by_role("link", name="My Info").click()
    expect(page.get_by_role("link", name="My Info")).to_be_visible()