import time
from pages.HomePage import HomePage
from pages.LoginPage import LoginPage
from utilities.readproperties import read_configurations


class TestHome:
    base_url = read_configurations("Basic Info", "base_url")
    username = read_configurations("Basic Info", "username")
    password = read_configurations("Basic Info", "password")

    # Verify product list is displayed
    def is_all_products_are_displayed(self, driver_setup):
        pass

    # Sort products A to Z
    def test_sorting_the_products_a_to_z(self, driver_setup):
        self.driver = driver_setup
        self.driver.get(self.base_url)
        self.driver.maximize_window()
        login_page = LoginPage(self.driver)
        login_page.login(self.username, self.password)
        home_page = HomePage(self.driver)
        home_page.sort("a_to_z")
        time.sleep(3)
        self.driver.close()

    # Sort products Z to A
    def test_sorting_the_products_z_to_a(self, driver_setup):
        self.driver = driver_setup
        self.driver.get(self.base_url)
        self.driver.maximize_window()
        login_page = LoginPage(self.driver)
        login_page.login(self.username, self.password)
        home_page = HomePage(self.driver)
        home_page.sort("z_to_a")
        time.sleep(5)
        self.driver.close()

    # Sort products low to high
    def test_sorting_the_products_low_to_height(self, driver_setup):
        self.driver = driver_setup
        self.driver.get(self.base_url)
        self.driver.maximize_window()
        login_page = LoginPage(self.driver)
        login_page.login(self.username, self.password)
        home_page = HomePage(self.driver)
        home_page.sort("low_to_high")
        time.sleep(5)
        self.driver.close()

    # Sort products high to low
    def test_sorting_the_products_high_to_low(self, driver_setup):
        self.driver = driver_setup
        self.driver.get(self.base_url)
        self.driver.maximize_window()
        login_page = LoginPage(self.driver)
        login_page.login(self.username, self.password)
        home_page = HomePage(self.driver)
        home_page.sort("high_to_low")
        time.sleep(5)
        self.driver.close()

    # Add product to cart
    def test_add_product_to_cart(self, driver_setup):
        self.driver = driver_setup
        self.driver.get(self.base_url)
        self.driver.maximize_window()
        login_page = LoginPage(self.driver)
        login_page.login(self.username, self.password)
        home_page = HomePage(self.driver)
        home_page.add_product_to_cart()
        self.driver.close()

    # Remove product from cart
    def test_remove_product_from_cart(self, driver_setup):
        self.driver = driver_setup
        self.driver.get(self.base_url)
        self.driver.maximize_window()
        login_page = LoginPage(self.driver)
        login_page.login(self.username, self.password)
        home_page = HomePage(self.driver)
        home_page.remove_product_from_card()
        self.driver.close()