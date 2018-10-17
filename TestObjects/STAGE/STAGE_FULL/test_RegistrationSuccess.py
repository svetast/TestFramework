import time

import pytest

from HelperTestBase import HelperTestBase

import random

from PageObjects.RegistrationPage1 import RegistrationPage1
from PageObjects.RegistrationPage2 import RegistrationPage2
from PageObjects.RegistrationPage3 import RegistrationPage3
from PageObjects.RegistrationPage4 import RegistrationPage4
from PageObjects.RegistrationPage5 import RegistrationPage5
from PageObjects.LoginPage import LoginPage
from PageObjects.HomePage import HomePage


class TestRegistrationSuccess(RegistrationPage1):

    def test_LeaseSuccessSTAGE_NewUser(self):
        driver = self.driver
        driver.get(self.base_url)
        url_1 = self.base_url + '/Account/Signup'
        url_2 = self.base_url + '/Account/Login'
        x = random.randint(100, 10000)
        text6 = 'Congratulations!'
        driver.get(url_1)
        PORTAL = 'mainstreet'

        ##### Page 1: START  ###########

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
                                    phone='77777777777',
                                    portal=PORTAL)

        ################## Page3: Employment Information   #########################

        RegistrationPage3.fillForm3(self,
                                    employerName='Private Firm Niagara',
                                    empPhone='5986547899',
                                    income='9999',
                                    ohterIncome='')

        HomePage.logOut(self)
        driver.get(url_2)
        LoginPage.logIn(self, "svetast" + str(x), "Ss123456")
        HelperTestBase.waitLogOutLink(self)
        self.assertIs(True, RegistrationPage4.checkSSN_Present(self))

        ################## Page4: Personal Information   #########################

        RegistrationPage4.fillForm4(self,
                                    ssn='121512230',
                                    driverLic='555555555',
                                    state="PA")

        time.sleep(3)
        HomePage.logOut(self)
        driver.get(url_2)
        LoginPage.logIn(self, "svetast" + str(x), "Ss123456")
        HelperTestBase.waitLogOutLink(self)
        self.assertIs(True, RegistrationPage4.checkCardNumberPresent(self))

        ######## Page5:     Payment Information   ###########################

        RegistrationPage5.fillForm5(self, accountType='DebitCard',
                                    cardNumber='5454-5454-5454-5454',
                                    cvv="1234",
                                    month='12',
                                    year='2021')

        time.sleep(35)
        self.assertIn(text6, self.driver.page_source)
