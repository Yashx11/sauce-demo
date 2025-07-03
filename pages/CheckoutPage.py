from pages.BasePage import BasePage


class CheckoutPage(BasePage):
    check_out_confirmation_title_xpath = "//span[text()='Checkout: Your Information']"
    continue_shopping_button_xpath = "//button[@id='continue-shopping']"
    first_name_input_xpath = "//input[@data-test='firstName']"
    last_name_input_xpath = "//input[@data-test='lastName']"
    postal_code_input_xpath = "//input[@data-test='postalCode']"
    continue_button_xpath = "//input[@data-test='continue']"
    cancel_button_xpath = "//input[@data-test='cancel']"
    finish_button_xpath = "//input[@data-test='finish']"
    sub_total_amount_xpath = "//input[@data-test='subtotal-label']"
    total_amount_xpath = "//input[@data-test='total-label']"
    tax_xpath = "//input[@data-test='tax-label']"


