import time

from pages.CartPage import CartPage
from pages.CheckoutPage import CheckoutPage
from pages.LoginPage import LoginPage
from pages.HomePage import HomePage
from pages.BasePage import BasePage
from utilities.readproperties import read_configurations

class TestCheckout:
    base_url = read_configurations("Basic Info", "base_url")
    username = read_configurations("Basic Info", "username")
    password = read_configurations("Basic Info", "password")
    first_name = read_configurations("Checkout Info", "first_name")
    last_name = read_configurations("Checkout Info", "last_name")
    zip_code = read_configurations("Checkout Info", "zip_code")

    def login_instance(self, driver_setup):
        self.driver = driver_setup
        self.driver.get(self.base_url)
        self.driver.maximize_window()
        login_page = LoginPage(self.driver)
        login_page.login(self.username, self.password)
        return login_page

    def navigate_to_checkout_step_one(self, driver_setup):
        self.login_instance(driver_setup)
        cart_page = CartPage(driver_setup)
        cart_page.proceed_to_checkout_setp_one_page()
        base_page = BasePage(driver_setup)
        base_page.verify_task(CheckoutPage.check_out_confirmation_title_xpath)
        self.driver.close()

    def submit_checkout_with_valid_info(self, driver_setup):
        self.login_instance(driver_setup)
        base_page = BasePage(driver_setup)
        checkout_page = CheckoutPage(driver_setup)
        checkout_page.add_product_to_cart_and_fill_checkout_details(self.first_name, self.last_name, self.zip_code)
        base_page.click_on_element(checkout_page.continue_button_xpath)
        base_page.verify_task(checkout_page.check_out_page_step2_verification_xpath)
        self.driver.close()

    def submit_checkout_without_first_name(self, driver_setup):
        self.login_instance(driver_setup)
        base_page = BasePage(driver_setup)
        checkout_page = CheckoutPage(driver_setup)
        checkout_page.add_product_to_cart_and_fill_checkout_details("", self.last_name, self.zip_code)
        base_page.click_on_element(checkout_page.continue_button_xpath)
        base_page.verify_task(checkout_page.first_name_blank_error_message_xpath)
        self.driver.close()

    def submit_checkout_without_last_name(self, driver_setup):
        self.login_instance(driver_setup)
        base_page = BasePage(driver_setup)
        checkout_page = CheckoutPage(driver_setup)
        checkout_page.add_product_to_cart_and_fill_checkout_details(self.first_name, "", self.zip_code)
        base_page.click_on_element(checkout_page.continue_button_xpath)
        base_page.verify_task(checkout_page.last_name_blank_error_message_xpath)
        self.driver.close()

    def submit_checkout_without_zip_code(self, driver_setup):
        self.login_instance(driver_setup)
        base_page = BasePage(driver_setup)
        checkout_page = CheckoutPage(driver_setup)
        checkout_page.add_product_to_cart_and_fill_checkout_details(self.first_name, self.last_name, "")
        base_page.click_on_element(checkout_page.continue_button_xpath)
        base_page.verify_task(checkout_page.zip_code_blank_error_message_xpath)
        self.driver.close()

    def cancel_checkout(self, driver_setup):
        self.login_instance(driver_setup)
        base_page = BasePage(driver_setup)
        checkout_page = CheckoutPage(driver_setup)
        checkout_page.add_product_to_cart_and_fill_checkout_details(self.first_name, self.last_name, self.zip_code)
        base_page.click_on_element(checkout_page.cancel_button_xpath)
        base_page.verify_task(CartPage.cart_page_verification_xpath)
        self.driver.close()

    def checkout(self, driver_setup):
        self.login_instance(driver_setup)
        base_page = BasePage(driver_setup)
        home_page = HomePage(driver_setup)
        product_total_amount = base_page.get_final_order_value(home_page.products_price_card_xpath)
        checkout_page = CheckoutPage(driver_setup)
        checkout_page.add_product_to_cart_and_fill_checkout_details(self.first_name, self.last_name, self.zip_code)
        base_page.click_on_element(checkout_page.continue_button_xpath)
        base_page.scroll_page()
        checkout_page_item_total = float((base_page.get_element_text(checkout_page.item_total_xpath)).split('$')[1])
        estimated_product_tax = round((product_total_amount * 8 / 100 ),2)
        actual_checkout_tax = float((base_page.get_element_text(checkout_page.product_tax_xpath)).split('$')[1])
        estimated_grand_total = product_total_amount + estimated_product_tax
        actual_grand_total = checkout_page_item_total + actual_checkout_tax
        # actual_grand_total = 2
        assert estimated_grand_total == actual_grand_total
        base_page.click_on_element(checkout_page.finish_checkout_button_xpath)
        base_page.verify_task(checkout_page.checkout_successful_text_xpath)
        base_page.click_on_element(checkout_page.back_to_products_xpath)
        base_page.verify_task(home_page.home_page_confirmation_xpath)
        self.driver.close()