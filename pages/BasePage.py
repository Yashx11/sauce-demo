from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.driver.implicitly_wait(5)

    def click_on_element(self, xpath):
        element = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, xpath)))
        element.click()

    def enter_value_in_input(self, xpath, value):
        element = WebDriverWait(self.driver,10).until(EC.element_to_be_clickable((By.XPATH, xpath)))
        element.clear()
        element.send_keys(value)

    def verify_task(self, xpath):
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, xpath)))
        assert element.is_displayed()

    def get_attribute_type(self, xpath):
        element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, xpath)))
        field_type = element.get_attribute("type")
        return field_type

    def sort_products(self, xpath, value):
        select = Select(self.driver.find_element(By.XPATH, xpath))
        option = select.select_by_value(value)

    def verify_price_sorting(self, xpath, expected_order):
        price_elements = self.driver.find_elements(By.XPATH, xpath)
        prices = [float(price.text.replace("$", "")) for price in price_elements]

        sorted_prices = sorted(prices)
        if expected_order == "desc":
            sorted_prices = sorted_prices[::-1]

        return prices == sorted_prices

    def verify_name_sorting(self, xpath, expected_order):
        name_elements = self.driver.find_elements(By.XPATH, xpath)
        names = [name.text.strip().lower() for name in name_elements]

        sorted_names = sorted(names)
        if expected_order == "desc":
            sorted_names = sorted_names[::-1]

        return names == sorted_names

    def get_element_text(self, xpath):
        element = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, xpath))
        )
        return element.text

    def get_element(self, xpath):
        element = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, xpath))
        )
        return element

    def get_element_count(self, xpath):
        elements = WebDriverWait(self.driver, 10).until(EC.visibility_of_all_elements_located((By.XPATH, xpath)))
        return len(elements)

    def get_multiple_elements(self, xpath):
        elements = WebDriverWait(self.driver, 10).until(EC.visibility_of_all_elements_located((By.XPATH, xpath)))
        return elements