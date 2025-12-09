# This is a sample test script using Playwright to perform an API GET request
import pytest

@pytest.fixture(scope="session")
def api_context(playwright):
    context = playwright.request.new_context(ignore_https_errors=True)
    yield context
    context.dispose()

def test_api_get(api_context):
        response = api_context.get("https://jsonplaceholder.typicode.com/posts/1")

        assert response.status == 200
        json_response = response.json()
        print("Json Response is :\n",json_response)
        assert json_response["id"] == 1

        print("API GET request test completed successfully.")