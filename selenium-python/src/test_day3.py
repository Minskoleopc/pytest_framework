
import pytest
@pytest.mark.smoke
def test_smoke_case():
    assert 1+1 == 2

@pytest.mark.regression
def test_regression_case():
    assert "chinmay" in "chinmay deshpande"

@pytest.mark.smoke
@pytest.mark.regression
def test_regression_and_smoke_case():
    assert len([11,22,33]) == 3

@pytest.mark.skip(reason="This testcase is under development")
def test_skipped_case():
    assert False








