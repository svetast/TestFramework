from selenium.webdriver.common.keys import Keys

from HelperTestBase import HelperTestBase


class ConfiguratorPortalsStagePage(HelperTestBase):
    def ConfiguratorPortalsStagePage(self):
        driver = self.driver
        self.base_url = 'https://stg.mainstreetlto.com'  # zipcode = '19116'
        driver.get(self.base_url)

    def openPortal(self, zipcode='19116'):
        self.driver.find_element_by_id("zipcode").send_keys(zipcode)
        self.driver.find_element_by_id("zipcode").send_keys(Keys.ENTER)
