import requests

def test_greet_post():
    url = 'http://127.0.0.1:5000/greet'
    data = {'name': 'TestUser'}
    response = requests.post(url, data=data)
    assert response.status_code == 200
    assert 'Hello, TestUser!' in response.text