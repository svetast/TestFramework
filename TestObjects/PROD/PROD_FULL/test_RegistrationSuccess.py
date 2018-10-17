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


class TestRegistrationSuccess(RegistrationPage1):

    @pytest.mark.skip
    def test_registration_GetSpendingLimitSuccess(self):
        driver = self.driver
        driver.get(self.base_url)
        url_1 = self.base_url + '/Account/Signup'
        url_2 = self.base_url + '/Account/ApplyNow'
        url_3 = self.base_url + '/Account/ApplyNow#'
        x = random.randint(10, 1000)
        text3 = 'Employment Information'
        text4 = 'Personal Information'
        text5 = 'Payment Information'
        text6 = 'Congratulations!'

        self.driver.get(url_1)
        time.sleep(5)
        self.assertEqual(url_1, HelperTestBase.getURL(self))

        ##### Page 1: START  ###########

        RegistrationPage1.fillForm1(self,
                                    email='Svetlana_Stepanova@microbilt.com',
                                    username='svetast' + str(x),
                                    password="Ss123456",
                                    passwordConfirm="Ss123456",
                                    answer='valya',
                                    zipcode='89104')

        # zipcode='19116')stage.mainstreet
        # zipcode='89104')stage.smarttires
        # zipcode='53563') ltodemo.com
        # zipcode='19966') stg.patriottireleasing

        # zipcode='60130') stg.wheelzontime.com

        time.sleep(15)
        self.assertEqual(url_2, HelperTestBase.getURL(self))

        ################## Page2 : Contact Information  #########################

        RegistrationPage2.fillForm2(self,
                                    firstName='sveta',
                                    lastName='step' + str(x),
                                    address='2711 E. Sahara Ave',
                                    phone='6547899123')

        # address='15160 Sunflower Drive' # zipcode='19116'     #stage.mainstreet
        # address='2711 E. Sahara Ave' # zipcode='89104'        # stage.smarttires
        # address='123 RedLeaf Way. RedLeaf' #  zipcode='53563'  # ltodemo.com
        # address='36533 Pebble Dr,' # zipcode='19966'     # stg.patriottireleasing
        # address='7600 W. Roosevelt Rd') # zipcode ='60130'# stg.wheelzontime.com

        time.sleep(15)
        self.assertEqual(url_3, HelperTestBase.getURL(self))
        self.assertIn(text3, self.driver.page_source)

        ################## Page3: Employment Information   #########################

        RegistrationPage3.fillForm3(self,
                                    employerName='Private Firm Niagara',
                                    empPhone='5986547899',
                                    income='9999',
                                    ohterIncome='')

        time.sleep(10)
        self.assertIn(text4, self.driver.page_source)

        ################## Page4: Personal Information   #########################

        RegistrationPage4.fillForm4(self,
                                    ssn='121512230',
                                    driverLic='999999999',
                                    state="AL")
        time.sleep(15)
        self.assertIn(text5, self.driver.page_source)

        ######## Page5:     Payment Information   ###########################

        RegistrationPage5.fillForm5(self, accountType='DebitCard',
                                    cardNumber='5454-5454-5454-5454',
                                    cvv="1234",
                                    month='10',
                                    year='2020')

        time.sleep(18)
        self.assertIn(text6, self.driver.page_source)
        # self.assertIs(True, RegistrationPage.checkContinue(self))
