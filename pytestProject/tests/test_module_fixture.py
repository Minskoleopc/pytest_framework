import pytest

# Set up the WebDriver (e.g., Chrome)
def test_verify_title(browser3):
    actual = browser3.title
    assert actual == 'Google'
    

def test_verify_link(browser3):
    searchBox = browser3.find_element('name',"q")
    assert searchBox is not None
    
class TestGoogle2:
    def test_open_google(self,browser3):
        assert "Google" in browser3.title

    def test_search_box_exists(self,browser3):
        searchBox = browser3.find_element('name',"q")
        assert searchBox is not None




