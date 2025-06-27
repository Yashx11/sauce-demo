import pytest
from selenium import webdriver
from utilities.readproperties import read_configurations
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

browser = read_configurations("Basic Info", "browser")

@pytest.fixture()
def driver_setup():

    #Disable the Browser alert for the change password
    prefs = {
        "credentials_enable_service": False,
        "profile.password_manager_enabled": False
    }
    options = Options()
    options.add_argument("--incognito")
    options.add_argument("--disable-infobars")
    options.add_argument("--disable-notifications")
    options.add_experimental_option("prefs", prefs)

    if browser.lower() == "chrome":
        driver = webdriver.Chrome(service=Service(), options=options)
    elif browser.lower() == "firefox":
        driver = webdriver.Firefox(service=Service(), options=options)
    elif browser.lower() == "edge":
        driver = webdriver.Edge(service=Service(), options=options)
    else:
        return "Driver not Found"

    driver.maximize_window()
    return driver