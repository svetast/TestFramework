import time

import pytest

from HelperTestBase import HelperTestBase
from PageObjects.HomePage import HomePage

import random

from PageObjects.RegistrationPage1 import RegistrationPage1
from PageObjects.RegistrationPage2 import RegistrationPage2
from PageObjects.RegistrationPage3 import RegistrationPage3
from PageObjects.RegistrationPage4 import RegistrationPage4
from PageObjects.RegistrationPage5 import RegistrationPage5
from PageObjects.LoginPage import LoginPage
from PageObjects.ErrorMessagesPage import ErrorMessagesPage


class TestDontAccessStatesRegistration(RegistrationPage1):

    # @pytest.mark.skip
    def test_DontAccessStatesRegistration(self):
        driver = self.driver
        url_1 = self.base_url + '/Account/Signup'

        x = random.randint(100, 10000)
        text2 = 'Sorry we currently do not service your location. Please try a different zip code.'
        text3 = 'Program is not available in WI, MN, NC, NJ'

        driver.get(url_1)

        ##### Page 1: START  ###########
        # Test scope: Check 'Sorry, we currently do not service your location. Please try a different area.'

        self.driver.find_element_by_id('PostalCode').clear()
        self.driver.find_element_by_id('PostalCode').send_keys("54101")

        time.sleep(2)
        self.assertIn(text2, self.driver.page_source)
        self.driver.refresh()

        self.driver.find_element_by_id('PostalCode').clear()
        self.driver.find_element_by_id('PostalCode').send_keys("55106")

        time.sleep(2)
        self.assertIn(text2, self.driver.page_source)
        self.driver.refresh()

        self.driver.find_element_by_id('PostalCode').clear()
        self.driver.find_element_by_id('PostalCode').send_keys("27010")

        time.sleep(2)
        self.assertIn(text2, self.driver.page_source)
        self.driver.refresh()

        self.driver.find_element_by_id('PostalCode').clear()
        self.driver.find_element_by_id('PostalCode').send_keys("08840")

        time.sleep(2)
        self.assertIn(text2, self.driver.page_source)
        self.driver.refresh()

        HelperTestBase.waitNextButton(self)
        RegistrationPage1.fillForm1(self,
                                    email='svetatestbox@gmail.com',
                                    username='svetast' + str(x),
                                    password="Ss123456",
                                    passwordConfirm="Ss123456",
                                    answer='valya')

        HelperTestBase.waitNextButton(self)

        ################## Page2 : Contact Information  #########################

        #  Test scope:Check 'Program is not available in WI, MN, NC, NJ':

        self.driver.find_element_by_id('PostalCode').clear()
        self.driver.find_element_by_id('PostalCode').send_keys("55106")
        time.sleep(2)
        self.assertIn(text3, self.driver.page_source)

        self.driver.find_element_by_id('PostalCode').clear()
        self.driver.find_element_by_id('PostalCode').send_keys("27010")
        time.sleep(2)
        self.assertIn(text3, self.driver.page_source)

        self.driver.find_element_by_id('PostalCode').clear()
        self.driver.find_element_by_id('PostalCode').send_keys("54101")
        time.sleep(2)
        self.assertIn(text3, self.driver.page_source)

        self.driver.find_element_by_id('PostalCode').clear()
        self.driver.find_element_by_id('PostalCode').send_keys("08840")
        time.sleep(2)
        self.assertIn(text3, self.driver.page_source)
