import time

from selenium.webdriver.common.keys import Keys

from PageObjects.LoginPage import LoginPage
from HelperTestBase import HelperTestBase


class HomePage(HelperTestBase):
    def HomePage(self):
        driver = self.driver
        driver.get(self.base_url)

        ### LogOut action:

    def logOut(self):
        self.driver.find_element_by_link_text("Log Out").click()
        time.sleep(3)

    def checkLogOutLink(self):
        element = self.driver.find_element_by_link_text("Log Out").is_displayed()
        return element

    def submitSearch(self, searchItem):
        self.driver.find_element_by_id("header-search-input").send_keys(searchItem)
        time.sleep(3)
        self.driver.find_element_by_id("header-search-input").send_keys(Keys.ENTER)

    ####### Elements : HeaderMenu, FooterMenu, SearchField, INFO Banner are present on HomePage #############


    def checkINFOBannerPresent(self):
        banner = self.driver.find_element_by_xpath("//div[@class='info-banner']").is_displayed()
        return banner

    def checkHeaderMenuPresent(self):
        elem = self.driver.find_element_by_xpath("//ul[@class='drop-nav-list']").is_displayed()
        return elem

    def checkFooterMenuPresent(self):
        elem = self.driver.find_element_by_xpath("//ul[@class='sub-nav']").is_displayed()
        return elem

    def checkSearchPresent(self):
        elem = self.driver.find_element_by_id("header-search-input").is_displayed()
        return elem
