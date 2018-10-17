import time

import pytest

from PageObjects.ConfiguratorAdmin import ConfiguratorAdmin
from PageObjects.LoginPage import LoginPage
from PageObjects.OrdersAdminPage import OrdersAdminPage


class TestResendAgreement(LoginPage):

    @pytest.mark.skip
    @pytest.mark.order1
    def test_ReSendAgreementSuccess_STAGE(self):
        driver = self.driver
        s = '/Secure/Orders/OrderManagement/ViewOrders/Default.aspx'
        url_3 = 'https://admin.ltostage.com' + s
        text1 = 'Agreement has been sent.'

        ConfiguratorAdmin.loginAdminStage(self)
        ### click on View Orders:
        driver.get(url_3)
        time.sleep(10)
        OrdersAdminPage.findOrdersByLastname(self, 'step1968')
        time.sleep(8)
        OrdersAdminPage.clickManageOrder(self)
        OrdersAdminPage.clickReSendAgreement(self)
        time.sleep(15)
        self.assertIn(text1, self.driver.page_source)

    @pytest.mark.skip
    @pytest.mark.order2
    def test_ReSendAgreementSuccess_PROD(self):
        driver = self.driver
        s = '/Secure/Orders/OrderManagement/ViewOrders/Default.aspx'
        url_3 = 'https://admin.ltomall.com' + s
        text1 = 'Agreement has been sent.'

        ConfiguratorAdmin.loginAdminProd(self)
        ### click on View Orders:
        driver.get(url_3)
        time.sleep(10)
        OrdersAdminPage.findOrdersByLastname(self, 'step1968')
        time.sleep(8)
        OrdersAdminPage.clickManageOrder(self)
        OrdersAdminPage.clickReSendAgreement(self)
        time.sleep(10)
        self.assertIn(text1, self.driver.page_source)

    #@pytest.mark.skip
    @pytest.mark.order3
    def test_ReSendAgreementSuccess_Demo(self):
        driver = self.driver
        s = '/Secure/Orders/OrderManagement/ViewOrders/Default.aspx'
        url_3 = 'http://admin.ltodemo.com' + s
        text1 = 'Agreement has been sent.'

        ConfiguratorAdmin.loginAdminDemo(self)
        ### click on View Orders:
        driver.get(url_3)
        time.sleep(10)
        OrdersAdminPage.findOrdersByLastname(self, 'step1576')
        time.sleep(8)
        OrdersAdminPage.clickManageOrder(self)
        OrdersAdminPage.clickReSendAgreement(self)
        time.sleep(10)
        self.assertIn(text1, self.driver.page_source)
