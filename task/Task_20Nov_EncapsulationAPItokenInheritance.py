"""
🎯 Goal:
Simulate a secure API testing structure where:
The BaseAPI class holds an encapsulated token (private).
The UserAPI class inherits from BaseAPI and uses that token to call a fake endpoint.

✅ Requirements:
Create a BaseAPI class:
Private variable __token = "ABC123SECRET".
Protected method gettoken() returns this token safely.
Create a UserAPI class that inherits BaseAPI:
Method get_user_data() prints:
"Fetching user data using token: <token>".
"""


class BaseAPI:
    _token = "ABC123SECRET"

    def get_token(self):
        return self._token
class UserAPI(BaseAPI):

    def get_user_data(self):
        token=self._token
        print("Fetching user data using token: " ,token)
        return token

obj = UserAPI()
obj.get_user_data()