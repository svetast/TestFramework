import time
from telnetlib import EC

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from HelperTestBase import HelperTestBase


class CartPage(HelperTestBase):
    def CartPage(self):
        driver = self.driver
        driver.get(self.base_url)

    def clickCheckoutButton(self):
        self.driver.find_element_by_link_text("Checkout").click()

    def clickContinueShopping(self):
        self.driver.find_element_by_link_text("Continue Shopping").click()

    def clickWouldYouLikeLDW(self):
        self.driver.find_element_by_id("LiabilityDamageWaiver").click()

    def clickRemoveFromCartButton(self):
        self.driver.find_element_by_id('remove-item-submit').click()
        time.sleep(2)

    def clickUpdateButton(self):
        self.driver.find_element_by_id('quantity-update-submit').click()
        time.sleep(2)


    def setQTY(self, qty=None):
        self.driver.find_element_by_id('Quantity').clear()
        self.driver.find_element_by_id('Quantity').send_keys(qty)
        self.driver.find_element_by_id('quantity-update-submit').click()



    def clickEditButton(self):
        self.driver.find_element_by_link_text('Edit').click()

    def clickReviewYourLease(self):
        self.driver.find_element_by_xpath("//button[@class='button theme-bg btn-inline']").click()

    def clickChangePaymentMethod(self):
        self.driver.find_element_by_link_text('Change Payment Method').click()

    def selectPriceReviewedOptIn(self):
        self.driver.find_element_by_id("PriceReviewedOptIn").click()

    def clickChangePaymentInfoLink(self):
        self.driver.find_element_by_link_text("Change Payment info").click()

    def clickContinueShoppingButton(self):
        self.driver.find_element_by_link_text('Continue Shopping').click()

    def checkErrorMessagePresent(self):
        error = self.driver.find_element_by_id("quantity_error").is_displayed()
        return error

    def checkEditButtonIsPresent(self):
        state = self.driver.find_element_by_link_text("Edit").is_displayed()
        return state

    #### the methods - helpers:

    def checkCheckoutButton(self):
        elem = self.driver.find_element_by_link_text("Checkout").is_displayed()
        return elem

    def checkRemoveFromCartButton(self):
        elem = self.driver.find_element_by_id('remove-item-submit').is_displayed()
        return elem
