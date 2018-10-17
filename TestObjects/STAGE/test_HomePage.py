import time

from PageObjects.LoginPage import LoginPage
from HelperTestBase import HelperTestBase
from PageObjects.ContactUsPage import ContactUsPage
from PageObjects.HomePage import HomePage


class TestHomePage(HomePage):

    def test_checkElements(self):
        driver = self.driver
        driver.get(self.base_url)
        url_1 = self.base_url + '/Account/Login'

        # Test scope -  Check that HeaderMenu, FooterMenu, SearchField, INFO Banner are present on HomePage for UnAuthorized User

        time.sleep(3)

        self.assertIs(True, HomePage.checkINFOBannerPresent(self))
        self.assertIs(True, HomePage.checkHeaderMenuPresent(self))
        self.assertIs(True, HomePage.checkFooterMenuPresent(self))
        self.assertIs(True, HomePage.checkSearchPresent(self))

        # Test scope -  Check that HeaderMenu, FooterMenu, SearchField, INFO Banner are present on HomePage for Authorized User
        driver.get(url_1)
        LoginPage.logIn(self, "svetast555", "Ss123456")
        HelperTestBase.waitLogOutLink(self)
        driver.get(self.base_url)
        time.sleep(5)

        self.assertIs(True, HomePage.checkINFOBannerPresent(self))
        self.assertIs(True, HomePage.checkHeaderMenuPresent(self))
        self.assertIs(True, HomePage.checkFooterMenuPresent(self))
        self.assertIs(True, HomePage.checkSearchPresent(self))
