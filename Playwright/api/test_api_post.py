from playwright.sync_api import Playwright, sync_playwright

def test_api_post(playwright):
    request = playwright.request.new_context()
    response = request.post("https://api.restful-api.dev/objects", json = { "id": "7" })
                                
    assert response.status == 200
    json_response = response.json()
    print("JSON response :\n", json_response)
    
    request.dispose()
    print("Test completed successfully.")
