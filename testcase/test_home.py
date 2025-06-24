from pluggy import HookRelay

from pages.HomePage import HomePage
from utilities.readproperties import read_configurations


class TestHome:
    base_url = read_configurations("Basic Info", "base_url")
    username = read_configurations("Basic Info", "username")
    password = read_configurations("Basic Info", "password")

    # Verify product list is displayed
    def test_is_all_products_are_displayed(self, driver_setup):
        pass

    # Sort products A to Z
    def test_sorting_the_products_a_to_z(self, driver_setup):
        pass

    # Sort products Z to A
    def test_sorting_the_products_z_to_a(self, driver_setup):
            pass

    # Sort products low to high
    def test_sorting_the_products_low_to_height(self, driver_setup):
        pass

    # Sort products high to low
    def test_sorting_the_products_high_to_low(self, driver_setup):
        pass

    # Add product to cart
    def test_add_product_to_cart(self, driver_setup):
        pass

    # Remove product from cart
    def test_remove_product_from_cart(self, driver_setup):
        pass