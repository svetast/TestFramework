import time

import pytest

from HelperTestBase import HelperTestBase
from PageObjects.LoginPage import LoginPage
from PageObjects.HomePage import HomePage
from PageObjects.CartPage import CartPage

from PageObjects.SearchResultsPage import SearchResultsPage


class TestCartValidation(CartPage):

    # DO NOT USE for TIRES untill add Vechil
    # @pytest.mark.skip
    def test_CartQTY(self):
        """Test scope - impossible add to Cart : 0, 100, empty data, invalid data => appropriate message is displayed.
         The 'No items found in your cart.' is displayed after product has been removed from Cart."""

        driver = self.driver
        driver.get(self.base_url + '/Account/Login')
        url_2 = self.base_url + '/cart'

        text1 = 'No items found in your cart.'
        text5 = 'Change Payment Method'

        LoginPage.logIn(self, "svetast555", "Ss123456")
        HomePage.submitSearch(self, 'canon')
        time.sleep(3)
        SearchResultsPage.clickAddToCart(self)
        driver.get(url_2)
        time.sleep(2)

        CartPage.clickChangePaymentInfoLink(self)
        time.sleep(3)
        self.assertIn(text5, self.driver.page_source)
        self.driver.back()

        CartPage.clickContinueShoppingButton(self)
        time.sleep(6)
        self.assertIs(True, HomePage.checkINFOBannerPresent(self))
        self.driver.back()
        time.sleep(5)

        CartPage.setQTY(self, '100')
        time.sleep(5)
        self.assertIs(True, CartPage.checkErrorMessagePresent(self))
        self.driver.refresh()

        CartPage.setQTY(self, '')
        time.sleep(5)
        self.assertIs(True, CartPage.checkErrorMessagePresent(self))
        self.driver.refresh()

        CartPage.setQTY(self, 'As!@#$%^&*()_-+<>?')
        time.sleep(5)
        self.assertIs(True, CartPage.checkErrorMessagePresent(self))
        self.driver.refresh()

        self.driver.refresh()
        CartPage.setQTY(self, '0')
        time.sleep(5)
        self.assertIs(True, CartPage.checkErrorMessagePresent(self))
        self.driver.refresh()

        CartPage.setQTY(self, '1')
        CartPage.clickCheckoutButton(self)
        time.sleep(5)
        CartPage.clickEditButton(self)
        CartPage.clickRemoveFromCartButton(self)
        time.sleep(5)
        self.assertIn(text1, self.driver.page_source)
