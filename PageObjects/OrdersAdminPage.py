import time

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select

from HelperTestBase import HelperTestBase


class OrdersAdminPage(HelperTestBase):
    def OrdersAdminPage(self):
        driver = self.driver
        driver.get(self.base_url)

    def findOrdersByLastname(self, lastName=None):
        self.driver.find_element_by_id("txtlastname").send_keys(lastName)
        self.driver.find_element_by_id("txtlastname").send_keys(Keys.ENTER)

    def clickManageOrder(self):
        links = self.driver.find_elements_by_partial_link_text("MANAGE ORDER")
        links[0].click()
        time.sleep(2)

    def clickUpdateOrderStatus(self):
        self.driver.find_element_by_id("ctl00_ctl00_uxMainContent_uxMainContent_ChangeStatus").click()
        time.sleep(4)

    def clickCancelOrder(self):
        select = Select(self.driver.find_element_by_id("ctl00_ctl00_uxMainContent_uxMainContent_ListOrderStatus"))
        select.select_by_visible_text("CANCELLED")
        # self.driver.refresh()
        self.driver.find_element_by_id('ctl00_ctl00_uxMainContent_uxMainContent_UpdateOrderStatus').click()
        time.sleep(3)
        self.driver.find_element_by_id('ctl00_ctl00_uxMainContent_uxMainContent_txtReason').send_keys('test')
        self.driver.find_element_by_id('ctl00_ctl00_uxMainContent_uxMainContent_UpdateOrderStatus').click()
        time.sleep(3)

    def clickBackToOrderList(self):
        self.driver.find_element_by_id('ctl00_ctl00_uxMainContent_uxMainContent_List').click()
        time.sleep(3)

    def clickReSendAgreement(self):
        self.driver.find_element_by_xpath("//input[@value ='Resend Agreement']").click()
        time.sleep(3)
