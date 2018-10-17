import time
from telnetlib import EC

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from PageObjects.SearchPage import SearchPage
from HelperTestBase import HelperTestBase


class LoginPageAdminStage(SearchPage):
    def LoginPage(self):
        driver = self.driver
        driver.get(self.base_url)

    def logIn(self, userName=None, password=None):
        time.sleep(10)
        self.driver.find_element_by_id("login_username").send_keys(userName)
        self.driver.find_element_by_id("login_password").send_keys(password)
        self.driver.find_element_by_xpath("//button[@class='button theme-bg']").click()
        time.sleep(3)
