import time

from PageObjects.RegistrationPage import RegistrationPage
from HelperTestBase import HelperTestBase
from PageObjects.HomePage import HomePage

import random

from PageObjects.RegistrationPage1 import RegistrationPage1
from PageObjects.RegistrationPage2 import RegistrationPage2
from PageObjects.RegistrationPage3 import RegistrationPage3
from PageObjects.RegistrationPage4 import RegistrationPage4
from PageObjects.RegistrationPage5 import RegistrationPage5
from PageObjects.LoginPage import LoginPage


class TestRegistrationUnSuccessAgeLimitation(RegistrationPage):

    def test_registrationAgeUnder18(self):
        driver = self.driver
        driver.get(self.base_url)
        url_1 = self.base_url + '/Account/Signup'
        url_2 = self.base_url + '/Account/ApplyNow'
        url_3 = self.base_url + '/Account/ApplyNow#'
        x = random.randint(10, 1000)
        text3 = 'Employment Information'
        text4 = 'Personal Information'
        text7 = 'We’re sorry.'
        text8 = 'We were unable to locate enough information to approve you for a spending limit at this time.'

        LoginPage.startRegistration(self)

        ##### Page 1: START  ###########
        PORTAL = 'mainstreet'

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

        ################## Page3: Employment Information   #########################

        RegistrationPage3.fillForm3(self,
                                    employerName='Private Firm Niagara',
                                    empPhone='5986547899',
                                    income='9999',
                                    ohterIncome='')

        ################## Page4: Personal Information   #########################

        RegistrationPage4.fillForm4_AgeLimitation(self,
                                                  ssn='121512230',
                                                  driverLic='555555555',
                                                  state='PA'
                                                  )
        time.sleep(35)
        self.assertIn(text7, self.driver.page_source)
        self.assertIn(text8, self.driver.page_source)

        ### Check that Home button is present:
        RegistrationPage5.clickHomeButton(self)

        ### click on Home button => Home Page is opened, INFO banner, Header menu, Footer menu, Search field  are presennt:
        self.assertIs(True, HomePage.checkINFOBannerPresent(self))
        self.assertIs(True, HomePage.checkHeaderMenuPresent(self))
        self.assertIs(True, HomePage.checkFooterMenuPresent(self))
        self.assertIs(True, HomePage.checkSearchPresent(self))

        ######## Page5:     Payment Information  NOT USING IN THIS CASE ###########################
