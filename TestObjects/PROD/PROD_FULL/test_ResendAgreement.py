import time

import pytest

from PageObjects.ConfiguratorAdminPage import ConfiguratorAdminPage
from PageObjects.LoginPage import LoginPage
from PageObjects.OrdersAdminPage import OrdersAdminPage


class TestResendAgreement(LoginPage):

    # @pytest.mark.skip
    # @pytest.mark.order1
    def test_ReSendAgreementSuccess_STAGE(self):
        driver = self.driver
        s = '/Secure/Orders/OrderManagement/ViewOrders/Default.aspx'
        url_3 = 'https://admin.ltostage.com' + s
        text1 = 'Agreement has been sent.'

        ConfiguratorAdminPage.loginAdminStage(self)
        ### click on View Orders:
        driver.get(url_3)
        time.sleep(10)
        OrdersAdminPage.findOrdersByLastname(self, 'step1968')
        time.sleep(8)
        OrdersAdminPage.clickManageOrder(self)
        OrdersAdminPage.clickReSendAgreement(self)
        time.sleep(15)
        self.assertIn(text1, self.driver.page_source)
