from pages.BasePage import BasePage
from pages.CartPage import CartPage
from pages.HomePage import HomePage


class CheckoutPage(BasePage):
    check_out_confirmation_title_xpath = "//span[text()='Checkout: Your Information']"
    continue_shopping_button_xpath = "//button[@id='continue-shopping']"
    first_name_input_xpath = "//input[@data-test='firstName']"
    last_name_input_xpath = "//input[@data-test='lastName']"
    zip_code_input_xpath = "//input[@data-test='postalCode']"
    continue_button_xpath = "//input[@data-test='continue']"
    cancel_button_xpath = "//button[@data-test='cancel']"
    finish_button_xpath = "//input[@data-test='finish']"
    sub_total_amount_xpath = "//input[@data-test='subtotal-label']"
    total_amount_xpath = "//input[@data-test='total-label']"
    tax_xpath = "//input[@data-test='tax-label']"
    check_out_page_step2_verification_xpath = "//span[text()='Checkout: Overview']"
    first_name_blank_error_message_xpath = "//h3[text()='Error: First Name is required']"
    last_name_blank_error_message_xpath = "//h3[text()='Error: Last Name is required']"
    zip_code_blank_error_message_xpath = "//h3[text()='Error: Postal Code is required']"
    item_total_xpath = "//div[@class='summary_subtotal_label']"


    def add_product_to_cart_and_fill_checkout_details(self, first_name, last_name, zip_code):
        base_page = BasePage(self.driver)
        home_page = HomePage(self.driver)
        home_page.add_multiple_products_in_cart()
        base_page.click_on_element(CartPage.checkout_button_xpath)
        base_page.enter_value_in_input(self.first_name_input_xpath, first_name)
        base_page.enter_value_in_input(self.last_name_input_xpath, last_name)
        base_page.enter_value_in_input(self.zip_code_input_xpath, zip_code)




