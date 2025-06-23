from pages.BasePage import BasePage


class HomePage(BasePage):
    side_bar_xpath = "//button[text()='Open Menu']"
    logout_xpath = "//a[text()='Logout']"

