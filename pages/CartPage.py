from pages.BasePage import BasePage

class CartPage(BasePage):

    checkout_button_xpath = "//button[@id='checkout']"
    first_product_name_xpath = "(//div[@class='inventory_item_name'])[1]"
    remove_product_button_xpath = "(//button[text()='Remove'])[1]"

    def checkout(self):
        pass
