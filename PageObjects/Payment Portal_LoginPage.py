from PageObjects.LoginPage import LoginPage


class PaymentPortal_LoginPage(LoginPage):
    def PaymentPortal_LoginPage(self):
        driver = self.driver
        driver.get(self.base_url)







