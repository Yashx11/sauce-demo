import pytest
from selenium import webdriver
from utilities.readproperties import read_configurations
from selenium.webdriver.chrome.options import Options

browser = read_configurations("Basic Info", "browser")


@pytest.fixture()
def driver_setup():
    options = Options()
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--headless")  # If running in CI/CD
    options.add_argument("--disable-gpu")

    if browser.lower() == "chrome":
        driver = webdriver.Chrome()
    elif browser.lower() == "firefox":
        driver = webdriver.Firefox()
    elif browser.lower() == "edge":
        driver = webdriver.Edge()
    else:
        return "Driver not Found"
    driver.maximize_window()
    return driver