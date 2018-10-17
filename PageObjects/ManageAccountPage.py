import time

from selenium.webdriver.common.keys import Keys

from PageObjects.HomePage import HomePage


class ManageAccountPage(HomePage):
    def ManageAccountPage(self):
        driver = self.driver
        driver.get(self.base_url)

    def clickOrderHistory(self):
        self.driver.find_element_by_link_text("Order History").click()

    def clickTrackShipping(self):
        self.driver.find_element_by_link_text("Track Shipping").click()

    def clickAccountSettings(self):
        self.driver.find_element_by_link_text("Account Settings").click()

    def clickAddressAndPhone(self):
        self.driver.find_element_by_link_text("Address and Phone").click()

    def clickEmploymentInformation(self):
        self.driver.find_element_by_link_text("Employment Information").click()

    def clickPersonalInformation(self):
        self.driver.find_element_by_link_text("Personal Information").click()

    def clickAccountSummary(self):
        self.driver.find_element_by_link_text("Account Summary").click()

    def clickChangePaymentMethod(self):
        self.driver.find_element_by_link_text("Change Payment Method").click()

    def clickShopNow(self):
        self.driver.find_element_by_link_text("Shop Now!").click()

    def clickToGoTo(self):
        self.driver.find_element_by_partial_link_text("Click Here to go to").click()

    #### Account Settings section #############

    def changePassword(self, currentPW=None, newPW=None, reTypePW=None):
        self.driver.find_element_by_id("reset_oldpassword").send_keys(currentPW)
        self.driver.find_element_by_id("reset_password").send_keys(newPW)
        self.driver.find_element_by_id("reset_verify").send_keys(reTypePW)
        self.driver.find_element_by_id("reset_verify").send_keys(Keys.ENTER)

    def changeEmail(self, newEmailAddress=None, newEmailAddressConfirmation=None):
        self.driver.find_element_by_id("NewEmailAddress").send_keys(newEmailAddress)
        self.driver.find_element_by_id("NewEmailAddressConfirmation").send_keys(newEmailAddressConfirmation)
        self.driver.find_element_by_id("NewEmailAddressConfirmation").send_keys(Keys.ENTER)

    def checkNewPasswordFieldPresent(self):
        state = self.driver.find_element_by_id("reset_password").is_displayed()
        return state

    def checkNewEmailAddressFielfPresent(self):
        state = self.driver.find_element_by_id("NewEmailAddress").is_displayed()
        return state

    #### Addresses and phone section #############

    def checkAddressFieldPresent(self):
        state = self.driver.find_element_by_id("StreetAddress1").is_displayed()
        return state

    def checkZipCodeFielfPresent(self):
        state = self.driver.find_element_by_id("PostalCode").is_displayed()
        return state

    def checkMobilePhoneFielfPresent(self):
        state = self.driver.find_element_by_id("PhoneNumber").is_displayed()
        return state

    #### Employment Information section #############

    def checkSaveButtonPresent(self):
        state = self.driver.find_element_by_id("btnSave").is_displayed()
        return state

    def checkCancelButtonfPresent(self):
        state = self.driver.find_element_by_id("btnCancel").is_displayed()
        return state

    #### Personal Information section #############

    def checkSaveButton_Present(self):
        state = self.driver.find_element_by_id("btnSave").is_displayed()
        return state

    def checkCancelButton_Present(self):
        state = self.driver.find_element_by_id("btnCancel").is_displayed()
        return state

    def checkSSNPresent(self):
        state = self.driver.find_element_by_id("SocialSecurityNumber").is_displayed()
        return state

    def checkDriverLisensePresent(self):
        state = self.driver.find_element_by_id("DriversLicenseNumber").is_displayed()
        return state

    def checkDriverLisenseStatePresent(self):
        state = self.driver.find_element_by_id("StateOfIssue").is_displayed()
        return state
