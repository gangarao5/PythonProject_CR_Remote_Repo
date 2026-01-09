import requests

def test_get_users_api():
    response = requests.get("https://www.flipkart.com/")
    # response = requests.get("https://reqres.in/api/users?page=2")

    assert response.status_code == 529

