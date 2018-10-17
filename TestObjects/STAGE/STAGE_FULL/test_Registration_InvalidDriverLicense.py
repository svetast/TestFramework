import time

from PageObjects.LoginPage import LoginPage
from HelperTestBase import HelperTestBase

from PageObjects.RegistrationPage1 import RegistrationPage1
from PageObjects.RegistrationPage2 import RegistrationPage2
from PageObjects.RegistrationPage3 import RegistrationPage3
from PageObjects.RegistrationPage4 import RegistrationPage4
from PageObjects.RegistrationPage5 import RegistrationPage5

import random


class TestRegistrationInvalidDriverLicense(RegistrationPage1):

    # @pytest.mark.skip
    # @pytest.mark.parametrize
    def test_registration_GetSpendingLimitUnSuccess_InvalidDriverLicense(self):
        driver = self.driver
        driver.get(self.base_url)
        url_1 = self.base_url + '/Account/Signup'

        x = random.randint(100, 1000)

        text7 = 'We’re sorry.'
        text8 = 'We were unable to locate enough information to approve you for a spending limit at this time.'
        PORTAL = 'mainstreet'

        LoginPage.startRegistration(self)

        ##### Page 1: START  ###########

        RegistrationPage1.fillForm1(self,
                                    email='',
                                    username='svetast' + str(x),
                                    password="Ss123456",
                                    passwordConfirm="Ss123456",
                                    answer='valya')

        time.sleep(5)

        ################## Page2 : Contact Information  #########################

        RegistrationPage2.fillForm2(self,
                                    firstName='sveta',
                                    lastName='step' + str(x),
                                    phone='3333333333',
                                    portal=PORTAL)

        ################## Page3: Employment Information   #########################

        RegistrationPage3.fillForm3(self,
                                    employerName='Private Firm Niagara',
                                    empPhone='5986547899',
                                    income='9855',
                                    ohterIncome='')

        ################## Page4: Personal Information   #########################

        RegistrationPage4.fillForm4(self, ssn='121512230',
                                    driverLic='111111111',
                                    state='PA')

        ######## Page5: Payment Information   ###################################

        RegistrationPage5.fillForm5(self, accountType='DebitCard',
                                    cardNumber='5454-5454-5454-5454',
                                    cvv="1234",
                                    month='10',
                                    year='2020')

        time.sleep(35)
        self.assertIn(text7, self.driver.page_source)
        self.assertIn(text8, self.driver.page_source)
