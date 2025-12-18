import pytest
import allure
import requests

@allure.title("TC1 - Create Booking CRUD Positive")
@allure.description("Verify the create Booking!")
@pytest.mark.crud
def test_create_booking_positive_tc1():
    base_url = "https://restful-booker.herokuapp.com"
    base_path = "/booking"
    full_url = base_url + base_path


    headers = {
        "content-type": "application/json"
    }

    payload = {
        "firstname": "Jim",
        "lastname": "Brown",
        "totalprice": 111,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2018-01-01",
            "checkout": "2019-01-01"
        },
        "additionalneeds": "Breakfast"
    }
    response_data = requests.post(url=full_url, headers=headers, json=payload)
    print(response_data.text)
    assert response_data.status_code == 200