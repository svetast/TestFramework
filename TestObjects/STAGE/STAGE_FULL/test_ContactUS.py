import random
import time

from PageObjects.LoginPage import LoginPage
from HelperTestBase import HelperTestBase
from PageObjects.ContactUsPage import ContactUsPage
from PageObjects.NavigationMenuPage import NavigationMenuPage


class TestContactUs(NavigationMenuPage):

    def test_checkRequiredFields(self):
        ### test scope - check that fields are required :
        driver = self.driver
        driver.get(self.base_url)
        text0 = 'First name is required.'
        text1 = 'Last name is required.'
        text2 = 'Email Address is required.'
        text3 = 'Subject is required'
        text4 = 'Message is required'

        time.sleep(5)
        NavigationMenuPage.clickContactUS(self)
        time.sleep(2)
        ContactUsPage.clickSendButton(self)
        time.sleep(2)
        self.assertIn(text0, self.driver.page_source)
        self.assertIn(text1, self.driver.page_source)
        self.assertIn(text2, self.driver.page_source)
        self.assertIn(text3, self.driver.page_source)
        self.assertIn(text4, self.driver.page_source)

    def test_submitContactUsForm(self):
        driver = self.driver
        driver.get(self.base_url)
        text0 = 'Thank you for your feedback!'
        x = random.randint(1000, 10000)

        time.sleep(5)
        NavigationMenuPage.clickContactUS(self)
        ContactUsPage.fillForm(self,
                               firstName='sveta',
                               lastName='step',
                               email='svetlana_stepanova@microbilt.com',
                               subject='test ContactUs form' + str(x),
                               message='test ContactUs form' + str(x))
        ContactUsPage.clickSendButton(self)
        time.sleep(5)
        self.assertIn(text0, self.driver.page_source)
