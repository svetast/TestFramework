import random
import time

from PageObjects.LoginPage import LoginPage
from HelperTestBase import HelperTestBase
from PageObjects.ContactUsPage import ContactUsPage
from PageObjects.NavigationMenuPage import NavigationMenuPage


class TestContactUs(NavigationMenuPage):

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
                               email='svetatestbox@gmail.com',
                               subject='test subject',
                               message='test message' + str(x))
        ContactUsPage.clickSendButton(self)
        time.sleep(10)
        self.assertIn(text0, self.driver.page_source)
