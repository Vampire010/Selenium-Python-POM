from selenium.webdriver.common.by import By

class ContactPageLocators(object):
    """
    A class for all Contact page locators.
    """
    SUBMIT_FORM_BUTTON = (By.CSS_SELECTOR, 'button[type="submit"]')