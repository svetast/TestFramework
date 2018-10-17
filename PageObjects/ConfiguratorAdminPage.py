import time
from telnetlib import EC

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait

from HelperTestBase import HelperTestBase


class ConfiguratorAdminPage(HelperTestBase):

    def ConfiguratorAdmin(self):
        driver = self.driver
        self.base_url = 'http://admin.ltodemo.com'
        driver.get(self.base_url)

    def loginAdminStage(self, username='svetast', password='Pp123456'):
        self.driver.get('https://admin.ltostage.com')
        self.driver.find_element_by_id("ctl00_uxMainContent_UserName").send_keys(username)
        self.driver.find_element_by_id("ctl00_uxMainContent_Password").send_keys(password)
        self.driver.find_element_by_id("ctl00_uxMainContent_Password").send_keys(Keys.ENTER)

    def loginAdminDemo(self, username='svetast', password='Qw123456'):
        self.driver.get('http://admin.ltodemo.com')
        self.driver.find_element_by_id("ctl00_uxMainContent_UserName").send_keys(username)
        self.driver.find_element_by_id("ctl00_uxMainContent_Password").send_keys(password)
        self.driver.find_element_by_id("ctl00_uxMainContent_Password").send_keys(Keys.ENTER)

    def loginAdminProd(self, username='svetast', password='Pp123456'):
        self.driver.get('https://admin.ltomall.com')
        self.driver.find_element_by_id("ctl00_uxMainContent_UserName").send_keys(username)
        self.driver.find_element_by_id("ctl00_uxMainContent_Password").send_keys(password)
        self.driver.find_element_by_id("ctl00_uxMainContent_Password").send_keys(Keys.ENTER)

    def loginUserAllRoles_STAGE(self, username='svetast1', password='Ss123456'):
        self.driver.get('https://admin.ltostage.com')
        self.driver.find_element_by_id("ctl00_uxMainContent_UserName").send_keys(username)
        self.driver.find_element_by_id("ctl00_uxMainContent_Password").send_keys(password)
        self.driver.find_element_by_id("ctl00_uxMainContent_Password").send_keys(Keys.ENTER)

    def logOut(self):
        element_present = EC.element_to_be_clickable((By.ID, "ctl00_uxLoginStatus"))
        WebDriverWait(self.driver, 20).until(element_present)
        self.driver.find_element_by_link_text("LOGOUT").click()

    def changeRole(self):
        self.driver.get('https://admin.ltostage.com')
