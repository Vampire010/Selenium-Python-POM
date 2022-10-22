from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By

# browser exposes an executable file
# Through Selenium test we will invoke the executable file which will then #invoke actual browser
chrome_driver_path = '../Drivers/chromedriver.exe'
driver = webdriver.Chrome(executable_path=chrome_driver_path)

# to maximize the browser window
driver.maximize_window()

# get method to launch the URL
driver.get("https://www.google.com")
driver.find_element(By.NAME, 'q').send_keys("Selenium Python")
driver.find_element(By.NAME, 'btnK').submit()
sleep(5);

# to close the browser
driver.close()
