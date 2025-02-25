import csv
import pytest

def read_csv_data():
    with open("data.csv", newline='') as f:
        reader = csv.reader(f)
        next(reader)  # Skip header row
        return [tuple(row) for row in reader]

@pytest.mark.parametrize("username, password", read_csv_data())
def test_login_csv(username, password):
    print(f"Testing login with {username} and {password}")
    assert username != "" and password != ""
