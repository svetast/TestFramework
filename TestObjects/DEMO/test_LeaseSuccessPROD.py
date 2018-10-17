import time

import pytest

from PageObjects.LoginPage import LoginPage
from PageObjects.HomePage import HomePage
from PageObjects.SearchResultsPage import SearchResultsPage
from PageObjects.CartPage import CartPage
from PageObjects.LeasePage import LeasePage

from PageObjects.ConfiguratorAdmin import ConfiguratorAdmin
from PageObjects.OrdersAdminPage import OrdersAdminPage


class TestLeaseCreatingSuccessPROD(LeasePage):
    """Test scenario:
        1.User LogIn on Portal.
        2.Check that Cart is empty.
        3.The product added to Cart.
        4.Lease processing => OK, 'Thank you.' is displayed.
        5.Check that Cart is empty after purchased.
        6.Returt to start test data: Go to ADMIN and change order status to Canceled """

    @pytest.mark.skip
    def test_LeaseSuccessPROD(self):
        driver = self.driver
        driver.get(self.base_url + '/Account/Login')
        text1 = 'Thank you.'
        text2 = 'No items found in your cart.'
        url_3 = 'https://admin.ltomall.com'
        url_2 = self.base_url + '/cart'

        LoginPage.logIn(self, "svetast8078", "Ss123456")
        HomePage.submitSearch(self, 'canon')
        SearchResultsPage.clickAddToCart(self)
        driver.get(url_2)
        time.sleep(8)
        CartPage.clickCheckoutButton(self)
        time.sleep(3)
        CartPage.selectPriceReviewedOptIn(self)
        CartPage.clickReviewYourLease(self)
        LeasePage.signAgreement(self, firstName='sveta', lastName=' step8078')
        time.sleep(35)
        self.assertIn(text1, self.driver.page_source)
        driver.get(url_2)
        time.sleep(5)
        self.assertIn(text2, self.driver.page_source)

        #####  Return Test Data ##########
        """driver.get(url_3)
        ConfiguratorAdmin.loginAdminStage(self)
        driver.get(url_3 + '/Secure/Orders/OrderManagement/ViewOrders/Default.aspx')
        OrdersAdminPage.findOrdersByLastname(self, 'step1968')
        OrdersAdminPage.clickManageOrder(self)
        OrdersAdminPage.clickUpdateOrderStatus(self)
        OrdersAdminPage.clickCancelOrder(self)
        time.sleep(10)
        OrdersAdminPage.clickBackToOrderList(self)"""

    @pytest.mark.skip
    def test_LeaseSuccessPROD_Tires(self):
        driver = self.driver
        driver.get(self.base_url + '/Account/Login')
        text1 = 'Thank you.'
        text2 = 'No items found in your cart.'
        url_3 = 'https://admin.ltomall.com'
        url_2 = self.base_url + '/cart'

        LoginPage.logIn(self, "svetast1968", "Ss123456")
        HomePage.submitSearch(self, 'road')
        SearchResultsPage.clickAddToCart(self)
        driver.get(url_2)
        time.sleep(8)
        CartPage.clickCheckoutButton(self)
        time.sleep(3)
        CartPage.selectPriceReviewedOptIn(self)
        CartPage.clickReviewYourLease(self)
        LeasePage.signAgreement(self, firstName='sveta', lastName=' step1968')
        time.sleep(30)
        self.assertIn(text1, self.driver.page_source)
        driver.get(url_2)
        time.sleep(5)
        self.assertIn(text2, self.driver.page_source)

        #####  Return Test Data ##########
        driver.get(url_3)
        ConfiguratorAdmin.loginAdminProd(self)
        driver.get(url_3 + '/Secure/Orders/OrderManagement/ViewOrders/Default.aspx')
        OrdersAdminPage.findOrdersByLastname(self, 'step1968')
        OrdersAdminPage.clickManageOrder(self)
        OrdersAdminPage.clickUpdateOrderStatus(self)
        OrdersAdminPage.clickCancelOrder(self)
        time.sleep(10)
        OrdersAdminPage.clickBackToOrderList(self)

