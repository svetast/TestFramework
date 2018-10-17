from telnetlib import EC

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from PageObjects.LoginPage import LoginPage


class NavResultsPage(LoginPage):
    def NavResultsPage(self):
        driver = self.driver
        driver.get(self.base_url)




    def checkApplyButton(self):
        element = self.driver.find_element_by_link_text("Create Account").is_displayed()
        return element


    def waitCreateAccLink(self):
        element_present = EC.visibility_of_element_located((By.LINK_TEXT, "Create Account"))
        WebDriverWait(self.driver, 80).until(element_present)

    def checkCreateAccButton(self):
        element = self.driver.find_element_by_link_text("Create Account").is_displayed()
        return element

    def checkContentHowItsWorkPage(self):
        elem = self.driver.find_element_by_xpath("//div[@class='content-page how-it-work-page']").is_displayed()
        return elem
