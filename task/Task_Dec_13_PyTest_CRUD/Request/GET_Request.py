import pytest
import allure
import requests

@allure.title("TC1 - Verify the Get request")
@allure.description("Verify the GET request is basically give 200 status code id OK")
@pytest.mark.positive
def test_get_request():
    url = "https://restful-booker.herokuapp.com/booking/1"
    response_data = requests.get(url=url)
    assert response_data.status_code == 200

@allure.title("TC2 - Verify the GET Request of Restful Booker with invalid ID")
@allure.description("This Testcase check Booking -1 and verify the response")
@pytest.mark.negative
def test_get_request_negative():
    url = "https://restful-booker.herokuapp.com/booking/1"
    response_data = requests.get(url=url)
    assert response_data.status_code == 404