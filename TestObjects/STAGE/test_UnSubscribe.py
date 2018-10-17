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
        text0 = 'Please enter valid email address.'
        text1 = 'Thanks!  You will be unsubscribed from future promotional emails.  Please allow up to 10 business days for this to fully take effect.'

        time.sleep(5)

        NavigationMenuPage.clickUnsubscribe(self)
        ### test scope - check that Email field is required :
        UnSubscribePage.clickRemove(self)
        self.assertIn(text0, self.driver.page_source)
        self.driver.refresh()
        ### test scope - check Email field validation :
        UnSubscribePage.fillUnSubscribeForm(self, 'sveta@')
        UnSubscribePage.clickRemove(self)
        self.assertIn(text0, self.driver.page_source)
        self.driver.refresh()

        UnSubscribePage.fillUnSubscribeForm(self, 'sveta@ppp')
        UnSubscribePage.clickRemove(self)
        self.assertIn(text0, self.driver.page_source)
        self.driver.refresh()

        UnSubscribePage.fillUnSubscribeForm(self, '@gmail.com')
        UnSubscribePage.clickRemove(self)
        self.assertIn(text0, self.driver.page_source)
        self.driver.refresh()

        UnSubscribePage.fillUnSubscribeForm(self, 'asdfdfggh')
        UnSubscribePage.clickRemove(self)
        self.assertIn(text0, self.driver.page_source)
        self.driver.refresh()

        UnSubscribePage.fillUnSubscribeForm(self, 'asd@@fd.fggh')
        UnSubscribePage.clickRemove(self)
        self.assertIn(text0, self.driver.page_source)
        self.driver.refresh()

        UnSubscribePage.fillUnSubscribeForm(self, 'svetatestbox    12345@gmail.com')
        UnSubscribePage.clickRemove(self)
        self.assertIn(text0, self.driver.page_source)
        self.driver.refresh()

        ### test scope - unsubscribe success :
        UnSubscribePage.fillUnSubscribeForm(self, 'svetatestbox123456@gmail.com')
        UnSubscribePage.clickRemove(self)
        self.assertIn(text1, self.driver.page_source)
        UnSubscribePage.clickVisitHomePageLink(self)
        self.assertIs(True, HomePage.checkSearchPresent(self))
