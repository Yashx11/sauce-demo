import time

from pages.BasePage import BasePage
from pages.LoginPage import LoginPage
from utilities.readproperties import read_configurations

class TestLogin:
    base_url = read_configurations("Basic Info", "base_url")
    username = read_configurations("Basic Info", "username")
    password = read_configurations("Basic Info", "password")

    def login_instance(self, driver_setup):
        self.driver = driver_setup
        self.driver.get(self.base_url)
        self.driver.maximize_window()
        login_page = LoginPage(self.driver)
        return login_page

    #Login with valid credentials
    def test_login(self, driver_setup):
        login_instance = self.login_instance(driver_setup)
        login_instance.login(self.username, self.password)
        base_page = BasePage(self.driver)
        base_page.verify_task(LoginPage.login_verification_mark_xpath)
        self.driver.close()

    #Login with locked out user
    def test_login_with_locker_user(self, driver_setup):
        login_instance = self.login_instance(driver_setup)
        login_instance.login("locked_out_user", self.password)
        base_page = BasePage(self.driver)
        base_page.verify_task(LoginPage.locked_user_message)
        self.driver.close()

    #Login with invalid username
    def test_login_with_invalid_user(self, driver_setup):
        login_instance = self.login_instance(driver_setup)
        login_instance.login("invalid_user", self.password)
        base_page = BasePage(self.driver)
        base_page.verify_task(LoginPage.invalid_user_message)
        self.driver.close()

    #Login with empty fields
    def test_login_with_empty_fields(self, driver_setup):
        login_instance = self.login_instance(driver_setup)
        login_instance.login("", "")
        base_page = BasePage(self.driver)
        base_page.verify_task(LoginPage.blank_details_message)
        self.driver.close()

    #Login with only username
    def test_login_with_username_only(self, driver_setup):
        login_instance = self.login_instance(driver_setup)
        login_instance.login(self.username, "")
        base_page = BasePage(self.driver)
        base_page.verify_task(LoginPage.username_only_xpath)
        self.driver.close()

    #Password field masked
    def test_password_should_masked(self, driver_setup):
        login_instance = self.login_instance(driver_setup)
        base_page = BasePage(self.driver)
        assert base_page.get_attribute_type(LoginPage.password_input_xpath) == "password"
        self.driver.close()

    #Login & Logout
    def test_login_and_logout(self, driver_setup):
        login_instance = self.login_instance(driver_setup)
        login_instance.login(self.username, self.password)
        time.sleep(2)
        login_instance.logout()
        self.driver.close()
