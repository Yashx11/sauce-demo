import pytest
import os
import allure
import pytest
from datetime import datetime
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

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """Hook to capture screenshot on test failure and attach to Allure"""
    outcome = yield
    rep = outcome.get_result()

    if rep.when == "call" and rep.failed:
        driver = item.funcargs.get("driver_setup", None)

        if driver:
            # Create the screenshots directory
            screenshots_dir = os.path.join(os.getcwd(), "screenshots")
            os.makedirs(screenshots_dir, exist_ok=True)

            # Create a timestamped file name
            timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
            # file_name = f"{item.name}_{timestamp}.png"
            case_id = item.get_closest_marker("testcase_id")
            case_name = case_id.args[0] if case_id else item.name
            file_name = f"{case_name}_{timestamp}.png"
            file_path = os.path.join(screenshots_dir, file_name)

            # Save screenshot to file
            driver.save_screenshot(file_path)

            # Attach screenshot to Allure report
            with open(file_path, "rb") as image_file:
                allure.attach(image_file.read(), name="Failure Screenshot", attachment_type=allure.attachment_type.PNG)