from playwright.sync_api import sync_playwright

def test_api_header(playwright):
    request = playwright.request.new_context(
        extra_http_headers={
            "Accept": "application/json",
            "Authorization": "Bearer test_token_123",
            "X-Custom-Header": "value123"
        }
    )
    response = request.get("https://httpbin.org/headers")
    
    assert response.status == 200
    json_response = response.json()
    headers = json_response["headers"]
    print("JSON response :\n", headers)

    assert headers["Accept"] == "application/json"
    assert headers["Authorization"] == "Bearer test_token_123"
    assert headers["X-Custom-Header"] == "value123" 
    request.dispose()
    print("Test completed successfully.")
    