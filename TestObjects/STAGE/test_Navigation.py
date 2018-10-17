import time

from PageObjects.LoginPage import LoginPage
from HelperTestBase import HelperTestBase
from PageObjects.NavResultsPage import NavResultsPage
from PageObjects.NavigationMenuPage import NavigationMenuPage


class TestNavigation(NavigationMenuPage):

    def test_navigationHeaderUnAuthorizedUser(self):
        driver = self.driver
        driver.get(self.base_url + '/Account/Login')
        text = 'Frequently Asked Questions'
        text1 = 'About Us'
        text2 = 'Contact Us'
        text3 = 'Payment Portal Logon'

        NavigationMenuPage.clickHowItWorks(self)
        self.assertIs(True, NavResultsPage.checkCreateAccButton(self))
        self.driver.back()

        NavigationMenuPage.clickFAQ(self)
        self.assertIn(text, self.driver.page_source)
        self.driver.back()

        NavigationMenuPage.clickAboutUS(self)
        self.assertIn(text1, self.driver.page_source)
        self.driver.back()

        NavigationMenuPage.clickContactUS(self)
        self.assertIn(text2, self.driver.page_source)
        self.driver.back()

        NavigationMenuPage.clickMakePayment(self)
        self.assertIn(text3, self.driver.page_source)
        self.driver.back()

    def test_navigationHeaderAuthorizedUser(self):
        driver = self.driver
        driver.get(self.base_url + '/Account/Login')
        text = 'Frequently Asked Questions'
        text1 = 'About Us'
        text2 = 'Contact Us'
        text3 = 'Payment Portal Logon'

        LoginPage.logIn(self, "svetast555", "Ss123456")

        NavigationMenuPage.clickHowItWorks(self)
        self.assertIs(True, NavResultsPage.checkContentHowItsWorkPage(self))
        self.driver.back()

        NavigationMenuPage.clickFAQ(self)
        self.assertIn(text, self.driver.page_source)
        self.driver.back()

        NavigationMenuPage.clickAboutUS(self)
        self.assertIn(text1, self.driver.page_source)
        self.driver.back()

        NavigationMenuPage.clickContactUS(self)
        self.assertIn(text2, self.driver.page_source)
        self.driver.back()

        NavigationMenuPage.clickMakePayment(self)
        self.assertIn(text3, self.driver.page_source)
        self.driver.back()

    def test_navigationFooterUnAuthorizedUser(self):


        driver = self.driver
        driver.get(self.base_url + '/Account/Login')
        text = 'Frequently Asked Questions'
        text2 = 'Contact Us'
        text3 = 'Privacy Policy'
        text4 = 'Terms and Conditions of Use'
        text5 = 'Unsubscribe'

        NavigationMenuPage.clickHowItWorksFooter(self)
        time.sleep(2)
        self.assertIs(True, NavResultsPage.checkCreateAccLink(self))
        self.driver.back()

        NavigationMenuPage.clickFAQFooter(self)
        time.sleep(2)
        self.assertIn(text, self.driver.page_source)
        self.driver.back()

        NavigationMenuPage.clickContactUS_Footer(self)
        time.sleep(2)
        self.assertIn(text2, self.driver.page_source)
        self.driver.back()

        NavigationMenuPage.clickPrivacyPolicy(self)
        time.sleep(2)
        self.assertIn(text3, self.driver.page_source)
        self.driver.back()

        NavigationMenuPage.clickTerms(self)
        time.sleep(2)
        self.assertIn(text4, self.driver.page_source)
        self.driver.back()

        NavigationMenuPage.clickUnsubscribe(self)
        time.sleep(2)
        self.assertIn(text5, self.driver.page_source)
        self.driver.back()

    def test_navigationFooterAuthorizedUser(self):


        driver = self.driver
        driver.get(self.base_url + '/Account/Login')
        text = 'Frequently Asked Questions'
        text2 = 'Contact Us'
        text3 = 'Privacy Policy'
        text4 = 'Terms and Conditions of Use'
        text5 = 'Unsubscribe'

        LoginPage.logIn(self, "svetast555", "Ss123456")

        NavigationMenuPage.clickHowItWorksFooter(self)
        time.sleep(5)
        self.assertIs(True, NavResultsPage.checkContentHowItsWorkPage(self))
        self.driver.back()

        NavigationMenuPage.clickFAQFooter(self)
        time.sleep(2)

        self.assertIn(text, self.driver.page_source)
        self.driver.back()

        NavigationMenuPage.clickContactUS_Footer(self)

        time.sleep(2)

        self.assertIn(text2, self.driver.page_source)
        self.driver.back()

        NavigationMenuPage.clickPrivacyPolicy(self)

        time.sleep(2)

        self.assertIn(text3, self.driver.page_source)
        self.driver.back()

        NavigationMenuPage.clickTerms(self)
        time.sleep(2)
        self.assertIn(text4, self.driver.page_source)
        self.driver.back()

        NavigationMenuPage.clickUnsubscribe(self)
        time.sleep(2)
        self.assertIn(text5, self.driver.page_source)
        self.driver.back()
