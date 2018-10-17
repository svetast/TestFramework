import time

from selenium.webdriver.support.select import Select

from PageObjects.NavigationMenuPage import NavigationMenuPage
from HelperTestBase import HelperTestBase


class RegistrationPage5(NavigationMenuPage):
    def RegistrationPage5(self):
        driver = self.driver
        driver.get(self.base_url)

    ######## Page 5  Payment Information   ###########################
    def fillForm5(self,
                  accountType,
                  cardNumber=None,
                  cvv=None,
                  month=None,
                  year=None):
        time.sleep(15)
        ##select Acc Type
        select = Select(self.driver.find_element_by_id('AccountType'))
        select.select_by_value(accountType)

        ##fill Bank Card Number:
        self.driver.find_element_by_id('DebitCreditCardNumber').send_keys(cardNumber)

        ### fill CVV code
        self.driver.find_element_by_id('CVV2').send_keys(cvv)

        ### select Expiration Month
        select = Select(self.driver.find_element_by_id('ExpirationMonth'))
        select.select_by_visible_text(month)

        ### select Expiration Year
        select = Select(self.driver.find_element_by_id('ExpirationYear'))
        select.select_by_visible_text(year)

        ### select Certify
        self.driver.find_element_by_xpath('//*[@id="lto-page"]/div[8]/label/span').click()
        # time.sleep(3)

        ### select Agree(self):
        self.driver.find_element_by_xpath('//*[@id="lto-page"]/div[9]/label/span').click()
        # time.sleep(3)

        ### click on NEXT button

        HelperTestBase.waitNextButton(self)
        self.driver.find_element_by_link_text("Next").click()

        ############# Registration Success !!!   ######################

    def checkContinueButton(self):
        element = self.driver.find_element_by_xpath("//button[@]").is_displayed()
        return element

    def clickContinueButton(self):
        self.driver.find_element_by_xpath('//button[text()="Continue"]').click()

    ############# Registration Un Success !!!   ######################

    def checkError(self):
        error = self.driver.find_element_by_id("lblMessage").is_displayed()
        return error

    def getError(self):
        error = self.driver.find_element_by_id("lblMessage").text
        return error

    def clickHomeButton(self):
        self.driver.find_element_by_link_text("Home").click()
        time.sleep(3)
