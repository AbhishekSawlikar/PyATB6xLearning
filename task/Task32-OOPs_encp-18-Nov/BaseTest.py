# Build a Test Framework with Encapsulation + Inheritance
#
# 🎯 Goal:
#
# Create a simple automation structure that uses:
#
# A BaseTest class for setup/teardown (Parent class)
#
# A LoginTest class that inherits BaseTest (Child class)
#
# Encapsulate sensitive data (like credentials) as private variables
#
#
# ✅ Requirements:
#
# Create a BaseTest class:
#
# Has a protected variable _driver = "Chrome".
#
# Method setup() prints "Launching browser: Chrome".
#
# Method teardown() prints "Closing browser".
#
# Create a LoginTest class that inherits BaseTest:
#
# Has private variables for username and password.
#
# Method run_test() that prints:
#
# "Running login test with user: <username>".
#
# Use encapsulation: access private vars only through a method (e.g., get_user()).
#
# Create an object of LoginTest and call:
#
# setup()
#
# run_test()
#
# teardown()"""
#
# Launching browser: Chrome
#
# Running login test with user: admin
#
# Closing browser

class BaseTest:
    # def __init__(self):
    _driver = "Chrome"


    def setup(self):
        print(f"Launching browser : {self._driver}")


    def teardown(self):
        print("Closing browser")


class LoginTest(BaseTest):
    # def __init__(self):
    __username = "Admin"
    __password = "Password@1"


    def run_test(self):
        print(f"Running login test with user: {self.__username}")


    def get_user(self):
        print(f"username: {self.__username}")
        print(f"password: {self.__password}")


login = LoginTest()
login.setup()
login.run_test()
login.teardown()