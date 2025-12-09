import requests

def test_validate_headers():
    url = "https://httpbin.org/headers"

    # Send request with custom headers
    headers = {
        "User-Agent": "TestAgent/1.0",
        "Accept": "application/json",
        "X-Test-Header": "abc123"
    }

    response = requests.get(url, headers=headers)

    # Status code check
    assert response.status_code == 200

    # Response must be JSON
    data = response.json()
    returned_headers = data.get("headers")

    # Validate that our headers returned correctly
    assert returned_headers["User-Agent"] == "TestAgent/1.0"
    assert returned_headers["Accept"] == "application/json"
    assert returned_headers["X-Test-Header"] == "abc123"
