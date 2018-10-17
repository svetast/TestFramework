import time

import pytest
from selenium.webdriver.support.select import Select

from PageObjects.LoginPage import LoginPage
from HelperTestBase import HelperTestBase
from PageObjects.LoginPage import LoginPage
from PageObjects.NavigationMenuPage import NavigationMenuPage
from PageObjects.SearchResultsPage import SearchResultsPage
from PageObjects.HomePage import HomePage


class TestSearch(SearchResultsPage):

    def test_checkSearchFunction_UnAuthorizedUser(self):
        driver = self.driver
        driver.get(self.base_url + '/Account/Login')
        text1 = 'No results match your search.'

        ### Check Search Field validation :

        HomePage.submitSearch(self, '!@#$%^&*()_+><?')
        time.sleep(1)
        self.assertIn(text1, self.driver.page_source)
        NavigationMenuPage.goToHomePage(self)
        HomePage.submitSearch(self, 'kolobok')
        time.sleep(1)
        self.assertIn(text1, self.driver.page_source)
        NavigationMenuPage.goToHomePage(self)

        ### Check pangination on search results : ###

        HomePage.submitSearch(self, 'furniture')
        time.sleep(3)
        SearchResultsPage.checkElements(self)
        SearchResultsPage.clickNextLink(self)
        time.sleep(3)
        SearchResultsPage.checkElements(self)
        SearchResultsPage.clickFirstLink(self)
        time.sleep(3)
        SearchResultsPage.checkElements(self)
        SearchResultsPage.clickOnPage(self)
        time.sleep(3)
        SearchResultsPage.checkElements(self)
