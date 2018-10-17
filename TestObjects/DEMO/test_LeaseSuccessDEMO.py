import time

import pytest

from PageObjects.LoginPage import LoginPage
from PageObjects.HomePage import HomePage
from PageObjects.SearchResultsPage import SearchResultsPage
from PageObjects.CartPage import CartPage
from PageObjects.LeasePage import LeasePage

from PageObjects.ConfiguratorAdmin import ConfiguratorAdmin
from PageObjects.OrdersAdminPage import OrdersAdminPage


class TestLeaseCreatingSuccessDEMO(LeasePage):
    """Test scenario:
        1.User LogIn on Portal.
        2.Check that Cart is empty.
        3.The product added to Cart.
        4.Lease processing => OK, 'Thank you.' is displayed.
        5.Check that Cart is empty after purchased.
        6.Returt to start test data: Go to ADMIN and change order status to Canceled """

    #@pytest.mark.skip
    def test_LeaseSuccessDEMO(self):
        driver = self.driver
        driver.get(self.base_url + '/Account/Login')
        url_1 = self.base_url + '/cart'
        text1 = 'Thank you.'
        text2 = 'No items found in your cart.'
        url_2 = self.base_url + '/cart'
        url_3 = 'http://admin.ltodemo.com'

        LoginPage.logIn(self, "svetast1576", "Ss123456")
        # HomePage.submitSearch(self, 'lenovo')
        HomePage.submitSearch(self, 'canon')
        SearchResultsPage.clickAddToCart(self)
        driver.get(url_2)
        time.sleep(5)
        CartPage.clickCheckoutButton(self)
        time.sleep(3)
        # CartPage.selectPriceReviewedOptIn(self)
        CartPage.clickReviewYourLease(self)
        LeasePage.signAgreement(self, firstName='Sveta', lastName=' Step1576')
        time.sleep(10)
        self.assertIn(text1, self.driver.page_source)
        driver.get(url_1)
        time.sleep(5)
        self.assertIn(text2, self.driver.page_source)

        """#####  Return Test Data ##########
        driver.get(url_3)
        ConfiguratorAdmin.loginAdminDemo(self)
        driver.get(url_3 + '/Secure/Orders/OrderManagement/ViewOrders/Default.aspx')
        OrdersAdminPage.findOrdersByLastname(self, 'Step1576')
        OrdersAdminPage.clickManageOrder(self)
        OrdersAdminPage.clickUpdateOrderStatus(self)
        OrdersAdminPage.clickCancelOrder(self)
        time.sleep(10)
        OrdersAdminPage.clickBackToOrderList(self)"""
