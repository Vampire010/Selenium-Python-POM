from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options

# browser exposes an executable file
options = Options()
options.binary_location = r'C:\Program Files\Mozilla Firefox\firefox.exe'
gecko_driver_path = '../Drivers/geckodriver.exe'
driver = webdriver.Firefox(executable_path=gecko_driver_path, options=options)

# to maximize the browser window
driver.maximize_window()

# get method to launch the URL
driver.get("https://www.google.com")
driver.find_element(By.NAME, 'q').send_keys("Selenium Python")
driver.find_element(By.NAME, 'btnK').submit()

sleep(5);
# to close the browser
driver.close()
