import json
import pytest

def read_json_data():
    with open("test_data.json") as f:
        data = json.load(f)
    return [(item["username"], item["password"]) for item in data]

@pytest.mark.parametrize("username, password", read_json_data())
def test_login_json(username, password):
    print(f"Testing login with {username} and {password}")
    assert username != "" and password != ""
