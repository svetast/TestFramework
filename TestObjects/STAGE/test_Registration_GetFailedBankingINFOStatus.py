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


class TestRegistrationInvalidCardNumber(RegistrationPage1):



    # @pytest.mark.skip
    def test_registration_GetFailedBankingINFOStatus(self):
        driver = self.driver
        url_1 = self.base_url + '/Account/Signup'
        url_2 = self.base_url + '/Account/Login'
        url_3 = self.base_url + '/Account/ApplyNow#'

        x = random.randint(100, 10000)
        text3 = 'Employment Information'
        text4 = 'Personal Information'
        text5 = 'Payment Information'
        text7 = 'Payment Type is not authorized. Please try again with a different account (DECLINE).'

        text8 = 'We’re sorry.'
        text9 = 'We were unable to locate enough information to approve you for a spending limit at this time.'

        driver.get(url_1)
        PORTAL = 'mainstreet'

        ##### Page 1: START  ###########

        HelperTestBase.waitNextButton(self)

        RegistrationPage1.fillForm1(self,
                                    email='svetatestbox@gmail.com',
                                    username='svetast' + str(x),
                                    password="Ss123456",
                                    passwordConfirm="Ss123456",
                                    answer='valya')

        HelperTestBase.waitNextButton(self)

        ################## Page2 : Contact Information  #########################

        RegistrationPage2.fillForm2(self,
                                    firstName='sveta',
                                    lastName='step' + str(x),
                                    phone='6547899123',
                                    portal=PORTAL)

        time.sleep(20)
        self.assertIn(text3, self.driver.page_source)

        ################## Page3: Employment Information   #########################

        RegistrationPage3.fillForm3(self,
                                    employerName='Private Firm Niagara',
                                    empPhone='5986547899',
                                    income='9999',
                                    ohterIncome='')

        time.sleep(6)
        self.assertIn(text4, self.driver.page_source)

        ################## Page4: Personal Information   #########################

        RegistrationPage4.fillForm4(self,
                                    ssn='121512230',
                                    driverLic='555555555',
                                    state="AL")
        time.sleep(6)
        self.assertIn(text5, self.driver.page_source)

        ######## Page5:     Payment Information   ###########################

        RegistrationPage5.fillForm5(self, accountType='DebitCard',
                                    cardNumber='4242-4242-4242-4242',
                                    cvv="1234",
                                    month='10',
                                    year='2020')

        time.sleep(15)
        self.assertEqual(True, RegistrationPage5.checkError(self))
        self.assertEqual(text7, RegistrationPage5.getError(self))
        self.driver.refresh()
        time.sleep(15)

        RegistrationPage5.fillForm5(self, accountType='DebitCard',
                                    cardNumber='4242-4242-4242-4242',
                                    cvv="1234",
                                    month='10',
                                    year='2020')
        time.sleep(15)
        self.assertEqual(True, RegistrationPage5.checkError(self))
        self.assertEqual(text7, RegistrationPage5.getError(self))
        self.driver.refresh()
        time.sleep(15)

        RegistrationPage5.fillForm5(self, accountType='DebitCard',
                                    cardNumber='4242-4242-4242-4242',
                                    cvv="1234",
                                    month='10',
                                    year='2020')

        time.sleep(30)
        self.assertIn(text8, self.driver.page_source)
        self.assertIn(text9, self.driver.page_source)

        #### Test scope : Click on HOME button on Unsuccess page = > Home page is opened, INFO Banner is present:
        HelperTestBase.waitHomeButton(self)
        RegistrationPage5.clickHomeButton(self)
        time.sleep(15)
        self.assertIs(True, HomePage.checkINFOBannerPresent(self))

    # @pytest.mark.skip
    def test_registration_IncompleteStatus_CardNumberNotExist(self):
        """Test scope - Check that user get error message if entered not exist Card 0000000000000000 """
        driver = self.driver
        driver.get(self.base_url)
        url_1 = self.base_url + '/Account/Signup'
        url_2 = self.base_url + '/Account/Login'
        url_3 = self.base_url + '/Account/ApplyNow#'
        PORTAL = 'mainstreet'

        x = random.randint(100, 10000)
        text3 = 'Employment Information'
        text4 = 'Personal Information'
        text5 = 'Payment Information'
        text7 = 'Payment Type is not authorized. Please try again with a different account (DECLINE).'
        text8 = 'Please enter a valid card number.'
        text9 = 'We were unable to locate enough information to approve you for a spending limit at this time.'

        text10 = 'Payment Type is not authorized. Please try again with a different account (Error: E00027 (TESTMODE) The credit card number is invalid.).'

        LoginPage.startRegistration(self)
        self.driver.refresh()
        self.assertEqual(url_1, HelperTestBase.getURL(self))

        ##### Page 1: START  ###########
        HelperTestBase.waitNextButton(self)

        RegistrationPage1.fillForm1(self,
                                    email='svetatestbox@gmail.com',
                                    username='svetast' + str(x),
                                    password="Ss123456",
                                    passwordConfirm="Ss123456",
                                    answer='valya')

        HelperTestBase.waitNextButton(self)

        ################## Page2 : Contact Information  #########################

        RegistrationPage2.fillForm2(self,
                                    firstName='Sveta',
                                    lastName='Step' + str(x),
                                    phone='6547899123',
                                    portal=PORTAL)

        time.sleep(5)
        self.assertIn(text3, self.driver.page_source)

        ################## Page3: Employment Information   #########################

        RegistrationPage3.fillForm3(self,
                                    employerName='Private Firm Niagara',
                                    empPhone='5986547899',
                                    income='9999',
                                    ohterIncome='')

        time.sleep(6)
        self.assertIn(text4, self.driver.page_source)

        ################## Page4: Personal Information   #########################

        RegistrationPage4.fillForm4(self,
                                    ssn='121512230',
                                    driverLic='555555555',
                                    state="AL")
        time.sleep(6)
        self.assertIn(text5, self.driver.page_source)

        self.assertIs(True, RegistrationPage4.checkCardNumberPresent(self))

        ######## Page5:     Payment Information   ###########################

        RegistrationPage5.fillForm5(self, accountType='DebitCard',
                                    cardNumber='1111111111111111',
                                    cvv="1234",
                                    month='10',
                                    year='2020')

        time.sleep(3)
        self.assertIn(text8, self.driver.page_source)
        self.driver.refresh()

        RegistrationPage5.fillForm5(self, accountType='DebitCard',
                                    cardNumber='0000000000000000',
                                    cvv="1234",
                                    month='10',
                                    year='2020')

        time.sleep(15)
        self.assertIs(True, ErrorMessagesPage.checkErrorMessage(self))

