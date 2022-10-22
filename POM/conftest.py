import time

import pytest
from selenium import webdriver

from POM import settings
from POM.pages.login_page import LoginPage
from selenium.webdriver.firefox.options import Options

# browser = "chrome"


driver = None


def pytest_addoption(parser):
    # parser.addoption("--browser", action="store", default="chrome")
    parser.addoption("--browser", action="store", default=settings.browser)
    parser.addoption("--env", action="store", default=settings.env)


@pytest.fixture
def getBrowser(request):
    _browser = request.config.getoption("--browser")
    return _browser


@pytest.fixture
def getDriver(request, getBrowser):
    global driver
    print("browser from getBrowser method - " + getBrowser)
    if getBrowser == "chrome":
        chrome_driver_path = r'C:\Users\giris\PycharmProjects\PythonProj-01\Drivers\chromedriver.exe'
        driver = webdriver.Chrome(executable_path = chrome_driver_path)
    elif getBrowser == "firefox":
        options = Options()
        options.binary_location = r'C:\Program Files\Mozilla Firefox\firefox.exe'
        gecko_driver_path = r'C:\Users\giris\PycharmProjects\PythonProj-01\Drivers\geckodriver.exe'
        driver = webdriver.Firefox(executable_path=gecko_driver_path, options=options)

    driver.get(settings.url)
    driver.implicitly_wait(20)
    request.cls.loginPage = LoginPage(driver)
    yield driver
    time.sleep(2)
    driver.quit()
