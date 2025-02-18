import pytest

class TestGoogleSearch:

    def test_open_google(self,browser2):
        browser2.get("https://www.google.com")
        assert "Google" in browser2.title

    def test_search_box_exists(self,browser2):
        searchBox = browser2.find_element('name',"q")
        assert searchBox is not None

