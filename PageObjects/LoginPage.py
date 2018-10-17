import time
from telnetlib import EC

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from PageObjects.SearchPage import SearchPage
from HelperTestBase import HelperTestBase


class LoginPage(SearchPage):
    def LoginPage(self):
        driver = self.driver
        driver.get(self.base_url)

    def logIn(self, userName=None, password=None):
        self.driver.find_element_by_id("login_username").send_keys(userName)
        self.driver.find_element_by_id("login_password").send_keys(password)
        self.driver.find_element_by_xpath("//button[@class='button theme-bg']").click()
        HelperTestBase.waitLogOutLink(self)

    def logInUnSuccess(self, userName=None, password=None):
        self.driver.find_element_by_id("login_username").send_keys(userName)
        self.driver.find_element_by_id("login_password").send_keys(password)
        self.driver.find_element_by_xpath("//button[@class='button theme-bg']").click()


    def clickForgotPasswordLink(self):
        self.driver.get(self.base_url + '/Account/Login')
        self.driver.find_element_by_link_text("I forgot my password").click()

    def clickForgotUsernameLink(self):
        self.driver.get(self.base_url + '/Account/Login')
        self.driver.find_element_by_link_text("I forgot my username").click()

    def checkCreateAccLink(self):
        element = self.driver.find_element_by_link_text("Create Account").is_displayed()
        return element

    def checkLoginForm(self):
        element = self.driver.find_element_by_id('login_username').is_displayed()
        return element

    def checkSearchField(self):
        element = self.driver.find_element_by_name("searchterm").is_displayed()
        return element

    def startRegistration(self):
        self.driver.get(self.base_url + '/Account/Signup')
        HelperTestBase.waitNextButton(self)




    def fillZipCode(self, zipcode=None):
        self.driver.find_element_by_id("zipcode").send_keys(zipcode)
        self.clickContinueZipCode()

    def clickContinueZipCode(self):
        self.driver.find_element_by_xpath("//*[@id='zipCodePopup']/div/div[2]/button").click()

    def submitZipCode(self, zipcode=None):
        self.fillZipCode(zipcode='89104')
        self.clickContinueZipCode()
        # self.fillZipCode(self, zipcode='19116') #stage.mainstreet
        # self.fillZipCode(self, zipcode='89104') #stage.smarttires
        # self.fillZipCode(self, zipcode='53563')  # ltodemo.com
        # self.fillZipCode(self, zipcode='19966')  # ## stg.patriottireleasing

    def selectMainstreet(self):
        self.driver.find_element_by_id("zipcode").send_keys('19116')
        self.clickContinueZipCode()

    def selectSmartTires(self):
        self.driver.find_element_by_id("zipcode").send_keys('89104')
        self.clickContinueZipCode()

    def selectPatriot(self):
        self.driver.find_element_by_id("zipcode").send_keys('19966')
        self.clickContinueZipCode()

    def selectLTODemo(self):
        self.driver.find_element_by_id("zipcode").send_keys('53563')
        self.clickContinueZipCode()
