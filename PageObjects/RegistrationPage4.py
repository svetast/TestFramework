import time

from selenium.webdriver.support.select import Select

from PageObjects.NavigationMenuPage import NavigationMenuPage
from HelperTestBase import HelperTestBase


class RegistrationPage4(NavigationMenuPage):
    def RegistrationPage4(self):
        driver = self.driver
        driver.get(self.base_url)

    ############# Page 4 Personal Information   #########################

    def fillForm4(self,
                  ssn=None,
                  driverLic=None,
                  state=None
                  ):
        ### fill Social Security Number
        self.driver.find_element_by_id('SocialSecurityNumber').send_keys(ssn)

        ### fill Driver License Number
        self.driver.find_element_by_id('DriversLicenseNumber').send_keys(driverLic)

        ##select Driver License State(self):
        select = Select(self.driver.find_element_by_id('StateOfIssue'))
        select.select_by_value(state)

        ####select Valid Age Indicator(self):
        self.driver.find_element_by_xpath('//*[@id="lto-page"]/div[4]/div[1]/div/div/div[4]/label/span').click()

        # ####select Radiobuttons FOR DEMO ONLY :
        # self.driver.find_element_by_xpath('//*[@id="lto-page"]/div[5]/label/span').click()
        #
        # self.driver.find_element_by_xpath('//*[@id="lto-page"]/div[6]/label/span').click()
        # time.sleep(2)


        ### click on NEXT button
        # HelperTestBase.waitNextButton(self)
        self.driver.find_element_by_link_text("Next").click()
        time.sleep(2)

    def fillForm4_AgeLimitation(self,
                                ssn=None,
                                driverLic=None,
                                state=None
                                ):
        ### fill Social Security Number
        self.driver.find_element_by_id('SocialSecurityNumber').send_keys(ssn)

        ### fill Driver License Number
        self.driver.find_element_by_id('DriversLicenseNumber').send_keys(driverLic)

        ##select Driver License State(self):
        select = Select(self.driver.find_element_by_id('StateOfIssue'))
        select.select_by_value(state)

        ####select Invalid Age Indicator = > Age Limitation Status :
        self.driver.find_element_by_xpath('//*[@id="lto-page"]/div[4]/div[1]/div/div/div[1]/label/span').click()

        # ####select Radiobuttons:
        # self.driver.find_element_by_xpath('//*[@id="lto-page"]/div[5]/label/span').click()
        #
        # self.driver.find_element_by_xpath('//*[@id="lto-page"]/div[6]/label/span').click()
        # time.sleep(2)

        ### click on NEXT button
        HelperTestBase.waitNextButton(self)
        self.driver.find_element_by_link_text("Next").click()

    ####### check field  is present   #########

    def checkSSN_Present(self):
        element = self.driver.find_element_by_id('SocialSecurityNumber').is_displayed()
        return element

    def checkCardNumberPresent(self):
        element = self.driver.find_element_by_id('DebitCreditCardNumber').is_displayed()
        return element
