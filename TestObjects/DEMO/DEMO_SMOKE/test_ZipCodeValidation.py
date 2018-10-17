import time

import pytest

from HelperTestBase import HelperTestBase
from PageObjects.HomePage import HomePage
from PageObjects.LoginPage import LoginPage


class TestZipCodeValidation(LoginPage):

    def test_zipcodeValidation(self):
        driver = self.driver
        driver.get(self.base_url + '/Account/Login')
        text1 = 'Please enter your shipping zip code'
        text2 = 'Sorry we currently do not service your location. Please try a different zip code.'
        text3 = 'This is not a valid US zip code.'

        HelperTestBase.checkZipcodeValidation(self, '123654789')
        self.assertIn(text2, self.driver.page_source)
        self.driver.refresh()
        time.sleep(2)

        HelperTestBase.checkZipcodeValidation(self, '1111111111111111111')
        self.assertIn(text2, self.driver.page_source)
        self.driver.refresh()
        time.sleep(2)

        HelperTestBase.checkZipcodeValidation(self, '55000')
        time.sleep(2)
        self.assertIn(text3, self.driver.page_source)
        self.driver.refresh()
        time.sleep(2)

        HelperTestBase.checkZipcodeValidation(self, '55  000')
        time.sleep(2)
        self.assertIn(text3, self.driver.page_source)
        self.driver.refresh()

        HelperTestBase.checkZipcodeValidation(self, 'Ee!@#$%^&*()_+<>')
        time.sleep(2)
        self.assertIn(text1, self.driver.page_source)
        self.driver.refresh()

        HelperTestBase.checkZipcodeValidation(self, '')
        time.sleep(2)
        self.assertIn(text1, self.driver.page_source)
        self.driver.refresh()

        HelperTestBase.checkZipcodeValidation(self, '8')
        time.sleep(2)
        self.assertIn(text3, self.driver.page_source)
        self.driver.refresh()

        # Check states (in these states LTO business is banned)=> zips should NOT be accepted - WI, MN, NC, NJ:

        HelperTestBase.checkZipcodeValidation(self, '54101')
        time.sleep(2)
        self.assertIn(text2, self.driver.page_source)
        self.driver.refresh()

        HelperTestBase.checkZipcodeValidation(self, '55106')
        time.sleep(2)
        self.assertIn(text2, self.driver.page_source)
        self.driver.refresh()

        HelperTestBase.checkZipcodeValidation(self, '27010')
        time.sleep(2)
        self.assertIn(text2, self.driver.page_source)
        self.driver.refresh()

        HelperTestBase.checkZipcodeValidation(self, '08840')
        time.sleep(2)
        self.assertIn(text2, self.driver.page_source)
        self.driver.refresh()
