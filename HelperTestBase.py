import time
import unittest
from telnetlib import EC

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options


class HelperTestBase(unittest.TestCase):

    def setUp(self):

        ### to use Headless Browser:

        # chrome_options = Options()
        # chrome_options.add_argument("headless")
        # self.driver = webdriver.Chrome(chrome_options=chrome_options)


        ### to use WebBrowser :

        self.driver = webdriver.Chrome('chromedriver')
        self.driver.maximize_window()
        self.driver.implicitly_wait(60)
        PORTAL = 'mainstreet'
        self.setUpEnvironment(PORTAL)

    def setUpEnvironment(self, portal=None):




        if portal == 'mainstreet':
            self.base_url = 'https://stg.mainstreetlto.com'
            self.driver.get(self.base_url)

        if portal == 'ltodemo':
            self.base_url = "http://www.ltodemo.com"
            self.driver.get(self.base_url)


        if portal == 'smokeLTO':
            self.base_url = 'https://smoke.ltomall.com'
            self.driver.get(self.base_url)


        if portal == 'mainstreet':
            self.driver.find_element_by_id("zipcode").send_keys('59019')

        if portal == 'ltodemo':
            self.driver.find_element_by_id("zipcode").send_keys('33131')

        if portal == 'smokeLTO':
            self.driver.find_element_by_id("zipcode").send_keys('33131')
        self.driver.find_element_by_id("zipcode").send_keys(Keys.ENTER)
        time.sleep(5)
        self.driver.find_element_by_xpath("//a[@class='fancybox-item fancybox-close']").click()

    def checkZipcodeValidation(self, zipcode=None):
        element_present = EC.element_to_be_clickable((By.ID, "zip-code-popup-opener"))
        WebDriverWait(self.driver, 10).until(element_present)
        self.driver.find_element_by_id("zip-code-popup-opener").click()
        time.sleep(3)
        self.driver.find_element_by_id("zipcode").send_keys(zipcode)
        self.driver.find_element_by_id("zipcode").send_keys(Keys.ENTER)

    def clickChangeLocation(self):
        element_present = EC.element_to_be_clickable((By.ID, "zip-code-popup-opener"))
        WebDriverWait(self.driver, 150).until(element_present)
        self.driver.find_element_by_id("zip-code-popup-opener").click()

    def closeZip(self):
        element_present = EC.visibility_of_element_located((By.XPATH, "//a[@class='fancybox-item fancybox-close']"))
        WebDriverWait(self.driver, 150).until(element_present)
        self.driver.find_element_by_xpath("//a[@class='fancybox-item fancybox-close']").click()

    def waitLogOutLink(self):
        element_present = EC.visibility_of_element_located((By.XPATH, "//a[@class='btn-log-out mobile-hidden']"))
        WebDriverWait(self.driver, 100).until(element_present)

    def waitChangeLocation(self):
        element_present = EC.element_to_be_clickable((By.ID, "zip-code-popup-opener"))
        WebDriverWait(self.driver, 150).until(element_present)

    def getTitle(self):
        title = self.driver.title
        return title

    def getURL(self):
        url = self.driver.current_url
        return url

    def checkPresent(self, locator=None):
        element = self.driver.find_element_by_id(locator).is_displayed()
        return element

    def checkPresentElem(self, locator=None):
        element = self.driver.find_element_by_class_name(locator).is_displayed()
        return element

    def tearDown(self):
        self.driver.quit()

    ###### Utills - the methods for Wait  ##########

    ### Wait Next button on all Registration forms

    def waitNextButton(self):
        element_present = EC.element_to_be_clickable((By.LINK_TEXT, "Next"))
        WebDriverWait(self.driver, 100).until(element_present)

        ### Wait Next button on all Registration forms

    def waitHomeButton(self):
        element_present = EC.element_to_be_clickable((By.LINK_TEXT, "Home"))
        WebDriverWait(self.driver, 100).until(element_present)

    def openSmartTires(self):
        self.driver.find_element_by_id("zipcode").send_keys('89104')
        self.driver.find_element_by_id("zipcode").send_keys(Keys.ENTER)
        time.sleep(3)
        self.driver.refresh()

    def checkElementExist(self):
        state = self.driver.find_elements_by_xpath('//span[text()="Inventory"]')
        return state


if __name__ == "__main__":
    unittest.main()
