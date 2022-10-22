from selenium.webdriver.common.by import By

from POM.pages.base_page import BasePage


class LoginPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    username = (By.NAME, "username")
    password = (By.NAME, "password")
    loginButton = (By.XPATH, "//*[@id='loginPanel']/form/div[3]/input")

    def login(self, username, password):
        self.send_keys(self.username, username)
        self.send_keys(self.password, password)
        self.click(self.loginButton)

