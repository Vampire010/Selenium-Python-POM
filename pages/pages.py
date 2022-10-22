from elements import BasePageElement
from locators import ContactPageLocators

class NameElement(BasePageElement):
    """
    This class gets the search text from the specified locator
    """

    # The locator for text box where name is entered
    locator = 'wpforms-236-field_0'

# Similar classes for other text fields
class CompanyNameElement(BasePageElement):

    locator = 'wpforms-236-field_4'

class EmailElement(BasePageElement):

    locator = 'wpforms-236-field_1'

class AdditionalInfoElement(BasePageElement):

    locator = 'wpforms-236-field_0'

class BasePage(object):
    """
    Base class to initialize the base page that will be called from all pages
    """

    def __init__(self, driver):
        self.driver = driver

class ContactPage(BasePage):
    """
    Contact page action methods come here
    """

    # Declares text input fields
    name_input = NameElement()
    company_name_input = CompanyNameElement()
    email_input = EmailElement()
    additional_info_input = AdditionalInfoElement()

    def is_title_matches(self):
        """
        Verifies that the text "Contact" appears in page title
        """
        return 'Contact' in self.driver.title

    def click_submit_form_button(self):
        """
        Submits the form
        """
        element = self.driver.find_element(*ContactPageLocators.SUBMIT_FORM_BUTTON)
        element.click()

    def success_message_is_displayed(self):
        success_message = 'Thanks for contacting us! We will be in touch with you shortly.'
        return success_message in self.driver.page_source