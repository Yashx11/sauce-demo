from pages.BasePage import BasePage
from pages.HomePage import HomePage


class LoginPage(BasePage):

    username_input_xpath = "//input[@id='user-name']"
    password_input_xpath = "//input[@id='password']"
    login_button_xpath = "//input[@id='login-button']"
    login_verification_mark_xpath = "//div[text()='Swag Labs']"
    locked_user_message = "//h3[text()='Epic sadface: Sorry, this user has been locked out.']"
    invalid_user_message = "//h3[text()='Epic sadface: Username and password do not match any user in this service']"
    blank_details_message = "//h3[text()='Epic sadface: Username is required']"
    username_only_xpath = "//h3[text()='Epic sadface: Password is required']"


    def login(self, username, password):
        base_page = BasePage(self.driver)
        base_page.enter_value_in_input(self.username_input_xpath, username)
        base_page.enter_value_in_input(self.password_input_xpath, password)
        base_page.click_on_element(self.login_button_xpath)

    def logout(self):
        base_page = BasePage(self.driver)
        base_page.click_on_element(HomePage.side_bar_xpath)
        base_page.click_on_element(HomePage.logout_xpath)
