import time

from PageObjects.LoginPage import LoginPage


class ErrorMessagesPage(LoginPage):

    def ErrorMessagesPage(self):
        driver = self.driver
        driver.get(self.base_url)

    def checkErrorMessage(self):
        error = self.driver.find_element_by_id("lblMessage").is_displayed()
        return error

    def getErrorMessage(self):
        textError = self.driver.find_element_by_id("lblMessage").text
        return textError
