from selenium.webdriver.common.keys import Keys

from HelperTestBase import HelperTestBase


class ConfiguratorAdmin(HelperTestBase):

    def ConfiguratorAdmin(self):
        driver = self.driver
        self.base_url = 'http://admin.ltodemo.com'
        driver.get(self.base_url)

    def loginAdminStage(self, username='svetast', password='Qq123456'):
        self.driver.get('https://admin.ltostage.com')
        self.driver.find_element_by_id("ctl00_uxMainContent_UserName").send_keys(username)
        self.driver.find_element_by_id("ctl00_uxMainContent_Password").send_keys(password)
        self.driver.find_element_by_id("ctl00_uxMainContent_Password").send_keys(Keys.ENTER)

    def loginAdminDemo(self, username='svetast', password='Qw123456'):
        self.driver.get('http://admin.ltodemo.com')
        self.driver.find_element_by_id("ctl00_uxMainContent_UserName").send_keys(username)
        self.driver.find_element_by_id("ctl00_uxMainContent_Password").send_keys(password)
        self.driver.find_element_by_id("ctl00_uxMainContent_Password").send_keys(Keys.ENTER)

    def loginAdminProd(self, username='svetast', password='Qq123456'):
        self.driver.get('https://admin.ltomall.com')
        self.driver.find_element_by_id("ctl00_uxMainContent_UserName").send_keys(username)
        self.driver.find_element_by_id("ctl00_uxMainContent_Password").send_keys(password)
        self.driver.find_element_by_id("ctl00_uxMainContent_Password").send_keys(Keys.ENTER)
