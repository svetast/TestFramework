import time

from HelperTestBase import HelperTestBase



class LocationPage(HelperTestBase):

    def LocationPage(self):
        driver = self.driver
        driver.get(self.base_url)


    def closeLocation(self):
        self.driver.find_element_by_xpath("//a[@class='fancybox-item fancybox-close']").click()
        time.sleep(2)


    def fillForm(self, firstName=None, lastName=None, email=None, subject=None, message=None):
        self.driver.find_element_by_id("contactFirstName").send_keys(firstName)
        self.driver.find_element_by_id("contactLastName").send_keys(lastName)
        self.driver.find_element_by_id("contactEmail").send_keys(email)
        self.driver.find_element_by_id("contactSubject").send_keys(subject)
        self.driver.find_element_by_id("contactMessage").send_keys(message)




