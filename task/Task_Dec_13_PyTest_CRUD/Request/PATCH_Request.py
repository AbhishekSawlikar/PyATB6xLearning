from http.cookiejar import Cookie

import pytest
import allure
import requests


def test_create_token():
    base_url = "https://restful-booker.herokuapp.com"
    headers = {"Content-Type": "application/json"}
    base_path = "/auth"
    full_url = base_url + base_path
    json_payload_auth = {
        "username": "admin",
        "password": "password123"
    }
    response_data = requests.post(url=full_url, headers=headers, json=json_payload_auth)
    print(response_data)

    assert response_data.status_code == 200
    response_data_json = response_data.json()
    token = response_data_json["token"]
    print("Token ID: ",token)
    assert type(token) == str
    assert len(token) > 0
    return token

@allure.title("(POST)Get Booking ID")
@allure.description("Get Booking id for update")
@pytest.mark.getbooking
def test_create_and_get_bookingid():
    base_url="https://restful-booker.herokuapp.com"
    path_url="/booking"
    full_url = base_url + path_url

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

    response_data=requests.post(url=full_url,headers=headers,json=payload)
    response_data_json = response_data.json()
    bookingId = response_data_json["bookingid"]
    print("Booking Id: ",bookingId)
    return bookingId

@allure.title("(PATCH) Update Booking Details")
@allure.description("Some of the details update of booking")
@pytest.mark.getbooking
def test_patch_booking():
    token1 = test_create_token()
    booking_id= test_create_and_get_bookingid()
    base_url="https://restful-booker.herokuapp.com"
    path_url="/booking/" + str(booking_id)
    full_url = base_url + path_url
    cookie = 'token=' + token1
    print("Booking Id to Update: ",booking_id)

    headers = {
        "content-type": "application/json",
        "Cookie": cookie
    }

    payload = {
        "firstname": "John",
        "lastname": "Mackwan",
        "totalprice": 111,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2025-12-05",
            "checkout": "2025-12-05"
        },
        "additionalneeds": "Breakfast and Dinner"
    }

    response_data=requests.patch(url=full_url,headers=headers,json=payload)
    response_data_json = response_data.json()

    assert  response_data.status_code == 200
    assert  response_data_json["totalprice"] == 111
    assert  response_data_json["bookingdates"]["checkin"] == "2025-12-05"
    assert  response_data_json["bookingdates"]["checkout"] == "2025-12-05"

    print(payload)