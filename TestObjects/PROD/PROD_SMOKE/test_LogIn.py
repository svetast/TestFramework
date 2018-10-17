import time

import pytest

from HelperTestBase import HelperTestBase
from PageObjects.LoginPage import LoginPage
from PageObjects.HomePage import HomePage
from PageObjects.ForgotPasswordPage import ForgotPasswordPage


class TestLogin(LoginPage):

    @pytest.mark.order1
    def test_loginSuccess_LogOut(self):
        driver = self.driver
        driver.get(self.base_url + '/Account/Login')

        LoginPage.logIn(self, "svetast555", "Ss123456")

        #### Check that user stay login after page refreshed:  #####
        self.driver.refresh()
        self.assertIs(True, HomePage.checkLogOutLink(self))
        HomePage.logOut(self)
        time.sleep(5)
        self.assertIs(LoginPage.checkLoginForm(self), True)
