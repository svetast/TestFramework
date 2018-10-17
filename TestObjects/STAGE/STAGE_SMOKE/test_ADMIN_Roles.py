import time

import pytest

from HelperTestBase import HelperTestBase
from PageObjects.ConfiguratorAdminPage import ConfiguratorAdminPage


class TestADMIN_Roles(HelperTestBase):

    @pytest.mark.skip
    def test_ADMIN_Roles(self):
        driver = self.driver
        url_3 = 'https://admin.ltostage.com'

        driver.get(url_3)
        time.sleep(5)

        ConfiguratorAdminPage.loginAdminStage(self)
        time.sleep(10)
        ConfiguratorAdminPage.changeRole(self)
        ConfiguratorAdminPage.logOut(self)
        driver.get(url_3)
        time.sleep(5)
        ConfiguratorAdminPage.loginUserAllRoles_STAGE(self)

        self.assertEqual(len(HelperTestBase.checkElementExist(self)), 0)
        # self.driver.find_element_by_xpath('//span[text()="Dashboard"]').click()
        ConfiguratorAdminPage.logOut(self)
