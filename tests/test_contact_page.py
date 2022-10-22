import unittest
from selenium import webdriver
import pages
from selenium.webdriver.firefox.options import Options


class TestColibriSoftwareContactMe(unittest.TestCase):

    def setUp(self):
        options = Options()
        options.binary_location = r'C:\Program Files\Mozilla Firefox\firefox.exe'
        gecko_driver_path = '../Drivers/geckodriver.exe'
        self.driver = webdriver.Firefox(executable_path=gecko_driver_path, options=options)
        self.driver.get("https://www.colibri-software.com")

    def test_submit_contact_me_form(self):
        """
        Tests "Contact me" form.
        Populates the fields, submits the forms and verifies the success message
        """

        # Load the main page. In this case the home page of colibri-software.com.
        contact_page = pages.ContactPage(self.driver)

        # Checks if the word "Contact" is in title
        assert contact_page.is_title_matches()

        # Populating the form
        contact_page.name_input = 'John Doe'
        contact_page.company_name_input = 'John Doe\'s paper company'
        contact_page.email_input = 'jdoe@gmail.com'
        contact_page.additional_info_input = 'I need a website to sell paper online'

        # Submitting the form
        contact_page.click_submit_form_button()

        # Verifies that success message is displayed
        assert contact_page.success_message_is_displayed()

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()
