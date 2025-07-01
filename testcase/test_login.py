import time

from pages.BasePage import BasePage
from pages.LoginPage import LoginPage
from utilities.readproperties import read_configurations

class TestLogin:
    base_url = read_configurations("Basic Info", "base_url")
    username = read_configurations("Basic Info", "username")
    password = read_configurations("Basic Info", "password")

    #Login with valid credentials
    def login(self, driver_setup):
        self.driver = driver_setup
        self.driver.get(self.base_url)
        self.driver.maximize_window()
        login_page = LoginPage(self.driver)
        login_page.login(self.username, self.password)
        base_page = BasePage(self.driver)
        base_page.verify_task(LoginPage.login_verification_mark_xpath)
        self.driver.close()

    #Login with locked out user
    def login_with_locker_user(self, driver_setup):
        self.driver = driver_setup
        self.driver.get(self.base_url)
        self.driver.maximize_window()
        login_page = LoginPage(self.driver)
        login_page.login("locked_out_user", self.password)
        base_page = BasePage(self.driver)
        base_page.verify_task(LoginPage.locked_user_message)
        self.driver.close()

    #Login with invalid username
    def login_with_invalid_user(self, driver_setup):
        self.driver = driver_setup
        self.driver.get(self.base_url)
        self.driver.maximize_window()
        login_page = LoginPage(self.driver)
        login_page.login("invalid_user", self.password)
        base_page = BasePage(self.driver)
        base_page.verify_task(LoginPage.invalid_user_message)
        self.driver.close()

    #Login with empty fields
    def login_with_empty_fields(self, driver_setup):
        self.driver = driver_setup
        self.driver.get(self.base_url)
        self.driver.maximize_window()
        login_page = LoginPage(self.driver)
        login_page.login("", "")
        base_page = BasePage(self.driver)
        base_page.verify_task(LoginPage.blank_details_message)
        self.driver.close()

    #Login with only username
    def login_with_username_only(self, driver_setup):
        self.driver = driver_setup
        self.driver.get(self.base_url)
        self.driver.maximize_window()
        login_page = LoginPage(self.driver)
        login_page.login(self.username, "")
        base_page = BasePage(self.driver)
        base_page.verify_task(LoginPage.username_only_xpath)
        self.driver.close()

    #Password field masked
    def password_should_masked(self, driver_setup):
        self.driver = driver_setup
        self.driver.get(self.base_url)
        self.driver.maximize_window()
        base_page = BasePage(self.driver)
        assert base_page.get_attribute_type(LoginPage.password_input_xpath) == "password"
        self.driver.close()

    #Login & Logout
    def login_and_logout(self, driver_setup):
        self.driver = driver_setup
        self.driver.get(self.base_url)
        self.driver.maximize_window()
        login_page = LoginPage(self.driver)
        login_page.login(self.username, self.password)
        time.sleep(2)
        login_page.logout()
        self.driver.close()
