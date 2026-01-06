import requests

def test_get_users_api():
    response = requests.get("https://www.flipkart.com/")

    assert response.status_code == 200
    assert response.json()["data"]["id"] == 2
