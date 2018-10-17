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

    @pytest.mark.order2
    def test_loginUnSuccess1(self):
        # password is wrong:
        driver = self.driver
        driver.get(self.base_url + '/Account/Login')

        LoginPage.logInUnSuccess(self, "svetast723", "Ss12345561119")
        self.assertIs(LoginPage.checkLoginForm(self), True)

    @pytest.mark.order3
    def test_checkSubmitForgotPasswordFormValidation(self):
        driver = self.driver
        driver.get(self.base_url + '/Account/Login')
        text = 'Reset your password.'
        text1 = 'Account information is incorrect'
        text3 = 'Please enter your username.'
        text4 = 'Please enter your email.'

        text5 = "The username and email address you entered don’t match our records"

        time.sleep(5)

        LoginPage.clickForgotPasswordLink(self)
        time.sleep(2)
        self.assertIn(text, self.driver.page_source)

        ForgotPasswordPage.fillForgotPasswordForm(self,
                                                  userName="svetast#123",
                                                  email="svetatestbox@gmail.com",
                                                  )
        time.sleep(3)
        self.assertIn(text1, self.driver.page_source)
        self.driver.refresh()
        time.sleep(2)

        LoginPage.clickForgotPasswordLink(self)
        ForgotPasswordPage.fillForgotPasswordForm(self,
                                                  userName="1",
                                                  email="svetatestbox@gmail.com",
                                                  )
        time.sleep(5)
        self.assertIn(text5, self.driver.page_source)
        self.driver.refresh()
        time.sleep(2)

        LoginPage.clickForgotPasswordLink(self)
        ForgotPasswordPage.fillForgotPasswordForm(self,
                                                  userName="",
                                                  email="",
                                                  )
        time.sleep(3)
        self.assertIn(text3, self.driver.page_source)
        self.assertIn(text4, self.driver.page_source)

        self.driver.refresh()
        time.sleep(2)

        LoginPage.clickForgotPasswordLink(self)
        ForgotPasswordPage.fillForgotPasswordForm(self,
                                                  userName="svetast22",
                                                  email="",
                                                  )
        time.sleep(3)
        self.assertIn(text4, self.driver.page_source)

        self.driver.refresh()
        time.sleep(2)

        LoginPage.clickForgotPasswordLink(self)
        ForgotPasswordPage.fillForgotPasswordForm(self,
                                                  userName="",
                                                  email="svetatestbox@gmail.com",
                                                  )
        time.sleep(3)
        self.assertIn(text3, self.driver.page_source)

        self.driver.refresh()
        time.sleep(2)

        LoginPage.clickForgotPasswordLink(self)
        ForgotPasswordPage.fillForgotPasswordForm(self,
                                                  userName="svetatestbox@gmail.com",
                                                  email="svetast999",
                                                  )
        time.sleep(3)
        self.assertIn(text5, self.driver.page_source)

    # @pytest.mark.skip
    @pytest.mark.order4
    def test_checkSubmitForgotUsernameFormValidation(self):
        driver = self.driver
        driver.get(self.base_url + '/Account/Login')
        text = 'Account information is incorrect'
        text1 = 'Please enter correct ZIP'
        text2 = 'Please enter your zip code.'
        text3 = 'Please enter your email.'
        text4 = 'Account information is incorrect'

        time.sleep(5)
        LoginPage.clickForgotUsernameLink(self)
        ForgotPasswordPage.fillForgotUserNameForm(self,
                                                  zip="",
                                                  email="")

        self.assertIn(text2, self.driver.page_source)
        self.assertIn(text3, self.driver.page_source)
        self.driver.refresh()

        LoginPage.clickForgotUsernameLink(self)
        ForgotPasswordPage.fillForgotUserNameForm(self,
                                                  zip="",
                                                  email="svetatestbox@gmail.com")

        self.assertIn(text2, self.driver.page_source)
        self.driver.refresh()

        LoginPage.clickForgotUsernameLink(self)
        ForgotPasswordPage.fillForgotUserNameForm(self,
                                                  zip="12345789",
                                                  email="svetatestbox@gmail.com")
        time.sleep(5)
        self.assertIn(text1, self.driver.page_source)
        self.driver.refresh()

        LoginPage.clickForgotUsernameLink(self)
        ForgotPasswordPage.fillForgotUserNameForm(self,
                                                  zip="",
                                                  email="svetatestbox@gmail.com")

        time.sleep(2)
        self.assertIn(text2, self.driver.page_source)
        self.driver.refresh()

        LoginPage.clickForgotUsernameLink(self)
        ForgotPasswordPage.fillForgotUserNameForm(self,
                                                  zip="89104",
                                                  email="")

        time.sleep(2)
        self.assertIn(text3, self.driver.page_source)
        self.driver.refresh()

        LoginPage.clickForgotUsernameLink(self)
        ForgotPasswordPage.fillForgotUserNameForm(self,
                                                  zip="89104",
                                                  email="svetatestbox@gmail.com")

        time.sleep(2)
        self.assertIn(text, self.driver.page_source)

        LoginPage.clickForgotUsernameLink(self)
        ForgotPasswordPage.fillForgotUserNameForm(self,
                                                  zip="8",
                                                  email="svetatestbox@gmail.com")

        time.sleep(2)
        self.assertIn(text1, self.driver.page_source)


