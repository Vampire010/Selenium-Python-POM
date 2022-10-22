from POM import settings
from POM.tests.base_test import BaseTest


class TestLogin(BaseTest):

    def test_valid_login(self):
        # launch url
        self.loginPage.login(settings.username, settings.password)
