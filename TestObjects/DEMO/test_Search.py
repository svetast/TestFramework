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

    def test_checkSearchFunction_AuthorizedUser(self):
        driver = self.driver
        driver.get(self.base_url + '/Account/Login')
        text1 = 'No results match your search.'

        LoginPage.logIn(self, "svetast555", "Ss123456")
        HelperTestBase.waitLogOutLink(self)
        time.sleep(2)

        ### Check Search Field validation :

        HomePage.submitSearch(self, 'àáâãäåçèéêëìíîðñòôõöö')
        time.sleep(3)
        self.assertIn(text1, self.driver.page_source)
        NavigationMenuPage.goToHomePage(self)

        HomePage.submitSearch(self, '!@#$%^&*()_+><?')
        time.sleep(2)
        self.assertIn(text1, self.driver.page_source)
        NavigationMenuPage.goToHomePage(self)

        HomePage.submitSearch(self, 'kolobok')
        time.sleep(3)
        self.assertIn(text1, self.driver.page_source)
        NavigationMenuPage.goToHomePage(self)
        # HomePage.submitSearch(self, '123')
        # time.sleep(4)
        # SearchResultsPage.checkElements(self)
        # NavigationMenuPage.goToHomePage(self)

        ### Check pangination on search results : ###

        # HomePage.submitSearch(self, 'road')

        HomePage.submitSearch(self, 'canon')
        time.sleep(5)
        SearchResultsPage.checkElements(self)
        SearchResultsPage.clickNextLink(self)
        time.sleep(5)
        SearchResultsPage.checkElements(self)
        SearchResultsPage.clickFirstLink(self)
        time.sleep(5)
        SearchResultsPage.checkElements(self)
        SearchResultsPage.clickOnPage(self)
        time.sleep(5)
        SearchResultsPage.checkElements(self)

        ### Check select Search Sort options  : ###

        select = Select(self.driver.find_element_by_id('ddSearchSort'))
        select.select_by_value("0")
        time.sleep(2)
        SearchResultsPage.checkElements(self)
        select = Select(self.driver.find_element_by_id('ddSearchSort'))
        select.select_by_value("1")
        time.sleep(2)
        SearchResultsPage.checkElements(self)
        select = Select(self.driver.find_element_by_id('ddSearchSort'))
        select.select_by_value("2")
        time.sleep(2)
        SearchResultsPage.checkElements(self)
        select = Select(self.driver.find_element_by_id('ddSearchSort'))
        select.select_by_value("3")
        time.sleep(2)
        SearchResultsPage.checkElements(self)
        select = Select(self.driver.find_element_by_id('ddSearchSort'))
        select.select_by_value("4")
        time.sleep(2)
        SearchResultsPage.checkElements(self)
        select = Select(self.driver.find_element_by_id('ddSearchSort'))
        select.select_by_value("5")
        time.sleep(2)
        SearchResultsPage.checkElements(self)
        select = Select(self.driver.find_element_by_id('ddSearchSort'))
        select.select_by_value("6")
        time.sleep(2)
        SearchResultsPage.checkElements(self)

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
        #         HomePage.submitSearch(self, '123')
        # time.sleep(3)
        # SearchResultsPage.checkElements(self)
        # NavigationMenuPage.goToHomePage(self)

        ### Check pangination on search results : ###

        HomePage.submitSearch(self, 'canon')
        # HomePage.submitSearch(self, 'dewalt')  # toolcabin
        time.sleep(5)
        SearchResultsPage.checkElements(self)
        SearchResultsPage.clickNextLink(self)
        time.sleep(5)
        SearchResultsPage.checkElements(self)
        SearchResultsPage.clickFirstLink(self)
        time.sleep(5)
        SearchResultsPage.checkElements(self)
        SearchResultsPage.clickOnPage(self)
        time.sleep(5)
        SearchResultsPage.checkElements(self)

    def test_check_SortByFilter_AuthorizedUser(self):
        driver = self.driver
        driver.get(self.base_url + '/Account/Login')

        LoginPage.logIn(self, "svetast555", "Ss123456")
        HelperTestBase.waitLogOutLink(self)

        ###### Select the appropriate test data !!!!!!
        HomePage.submitSearch(self, 'canon')
        #HomePage.submitSearch(self, 'road')  # toolcabin
        time.sleep(5)
        # HomePage.submitSearch(self, 'road')

        select = Select(self.driver.find_element_by_id('ddSearchSort'))
        select.select_by_value("0")
        time.sleep(2)
        SearchResultsPage.checkElements(self)

        select = Select(self.driver.find_element_by_id('ddSearchSort'))
        select.select_by_value("1")
        time.sleep(2)
        SearchResultsPage.checkElements(self)

        select = Select(self.driver.find_element_by_id('ddSearchSort'))
        select.select_by_value("2")
        time.sleep(2)
        SearchResultsPage.checkElements(self)

        select = Select(self.driver.find_element_by_id('ddSearchSort'))
        select.select_by_value("3")
        time.sleep(2)
        SearchResultsPage.checkElements(self)

        select = Select(self.driver.find_element_by_id('ddSearchSort'))
        select.select_by_value("4")
        time.sleep(2)
        SearchResultsPage.checkElements(self)

        select = Select(self.driver.find_element_by_id('ddSearchSort'))
        select.select_by_value("5")
        time.sleep(2)
        SearchResultsPage.checkElements(self)

        select = Select(self.driver.find_element_by_id('ddSearchSort'))
        select.select_by_value("6")
        time.sleep(2)
        SearchResultsPage.checkElements(self)

    def test_check_ProductsPerPageFilterHeader_AuthorizedUser(self):
        driver = self.driver
        driver.get(self.base_url + '/Account/Login')
        text1 = '1 - 30'
        text2 = '1 - 15'
        text3 = '1 - 45'
        text4 = '1 - 60'

        LoginPage.logIn(self, "svetast555", "Ss123456")
        HelperTestBase.waitLogOutLink(self)

        ###### Select the appropriate test data !!!!!!
        HomePage.submitSearch(self, 'furniture')
        #HomePage.submitSearch(self, 'road')  # toolcabin
        time.sleep(5)
        # HomePage.submitSearch(self, 'road')

        select = Select(self.driver.find_element_by_id('page-sort'))
        select.select_by_value("30")
        time.sleep(6)
        #self.assertIn(text1, self.driver.page_source)
        SearchResultsPage.checkElements(self)

        select = Select(self.driver.find_element_by_id('page-sort'))
        select.select_by_value("15")
        time.sleep(6)
        #self.assertIn(text2, self.driver.page_source)
        SearchResultsPage.checkElements(self)
        select = Select(self.driver.find_element_by_id('page-sort'))
        select.select_by_value("45")
        time.sleep(6)
        #self.assertIn(text3, self.driver.page_source)
        SearchResultsPage.checkElements(self)

        select = Select(self.driver.find_element_by_id('page-sort'))
        select.select_by_value("60")
        time.sleep(6)
        #self.assertIn(text4, self.driver.page_source)
        SearchResultsPage.checkElements(self)

    #@pytest.mark.skip
    def test_check_ProductsPerPageFilterFooter_AuthorizedUser(self):
        driver = self.driver
        driver.get(self.base_url + '/Account/Login')
        text1 = '1 - 30'
        text2 = '1 - 15'
        text3 = '1 - 45'
        text4 = '1 - 60'

        LoginPage.logIn(self, "svetast555", "Ss123456")
        HelperTestBase.waitLogOutLink(self)

        ###### Select the appropriate test data !!!!!!
        HomePage.submitSearch(self, 'furnirure')
        #HomePage.submitSearch(self, 'asus')  # toolcabin
        time.sleep(5)
        # HomePage.submitSearch(self, 'road')

        select = Select(self.driver.find_element_by_id('ddSearchPage'))
        select.select_by_value("30")
        time.sleep(6)
        #self.assertIn(text1, self.driver.page_source)
        SearchResultsPage.checkElements(self)

        select = Select(self.driver.find_element_by_id('ddSearchPage'))
        select.select_by_value("15")
        time.sleep(6)
        #self.assertIn(text2, self.driver.page_source)
        SearchResultsPage.checkElements(self)

        select = Select(self.driver.find_element_by_id('ddSearchPage'))
        select.select_by_value("45")
        time.sleep(6)
        #self.assertIn(text3, self.driver.page_source)
        SearchResultsPage.checkElements(self)
        select = Select(self.driver.find_element_by_id('ddSearchPage'))
        select.select_by_value("60")
        time.sleep(6)
        #self.assertIn(text4, self.driver.page_source)
        SearchResultsPage.checkElements(self)

        SearchResultsPage.clickDisplayIconList(self)
        SearchResultsPage.checkElements(self)
        self.driver.refresh()
        SearchResultsPage.clickDisplayIconTab(self)
        SearchResultsPage.checkElements(self)
