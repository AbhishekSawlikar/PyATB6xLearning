# pytest assert
import pytest

@pytest.mark.smoke
def test_method1():
    print("Positive case")
    assert 5 == 5

@pytest.mark.smoke
def test_method2():
    print("Negative case")
    assert 5 == 6