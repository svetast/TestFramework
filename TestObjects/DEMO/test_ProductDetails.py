import time

import pytest

from HelperTestBase import HelperTestBase
from PageObjects.LoginPage import LoginPage
from PageObjects.HomePage import HomePage
from PageObjects.ProductDetailsPage import ProductDetailsPage
from PageObjects.CartPage import CartPage


class TestProductDetails(ProductDetailsPage):

    # @pytest.mark.skip
    def test_ProductDetailsValidation(self):
        driver = self.driver
        driver.get(self.base_url + '/Account/Login')
        url_2 = self.base_url + '/cart'
        text2 = 'No items found in your cart.'
        text3 = 'In Stock'

        LoginPage.logIn(self, "svetast555", "Ss123456")
        HelperTestBase.waitLogOutLink(self)
        driver.get(self.base_url)
        time.sleep(5)
        ProductDetailsPage.clickOnDetailsButton(self)
        time.sleep(10)
        self.assertIs(True, ProductDetailsPage.checkQTY(self))
        self.assertIs(True, ProductDetailsPage.checkAddToCart(self))

        ##### Test scope - Check validation of QTY field  #########

        ProductDetailsPage.setQTY(self, qty='200')
        time.sleep(9)
        self.assertIs(True, ProductDetailsPage.checkError(self))
        ProductDetailsPage.setQTY(self, qty='0')
        time.sleep(9)
        self.assertIs(True, ProductDetailsPage.checkError(self))
        ProductDetailsPage.setQTY(self, qty='As!@#$%^&*()_+<>?')
        time.sleep(3)
        self.assertIs(True, ProductDetailsPage.checkError(self))
        ProductDetailsPage.setQTY(self, qty='1')
        time.sleep(5)

        ##### Test scope Click on Continue Shopping Button in Light => user stays on Product Details page  #########
        self.assertEqual(text3, ProductDetailsPage.checkStatusInStock(self))
        ProductDetailsPage.clickAddToCart(self)
        time.sleep(25)
        self.assertIs(True, ProductDetailsPage.checkViewCartButton(self))
        time.sleep(5)
        ProductDetailsPage.clickContinueShoppingButton(self)
        self.assertIs(True, ProductDetailsPage.checkAddToCart(self))

        #####   return test data ###########
        driver.get(url_2)
        CartPage.clickRemoveFromCartButton(self)
        time.sleep(5)
        self.assertIn(text2, self.driver.page_source)

        ##### Test scope Click on View Cart in Light => Cart page is opened  #########

        driver.get(self.base_url)
        time.sleep(2)
        ProductDetailsPage.clickOnDetailsButton(self)
        ProductDetailsPage.clickAddToCart(self)
        time.sleep(5)
        self.assertIs(True, ProductDetailsPage.checkViewCartButton(self))
        ProductDetailsPage.clickViewCart(self)
        CartPage.clickRemoveFromCartButton(self)
        time.sleep(2)
        self.assertIn(text2, self.driver.page_source)

        ##### Test scope Click on Close Button in Light  => user stays on Product Details page  #########

        driver.get(self.base_url)
        time.sleep(2)
        ProductDetailsPage.clickOnDetailsButton(self)
        ProductDetailsPage.clickAddToCart(self)
        time.sleep(5)
        self.assertIs(True, ProductDetailsPage.checkViewCartButton(self))
        ProductDetailsPage.closeLight(self)
        self.assertIs(True, ProductDetailsPage.checkAddToCart(self))

        #####   return test data ###########
        driver.get(url_2)
        CartPage.clickRemoveFromCartButton(self)
        time.sleep(2)
        self.assertIn(text2, self.driver.page_source)
        time.sleep(5)
