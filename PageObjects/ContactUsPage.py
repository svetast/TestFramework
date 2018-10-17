import time

from PageObjects.NavigationMenuPage import NavigationMenuPage



class ContactUsPage(NavigationMenuPage):

    def ContactUsPage(self):
        driver = self.driver
        driver.get(self.base_url)


    def clickSendButton(self):
        self.driver.find_element_by_xpath("//button[@class='button theme-bg']").click()
        time.sleep(2)


    def fillForm(self, firstName=None, lastName=None, email=None, subject=None, message=None):
        self.driver.find_element_by_id("contactFirstName").send_keys(firstName)
        self.driver.find_element_by_id("contactLastName").send_keys(lastName)
        self.driver.find_element_by_id("contactEmail").send_keys(email)
        self.driver.find_element_by_id("contactSubject").send_keys(subject)
        self.driver.find_element_by_id("contactMessage").send_keys(message)




