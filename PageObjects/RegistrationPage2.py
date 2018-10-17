import time

from HelperTestBase import HelperTestBase

from PageObjects.NavigationMenuPage import NavigationMenuPage


class RegistrationPage2(NavigationMenuPage):
    def RegistrationPage2(self):
        driver = self.driver
        driver.get(self.base_url)

    ################## Page 2 Contact Information  #########################
    def fillForm2(self,
                  firstName=None,
                  lastName=None,
                  address=None,
                  phone=None,
                  portal=None):

        self.driver.find_element_by_id('FirstName').send_keys(firstName)
        self.driver.find_element_by_id('LastName').send_keys(lastName)

        if portal == 'smarttires':
            self.driver.find_element_by_id("StreetAddress").send_keys('15160 Sunflower Drive')

        if portal == 'weelzontime':
            self.driver.find_element_by_id("StreetAddress").send_keys('7600 W. Roosevelt Rd')

        if portal == 'mainstreet':
            self.driver.find_element_by_id("StreetAddress").send_keys('564 Countryman Creek Rd')
            # self.driver.find_element_by_id("StreetAddress").send_keys('1828 Gregg St')

        if portal == 'ltodemo':
            self.driver.find_element_by_id("StreetAddress").send_keys('788 Brickell Plaza')

        if portal == 'patriottireleasing':
            self.driver.find_element_by_id("StreetAddress").send_keys('38613 Benro DR')
        # self.driver.find_element_by_id("StreetAddress").send_keys('2711 E. Sahara Ave')

        if portal == 'toolcabin':
            self.driver.find_element_by_id("StreetAddress").send_keys('9518 Therrell Dr')

        if portal == 'smokeLTO':
            self.driver.find_element_by_id("StreetAddress").send_keys('100 Chopin Plaza')
        # self.driver.find_element_by_id("StreetAddress").send_keys('15160 Sunflower Drive')
        # self.driver.find_element_by_id("StreetAddress").send_keys('2711 E. Sahara Ave')
        # self.driver.find_element_by_id("StreetAddress").send_keys('999 Brickell Bay Dr 1506')
        # self.driver.find_element_by_id("StreetAddress").send_keys('777 Brickell Avenue')
        # self.driver.find_element_by_id("StreetAddress").send_keys('394 Lincoln Highway')

        self.driver.find_element_by_id('MobilePhoneNumber').send_keys(phone)
        self.driver.find_element_by_xpath("//span[@class='custom-checkbox-bg']").click()
        HelperTestBase.waitNextButton(self)
        self.driver.find_element_by_link_text("Next").click()

    ###### Check states (in these states LTO business is banned)=> zips should NOT be accepted during Registration- WI, MN, NC, NJ:

    def fillFormDontAccessStates(self,
                                 firstName=None,
                                 lastName=None,
                                 address=None,
                                 phone=None,
                                 portal=None):

        self.driver.find_element_by_id('FirstName').send_keys(firstName)
        self.driver.find_element_by_id('LastName').send_keys(lastName)

        if portal == 'smarttires':
            self.driver.find_element_by_id("StreetAddress").send_keys('15160 Sunflower Drive')

        if portal == 'weelzontime':
            self.driver.find_element_by_id("StreetAddress").send_keys('7600 W. Roosevelt Rd')

        if portal == 'mainstreet':
            self.driver.find_element_by_id("StreetAddress").send_keys('47-1 Bissett Pl Metuchen')

        if portal == 'patriottireleasing':
            # self.driver.find_element_by_id("StreetAddress").send_keys('38613 Benro DR')
            self.driver.find_element_by_id("StreetAddress").send_keys('2711 E. Sahara Ave')

        if portal == 'ltodemo':
            self.driver.find_element_by_id("StreetAddress").send_keys('2711 E. Sahara Ave')

        if portal == 'toolcabin':
            self.driver.find_element_by_id("StreetAddress").send_keys('9518 Therrell Dr')

        # if portal == 'smokeLTO':
        # self.driver.find_element_by_id("StreetAddress").send_keys('15160 Sunflower Drive')
        # self.driver.find_element_by_id("StreetAddress").send_keys('2711 E. Sahara Ave')
        # self.driver.find_element_by_id("StreetAddress").send_keys('999 Brickell Bay Dr 1506')
        # self.driver.find_element_by_id("StreetAddress").send_keys('1640 Airport Rd')
        # self.driver.find_element_by_id("StreetAddress").send_keys('394 Lincoln Highway')

        self.driver.find_element_by_id('MobilePhoneNumber').send_keys(phone)
        self.driver.find_element_by_xpath("//span[@class='custom-checkbox-bg']").click()
        HelperTestBase.waitNextButton(self)
        self.driver.find_element_by_link_text("Next").click()
