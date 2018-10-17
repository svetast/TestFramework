import time

from selenium.webdriver.common.keys import Keys

from PageObjects.LoginPage import LoginPage
from HelperTestBase import HelperTestBase


class LeasePage(HelperTestBase):
    def LeasePage(self):
        driver = self.driver
        driver.get(self.base_url)

    def signAgreement(self, firstName=None, lastName=None):
        self.driver.find_element_by_id("lessee_name").send_keys(firstName, lastName)
        time.sleep(5)
        self.clickContinue()

    def clickContinue(self):
        self.driver.find_element_by_id("agreement-submit").click()
