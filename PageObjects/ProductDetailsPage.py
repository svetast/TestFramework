import time

from PageObjects.HomePage import HomePage


class ProductDetailsPage(HomePage):

    def ProductDetailsPage(self):
        driver = self.driver
        driver.get(self.base_url)

    def clickOnDetailsButton(self):
        button = self.driver.find_elements_by_link_text("Details")
        button[0].click()

    def setQTY(self, qty=None):
        self.driver.find_element_by_id("Quantity").clear()
        self.driver.find_element_by_id("Quantity").send_keys(qty)

    def clickAddToCart(self, qty=None):
        self.driver.find_element_by_id("addToCart").click()

    def closeLight(self):
        self.driver.find_element_by_xpath("//a[@title='Close']").click()

    def clickViewCart(self):
        self.driver.find_element_by_link_text('View cart').click()

    def clickContinueShoppingButton(self):
        butt = self.driver.find_elements_by_css_selector("#lightbox > ul > li:nth-child(2)")
        butt[1].click()

    def checkQTY(self):
        element = self.driver.find_element_by_id("Quantity").is_displayed()
        return element

    def checkAddToCart(self):
        element = self.driver.find_element_by_id('addToCart').is_displayed()
        return element

    def checkError(self):
        element = self.driver.find_element_by_id('quantity_error').is_displayed()
        return element

    ###### Check Lightbox is present:     ##################

    def checkLightbox(self):
        element = self.driver.find_element_by_id('lightbox').is_displayed()
        return element

    def checkViewCartButton(self):
        element = self.driver.find_element_by_link_text('View cart').is_displayed()
        return element

    def checkContinueShoppingButton(self):
        element = self.driver.find_element_by_xpath('//*[@id="lightbox"]/ul/li[2]/button').is_displayed()
        return element

    def checkStatusInStock(self):
        element = self.driver.find_element_by_id('product_status').text
        return element
