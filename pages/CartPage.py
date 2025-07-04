from pages.BasePage import BasePage
from pages.HomePage import HomePage


class CartPage(BasePage):

    checkout_button_xpath = "//button[@id='checkout']"
    first_product_name_xpath = "(//div[@class='inventory_item_name'])[1]"
    remove_product_button_xpath = "(//button[text()='Remove'])[1]"
    cart_page_verification_xpath = "//span[text()='Your Cart']"

    def proceed_to_checkout_setp_one_page(self):
        base_page = BasePage(self.driver)
        home_page = HomePage(self.driver)
        home_page.add_product_to_cart()
        base_page.click_on_element(HomePage.cart_page_xpath)
        base_page.click_on_element(CartPage.checkout_button_xpath)

