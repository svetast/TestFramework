import time

from selenium.webdriver.common.keys import Keys

from PageObjects.HomePage import HomePage
from HelperTestBase import HelperTestBase


class VehiclenInfoPage(HomePage):
    def VehiclenInfoPage(self):
        driver = self.driver
        driver.get(self.base_url)

    def fiilForm(self, make=None,
                 vehicleYear=None,
                 model=None,
                 vin=None,
                 mileage=None,
                 licenseTag=None,
                 state=None,
                 partyPhone=None):
        input = self.driver.find_elements_by_xpath("//input[@type='text']")
        input[0].clear()
        input[0].send_keys(make)
        input[1].clear()
        input[1].send_keys(vehicleYear)
        input[2].clear()
        input[2].send_keys(model)
        input[3].clear()
        input[3].send_keys(vin)
        input[4].clear()
        input[4].send_keys(mileage)
        input[5].clear()
        input[5].send_keys(licenseTag)
        input[6].clear()
        input[6].send_keys(state)
        input[8].clear()
        input[8].send_keys(partyPhone)
        self.driver.find_element_by_link_text("Next").click()
