import time
from pages.CartPage import CartPage
from pages.CheckoutPage import CheckoutPage
from pages.LoginPage import LoginPage
from pages.HomePage import HomePage
from pages.BasePage import BasePage
from utilities.readproperties import read_configurations


class TestCart:
    base_url = read_configurations("Basic Info", "base_url")
    username = read_configurations("Basic Info", "username")
    password = read_configurations("Basic Info", "password")

    def login_instance(self, driver_setup):
        self.driver = driver_setup
        self.driver.get(self.base_url)
        self.driver.maximize_window()
        login_page = LoginPage(self.driver)
        login_page.login(self.username, self.password)
        home_page = HomePage(self.driver)
        home_page.add_product_to_cart()

    def navigate_to_cart_page(self, driver_setup):
        self.login_instance(driver_setup)
        base_page = BasePage(self.driver)
        base_page.click_on_element(HomePage.cart_page_xpath)
        base_page.verify_task("//span[text()='Your Cart']")
        self.driver.close()

    def verify_product_details_in_cart(self, driver_setup):
        self.login_instance(driver_setup)
        base_page = BasePage(self.driver)
        base_page.click_on_element(HomePage.cart_page_xpath)
        cart_page = CartPage(self.driver)
        product_name = base_page.get_element_text(cart_page.first_product_name_xpath)
        # print("Product name in cart:", product_name)
        assert product_name == "Sauce Labs Backpack"
        self.driver.close()

    def remove_product_from_cart(self, driver_setup):
        self.login_instance(driver_setup)
        base_page = BasePage(self.driver)
        base_page.click_on_element(HomePage.cart_page_xpath)
        base_page.click_on_element(CartPage.remove_product_button_xpath)
        base_page.click_on_element(HomePage.side_bar_xpath)
        base_page.click_on_element(HomePage.all_items_sidebar_menu_xpath)
        self.driver.close()

    def click_checkout(self, driver_setup):
        self.login_instance(driver_setup)
        base_page = BasePage(self.driver)
        base_page.click_on_element(CartPage.checkout_button_xpath)
        element = base_page.get_element(CheckoutPage.check_out_confirmation_title_xpath)
        assert element.is_displayed()
        self.driver.close()

    def back_to_inventory(self, driver_setup):
        self.login_instance(driver_setup)
        base_page = BasePage(self.driver)
        base_page.click_on_element(CheckoutPage.continue_shopping_button_xpath)
        assert base_page.get_element(HomePage.home_page_confirmation_xpath).is_displayed()
        self.driver.close()