import pytest 

@pytest.mark.parametrize("username,password",[
    ("username1","pwd1"),
    ("username2","pwd2"),
    ("username3","pwd3"),
    ("username4","pwd4")
])
def test_login(username,password):
    print(f'{username}{password}')
    assert username != "" and password != ""


# def test_open_google(browser):
#     browser.get('https://www.google.com')
#     assert "Google" in browser.title
