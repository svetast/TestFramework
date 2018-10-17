import time

from PageObjects.NavigationMenuPage import NavigationMenuPage



class UnSubscribePage(NavigationMenuPage):

    def UnSubscribePage(self):
        driver = self.driver
        driver.get(self.base_url)


    def clickRemove(self):
        self.driver.find_element_by_link_text("Remove me from future mailings.").click()
        time.sleep(3)



    def fillUnSubscribeForm(self, email=None):
        self.driver.find_element_by_id("Email").send_keys(email)


    def clickVisitHomePageLink(self):
        self.driver.find_element_by_link_text('Visit our Home page').click()
        time.sleep(3)

