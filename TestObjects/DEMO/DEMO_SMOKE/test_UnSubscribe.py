import time

from PageObjects.LoginPage import LoginPage
from PageObjects.UnsubscribePage import UnSubscribePage
from PageObjects.NavigationMenuPage import NavigationMenuPage
from HelperTestBase import HelperTestBase
from PageObjects.HomePage import HomePage


class TestUnSubscribe(UnSubscribePage):

    def test_submitUnSubscribeForm(self):
        driver = self.driver
        driver.get(self.base_url)
        text1 = 'Thanks!  You will be unsubscribed from future promotional emails.  Please allow up to 10 business days for this to fully take effect.'

        ### test scope - unsubscribe success :
        NavigationMenuPage.clickUnsubscribe(self)
        UnSubscribePage.fillUnSubscribeForm(self, 'svetatestbox123456@gmail.com')
        UnSubscribePage.clickRemove(self)
        time.sleep(2)
        self.assertIn(text1, self.driver.page_source)
        ### back to HomePage:
        UnSubscribePage.clickVisitHomePageLink(self)
        self.assertIs(True, HomePage.checkSearchPresent(self))
