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

    def remove_product_from_card(self):
        base_page = BasePage(self.driver)
        base_page.click_on_element(self.first_product_card_button_xpath)
        base_page.click_on_element(self.first_product_card_button_xpath)

    def sort(self, sorting_type):
        base_page = BasePage(self.driver)
        if sorting_type == "a_to_z":
            base_page.sort_products(self.sorting_dropdown_xpath, "az")
            base_page.verify_name_sorting(self.products_name_card_xpath, "asc")
        elif sorting_type == "z_to_a":
            base_page.sort_products(self.sorting_dropdown_xpath, "za")
            base_page.verify_name_sorting(self.products_name_card_xpath, "desc")
        elif sorting_type == "low_to_high":
            base_page.sort_products(self.sorting_dropdown_xpath, "lohi")
            assert base_page.verify_price_sorting(self.products_price_card_xpath, "asc")
        elif sorting_type == "high_to_low":
            base_page.sort_products(self.sorting_dropdown_xpath, "hilo")
            assert base_page.verify_price_sorting(self.products_price_card_xpath, "desc")
        else:
            raise ValueError("Type not found")