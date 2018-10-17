import time

from selenium.webdriver.common.keys import Keys

from PageObjects.HomePage import HomePage


class SearchResultsPage(HomePage):
    def SearchResultsPage(self):
        driver = self.driver
        driver.get(self.base_url)

    ####### Check element is present    ########################

    def checkPriceHighLowFilter(self):
        element = self.driver.find_element_by_id("ddSearchSort").is_displayed()
        return element

    def checkPageSortFilter(self):
        element = self.driver.find_element_by_id('page-sort').is_displayed()
        return element

    def checkPageSizeFilter(self):
        element = self.driver.find_element_by_id('ddSearchPage').is_displayed()
        return element

    def checkPriceFrom(self):
        element = self.driver.find_element_by_id('priceFrom').is_displayed()
        return element

    def checkPriceTo(self):
        element = self.driver.find_element_by_id('priceTo').is_displayed()
        return element

    def checkDisplayIcon(self):
        element = self.driver.find_element_by_xpath("//a[@class='view-type-item']").is_displayed()
        return element

    def checkLoupIcon(self):
        element = self.driver.find_element_by_xpath("//svg[@class='icon icon-search-second']").is_displayed()
        return element

    def checkAddToCart(self):
        addButton = self.driver.find_elements_by_link_text("Add to cart")
        addButton[0].is_displayed()
        return addButton

    def checkNextLink(self):
        element = self.driver.find_element_by_xpath("//a[@class='next-link']").is_displayed()
        return element

    def checkFirstLink(self):
        element = self.driver.find_element_by_xpath("//a[@class='prev-link']").is_displayed()
        return element

    ######  Actions with elements   #################

    def clickNextLink(self):
        self.driver.find_element_by_xpath("//a[@class='next-link']").click()

    def clickFirstLink(self):
        self.driver.find_element_by_xpath("//a[@class='prev-link']").click()

    def clickOnPage(self):
        addButton = self.driver.find_elements_by_xpath("//li[@class='paging-item']")
        addButton[0].click()

    def clickOnPageSizeFilter(self):
        self.driver.find_element_by_id('ddSearchSort').click()

    def clickDisplayIconList(self):
        icon = self.driver.find_elements_by_xpath("//a[@class='view-type-item']")
        icon[0].click()

    def clickDisplayIconTab(self):
        icon = self.driver.find_elements_by_xpath("//a[@class='view-type-item']")
        icon[1].click()

    def checkElements(self):
        self.assertIs(True, SearchResultsPage.checkPriceHighLowFilter(self))
        self.assertIs(True, SearchResultsPage.checkPageSortFilter(self))
        self.assertIs(True, SearchResultsPage.checkPageSizeFilter(self))
        self.assertIs(True, SearchResultsPage.checkPriceFrom(self))
        self.assertIs(True, SearchResultsPage.checkPriceTo(self))
        self.assertIs(True, SearchResultsPage.checkDisplayIcon(self))
        self.assertIs(True, SearchResultsPage.checkNextLink(self))
        self.assertIs(True, SearchResultsPage.checkFirstLink(self))

    def clickAddToCart(self):
        addButton = self.driver.find_elements_by_link_text("Add to cart")
        addButton[0].click()
        time.sleep(3)
