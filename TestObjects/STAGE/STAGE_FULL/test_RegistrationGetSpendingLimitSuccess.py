import time
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

    def test_registration_GetSpendingLimitSuccess(self):
        driver = self.driver
        driver.get(self.base_url)
        url_1 = self.base_url + '/Account/Signup'
        url_2 = self.base_url + '/Account/ApplyNow'
        url_3 = self.base_url + '/Account/ApplyNow#'
        x = random.randint(100, 10000)
        text3 = 'Employment Information'
        text4 = 'Personal Information'
        text5 = 'Payment Information'
        text6 = 'Congratulations!'
        PORTAL = 'mainstreet'

        time.sleep(3)
        driver.get(self.base_url + '/Account/Signup')

        # self.assertEqual(url_1, HelperTestBase.getURL(self))

        ##### Page 1: START Let’s Create Your Account  ###########

        RegistrationPage1.fillForm1(self,
                                    email='svetlana_stepanova@microbilt.com',
                                    username='svetast' + str(x),
                                    password="Ss123456",
                                    passwordConfirm="Ss123456",
                                    answer='valya')

        # self.assertEqual(url_2, HelperTestBase.getURL(self))
        HelperTestBase.waitNextButton(self)

        ################## Page2 : Contact Information  #########################

        RegistrationPage2.fillForm2(self,
                                    firstName='sveta',
                                    lastName='step' + str(x),
                                    phone='7777777777',
                                    portal=PORTAL)

        time.sleep(20)
        self.assertEqual(url_3, HelperTestBase.getURL(self))
        self.assertIn(text3, self.driver.page_source)

        ################## Page3: Employment Information   #########################

        RegistrationPage3.fillForm3(self,
                                    employerName='Private Firm Niagara',
                                    empPhone='5986547899',
                                    income='9999',
                                    ohterIncome='')

        time.sleep(5)
        # self.assertIn(text4, self.driver.page_source)

        ################## Page4: Personal Information   #########################

        RegistrationPage4.fillForm4(self,
                                    ssn='121512230',
                                    #driverLic='555555555',
                                    driverLic='12121212121212121212', #### => for to get iPredict Sorry Screen #####
                                    state="AL")
        time.sleep(10)
        self.assertIn(text5, self.driver.page_source)

        ######## Page5:     Payment Information   ###########################

        RegistrationPage5.fillForm5(self, accountType='DebitCard',
                                    cardNumber='5454-5454-5454-5454',
                                    # invalid cardNumber='4242-4242-4242-4242',
                                    cvv="1234",
                                    month='12',
                                    year='2021')

        time.sleep(35)
        self.assertIn(text6, self.driver.page_source)

        RegistrationPage5.clickContinueButton(self)
        time.sleep(15)
        self.assertIs(True, HomePage.checkINFOBannerPresent(self))
        HomePage.logOut(self)

        #####Test scope - new user can Log In with credentials:

        driver.get(self.base_url + '/Account/Login')
        LoginPage.logIn(self, "svetast" + str(x),
                        "Ss123456")
        self.assertIs(True, HomePage.checkLogOutLink(self))
