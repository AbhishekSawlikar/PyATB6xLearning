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
    __password = "12345"


    def run_test(self):
        print(f"Running login test with user: {self.__username}")


    def get_user(self):
        print(f"username: {self.__username}")
        print(f"password: {self.__password}")


login = LoginTest()
login.setup()
login.run_test()
login.teardown()