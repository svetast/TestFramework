import time

from selenium.webdriver.support.select import Select
from HelperTestBase import HelperTestBase


from PageObjects.NavigationMenuPage import NavigationMenuPage





class RegistrationPage3(NavigationMenuPage):
    def RegistrationPage3(self):
        driver = self.driver
        driver.get(self.base_url)

  ################## Page 3 Employment Information   #########################

    def fillForm3(self, employerName=None,
                  empPhone=None,
                  income=None,
                  ohterIncome=None):

        ### fillEmployerName
        self.driver.find_element_by_id('EmployerName').send_keys(employerName)
        ###fillEmplPhone:
        self.driver.find_element_by_id('EmployerPhoneNumber').send_keys(empPhone)

        ### selectPayFrequency
        select = Select(self.driver.find_element_by_id('PayFrequency'))
        select.select_by_visible_text("Weekly")

        ### selectNextPayrollDate
        select = Select(self.driver.find_element_by_id('NextPayDate_Month'))
        select.select_by_value("10")

        ### selectNextPayDateDay
        select = Select(self.driver.find_element_by_id('NextPayDate_Day'))
        select.select_by_value("29")

        ###fillIncome
        self.driver.find_element_by_id('Income').send_keys(income)

        ###fillOtherIncome
        self.driver.find_element_by_id('OtherIncomeSource').send_keys(ohterIncome)

        ### select No
        self.driver.find_element_by_xpath("//*[@id='lto-page']/div[12]/div/div[1]/div[2]/label/span").click()

        ### click on NEXT button
        HelperTestBase.waitNextButton(self)
        self.driver.find_element_by_link_text("Next").click()

        time.sleep(2)
