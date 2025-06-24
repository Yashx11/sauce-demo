from pages.BasePage import BasePage

class HomePage(BasePage):
    side_bar_xpath = "//button[text()='Open Menu']"
    logout_xpath = "//a[text()='Logout']"
    products_name_card_xpath = "//div[@class='inventory_item_description']/div[1]/a/div"
    products_price_card_xpath = "//div[@class='inventory_item_description']/div[2]/div"
    first_product_card_button_xpath = "(//div[@class='inventory_item_description'])[1]/div[2]/button"
    sorting_dropdown_xpath = "//select[@class='product_sort_container']"
    sorting_option_a_to_z_xpath = "//option[@value='az']"
    sorting_option_z_to_a_xpath = "//option[@value='za']"
    sorting_option_price_low_to_high_xpath = "//option[@value='lohi']"
    sorting_option_price_high_to_low_xpath = "//option[@value='hilo']"
    cart_page_xpath = "//a[@class='shopping_cart_link']"

    def add_product_to_cart(self):
        base_page = BasePage(self.driver)
        base_page.click_on_element(self.first_product_card_button_xpath)
        base_page.click_on_element(self.cart_page_xpath)

    def sort_products(self, sorting_type):
        base_page = BasePage(self.driver)
        base_page.click_on_element(self.sorting_dropdown_xpath)
        if sorting_type.lower == "a_to_z":
            base_page.click_on_element(self.sorting_option_a_to_z_xpath)
        elif sorting_type.lower == "z_to_z":
            base_page.click_on_element(self.sorting_option_z_to_a_xpath)
        elif sorting_type.lower == "low_to_high":
            base_page.click_on_element(self.sorting_option_price_low_to_high_xpath)
        elif sorting_type.lower == "high_to_low":
            base_page.click_on_element(self.sorting_option_price_high_to_low_xpath)
        else:
            return "Sorting Type Not Found"

    def remove_product_from_card(self):
        base_page = BasePage(self)
        if self.first_product_card_button_xpath.title() != "Remove":
            return "Product not added to cart Yet"
        else:
            base_page.click_on_element(self.first_product_card_button_xpath)