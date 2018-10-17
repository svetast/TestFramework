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

    # @pytest.mark.parametrize
    def test_registration_GetSpendingLimitUnSuccess_InvalidDriverLicense(self):
        driver = self.driver
        driver.get(self.base_url)
        url_1 = self.base_url + '/Account/Signup'
        url_2 = self.base_url + '/Account/ApplyNow'
        url_3 = self.base_url + '/Account/ApplyNow#'
        x = random.randint(10, 1000)
        text3 = 'Employment Information'
        text4 = 'Personal Information'
        text5 = 'Payment Information'
        text7 = 'We’re sorry.'
        text8 = 'We were unable to locate enough information to approve you for a spending limit at this time.'

        LoginPage.startRegistration(self)
        self.driver.refresh()
        self.assertEqual(url_1, HelperTestBase.getURL(self))


        ##### Page 1: START  ###########

        RegistrationPage1.fillForm1(self,
                                    email='Svetlana_Stepanova@microbilt.com',
                                    username='svetast' + str(x),
                                    password="Ss123456",
                                    passwordConfirm="Ss123456",
                                    answer='valya')


        time.sleep(20)
        # self.assertEqual(url_2, HelperTestBase.getURL(self))

        ################## Page2 : Contact Information  #########################

        RegistrationPage2.fillForm2(self,
                                    firstName='sveta',
                                    lastName='step' + str(x),
                                    phone='6547899123',
                                    portal='ltodemo')



        time.sleep(20)
        # self.assertEqual(url_3, HelperTestBase.getURL(self))
        self.assertIn(text3, self.driver.page_source)

        ################## Page3: Employment Information   #########################

        RegistrationPage3.fillForm3(self,
                                    employerName='Private Firm Niagara',
                                    empPhone='5986547899',
                                    income='9855',
                                    ohterIncome='')

        time.sleep(20)
        self.assertIn(text4, self.driver.page_source)

        ################## Page4: Personal Information   #########################

        RegistrationPage4.fillForm4(self, ssn='121512230',
                                    driverLic='111111111',
                                    state='LA')
        time.sleep(20)
        self.assertIn(text5, self.driver.page_source)

        ######## Page5: Payment Information   ###################################

        RegistrationPage5.fillForm5(self, accountType='DebitCard',
                                    cardNumber='5454-5454-5454-5454',
                                    cvv="1234",
                                    month='10',
                                    year='2020')

        time.sleep(35)
        self.assertIn(text7, self.driver.page_source)
        self.assertIn(text8, self.driver.page_source)








