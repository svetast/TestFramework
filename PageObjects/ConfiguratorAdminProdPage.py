from selenium.webdriver.common.keys import Keys

from HelperTestBase import HelperTestBase
from PageObjects.ConfiguratorAdminPage import ConfiguratorAdminPage


class ConfiguratorAdminProdPage(ConfiguratorAdminPage):
    def ConfiguratorAdminProdPage(self):
        driver = self.driver
        self.base_url = 'https://admin.ltomall.com'
        driver.get(self.base_url)

        ConfiguratorAdminPage.loginAdminStage(self)
