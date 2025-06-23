from selenium.webdriver.common.by import By
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