from HelperTestBase import HelperTestBase






class SearchPage(HelperTestBase):
    def SearchPage(self):
        driver = self.driver
        driver.get(self.base_url)

    def clickAcc(self):
        self.driver.find_element_by_class_name("opener account-btn").click()

    def closeWindow(self):
        self.driver.find_element_by_xpath("//a[@title='Close']").click()









