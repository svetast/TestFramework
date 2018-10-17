import time

import pytest

from PageObjects.RegistrationPage import RegistrationPage
from HelperTestBase import HelperTestBase
import random

from PageObjects.RegistrationPage1 import RegistrationPage1
from PageObjects.RegistrationPage2 import RegistrationPage2
from PageObjects.RegistrationPage3 import RegistrationPage3
from PageObjects.RegistrationPage4 import RegistrationPage4
from PageObjects.RegistrationPage5 import RegistrationPage5
from PageObjects.HomePage import HomePage


class TestRegistrationEmptyFields(RegistrationPage1):

    # @pytest.mark.skip
    def test_checkRequirementFields(self):
        driver = self.driver
        driver.get(self.base_url)
        url_1 = self.base_url + '/Account/Signup'
        # Requiure fied on Registation form Page 1:

        text0 = 'Email Address is required.'
        text1 = 'Email Address is required.'
        text2 = 'Username is required.'
        text3 = 'Password is required.'
        text4 = 'Re-type Password is required.'
        text5 = 'Security question is required.'
        text6 = 'Security answer is required.'

        # Required field on Registration form Page 2:

        text7 = 'First name is required.'
        text8 = 'Last name is required.'
        text9 = 'Street address is required.'
        text10 = 'Mobile phone number is required.'

        # Required field on Registration form Employment INFO  Page 3 :
        text11 = 'Employer Name is required.'
        text12 = 'Phone number is required.'
        text13 = 'Pay frequency is required.'
        text14 = 'Income is required.'
        text15 = 'Please select an option.'

        # Required field on Registration form Personal Information Page4:
        text16 = 'Social Security Number is required.'
        text17 = "Driver's License Number is required."
        text18 = 'State of Issue is required'
        text19 = 'Age Indicator is required.'

        # Success Page:
        text20 = 'Congratulations!'
        PORTAL = 'mainstreet'

        x = random.randint(10, 1000)

        self.driver.get(url_1)
        time.sleep(5)

        ##### Page 1: START Let’s Create Your Account ###########

        # self.assertEqual(url_1, HelperTestBase.getURL(self))
        RegistrationPage.selectTermsRadiobutton(self)

        RegistrationPage.clickNext(self)
        time.sleep(3)
        # self.assertEqual(url_1, HelperTestBase.getURL(self))
        self.assertIn(text0, self.driver.page_source)
        self.assertIn(text1, self.driver.page_source)
        self.assertIn(text2, self.driver.page_source)
        self.assertIn(text3, self.driver.page_source)
        self.assertIn(text4, self.driver.page_source)
        self.assertIn(text5, self.driver.page_source)
        self.assertIn(text6, self.driver.page_source)
        self.driver.get(url_1)

        RegistrationPage1.fillForm1(self,
                                    email='svetlana_stepanova@microbilt.com',
                                    username='svetast' + str(x),
                                    password="Ss123456",
                                    passwordConfirm="Ss123456",
                                    answer='valya')

        ########

        time.sleep(20)
        RegistrationPage.clickNext(self)
        time.sleep(5)

        self.assertIn(text7, self.driver.page_source)
        self.assertIn(text8, self.driver.page_source)
        self.assertIn(text9, self.driver.page_source)
        self.assertIn(text10, self.driver.page_source)

        self.driver.refresh()

        ################## Page2 : Contact Information  #########################

        HelperTestBase.waitNextButton(self)
        time.sleep(2)

        RegistrationPage2.fillForm2(self,
                                    firstName='sveta',
                                    lastName='step' + str(x),
                                    phone='1111111111',
                                    portal=PORTAL)

        time.sleep(15)
        self.assertIn(text11, self.driver.page_source)
        RegistrationPage.clickNext(self)

        ################## Page3: Employment Information   #########################

        RegistrationPage.clickNext(self)
        time.sleep(2)
        self.assertIn(text11, self.driver.page_source)
        self.assertIn(text12, self.driver.page_source)
        self.assertIn(text13, self.driver.page_source)
        self.assertIn(text14, self.driver.page_source)
        self.assertIn(text15, self.driver.page_source)

        RegistrationPage3.fillForm3(self,
                                    employerName='Private Firm Niagara',
                                    empPhone='5986547899',
                                    income='9999',
                                    ohterIncome='')

        time.sleep(5)

        ################## Page4: Personal Information   #########################

        RegistrationPage.clickNext(self)
        time.sleep(2)
        self.assertIn(text16, self.driver.page_source)
        self.assertIn(text17, self.driver.page_source)
        self.assertIn(text18, self.driver.page_source)
        self.assertIn(text19, self.driver.page_source)

        RegistrationPage4.fillForm4(self,
                                    ssn='121512230',
                                    driverLic='555555555',
                                    state="AL")
        time.sleep(5)

        ######## Page5: Payment Information   ###########################

        RegistrationPage5.fillForm5(self, accountType='DebitCard',
                                    cardNumber='5454-5454-5454-5454',
                                    cvv="1234",
                                    month='12',
                                    year='2021')

        time.sleep(30)
        self.assertIn(text20, self.driver.page_source)
