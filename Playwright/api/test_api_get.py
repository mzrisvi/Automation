def test_api_get(playwright):
        request = playwright.request.new_context()
        response = request.get("https://jsonplaceholder.typicode.com/posts/1")

        assert response.status == 200
        json_response = response.json()
        print("Json Response is :\n",json_response)
        assert json_response["id"] == 1

        request.dispose()
        print("API GET request test completed successfully.")