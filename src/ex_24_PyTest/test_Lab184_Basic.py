import pytest
@pytest.mark.smoke
def test_method1():
    print("Hello World")
    assert 5 == 6

@pytest.mark.smoke
def test_method2():
    print("Hello World")
    assert 5 == 5