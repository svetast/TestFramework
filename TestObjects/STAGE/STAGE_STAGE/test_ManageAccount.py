import time

import pytest

from PageObjects.LoginPage import LoginPage
from HelperTestBase import HelperTestBase
from PageObjects.ContactUsPage import ContactUsPage
from PageObjects.ManageAccountPage import ManageAccountPage

from PageObjects.HomePage import HomePage


class TestManageAccount(ManageAccountPage):

    def test_checkNavigation(self):
        driver = self.driver
        driver.get(self.base_url + '/Account/Dashboard')
        text1 = self.base_url + '/account/orderhistory'
        text2 = self.base_url + '/account/ordershipping'
        text3 = self.base_url + '/account/Settings'
        text4 = self.base_url + '/account/addressbook'
        text5 = self.base_url + '/LTO/EditEmploymentInformation'
        text6 = self.base_url + '/LTO/EditPersonalInformation'
        text7 = 'Change Payment Method'
        text9 = self.base_url + '/account/dashboard'

        text10 = "Register to Make Payments"

        LoginPage.logIn(self, "svetast555", "Ss123456")

        ManageAccountPage.clickOrderHistory(self)
        time.sleep(2)
        self.assertEqual(text1, HelperTestBase.getURL(self))
        self.driver.back()

        ManageAccountPage.clickTrackShipping(self)
        time.sleep(2)
        self.assertEqual(text2, HelperTestBase.getURL(self))
        self.driver.back()

        ManageAccountPage.clickAccountSettings(self)
        time.sleep(2)
        self.assertEqual(text3, HelperTestBase.getURL(self))
        self.assertIs(True, ManageAccountPage.checkNewPasswordFieldPresent(self))
        self.assertIs(True, ManageAccountPage.checkNewEmailAddressFielfPresent(self))
        self.driver.back()
        time.sleep(3)

        ManageAccountPage.clickAddressAndPhone(self)
        time.sleep(2)
        self.assertEqual(text4, HelperTestBase.getURL(self))
        self.assertIs(True, ManageAccountPage.checkAddressFieldPresent(self))
        self.assertIs(True, ManageAccountPage.checkZipCodeFielfPresent(self))
        self.assertIs(True, ManageAccountPage.checkMobilePhoneFielfPresent(self))
        self.driver.back()
        time.sleep(2)

        ManageAccountPage.clickEmploymentInformation(self)
        time.sleep(2)
        self.assertEqual(text5, HelperTestBase.getURL(self))
        self.driver.back()
        time.sleep(2)

        ManageAccountPage.clickPersonalInformation(self)
        time.sleep(2)
        self.assertEqual(text6, HelperTestBase.getURL(self))
        self.assertIs(True, ManageAccountPage.checkSaveButton_Present(self))
        self.assertIs(True, ManageAccountPage.checkCancelButton_Present(self))
        self.assertIs(True, ManageAccountPage.checkSSNPresent(self))
        self.assertIs(True, ManageAccountPage.checkDriverLisensePresent(self))
        self.assertIs(True, ManageAccountPage.checkDriverLisenseStatePresent(self))
        self.driver.back()
        time.sleep(2)

        ManageAccountPage.clickChangePaymentMethod(self)
        time.sleep(2)
        self.assertIn(text7, self.driver.page_source)
        self.driver.back()
        time.sleep(2)

        ManageAccountPage.clickAccountSummary(self)
        time.sleep(2)
        self.assertEqual(text9, HelperTestBase.getURL(self))
        self.driver.back()
        time.sleep(2)

        ManageAccountPage.clickShopNow(self)
        time.sleep(2)
        self.assertIs(True, HomePage.checkINFOBannerPresent(self))
        self.driver.back()
        time.sleep(2)
