import parser

import pytest
from selenium import webdriver


def pytest_addoption(parser):
    parser.addoption("--browser_name", action="store", default="chrome", help="Browser option selection")


@pytest.fixture(scope="function")
def driver_instance(request):
    browser_name = request.config.getoption("browser_name")
    if browser_name == "chrome":
        chrome_options = webdriver.ChromeOptions()
        # chrome_options.add_argument("--headless")
        chrome_options.add_argument("--incognito")
        driver = webdriver.Chrome(options=chrome_options)
        driver.maximize_window()

        driver.implicitly_wait(5)
    elif browser_name == "firefox":
        driver = webdriver.Firefox()

    yield driver
    driver.close()
