import time



from PageObjects.LoginPage import LoginPage


class NavigationMenuPage(LoginPage):
    def NavigationMenuPage(self):
        driver = self.driver
        driver.get(self.base_url)


####### HEADER:

    def clickHowItWorks(self):
        self.driver.find_element_by_xpath("//a[@title='How It Works']").click()
        time.sleep(3)

    def clickFAQ(self):
        self.driver.find_element_by_xpath("//a[@title='FAQ']").click()
        time.sleep(3)

    def clickAboutUS(self):
        self.driver.find_element_by_xpath("//a[@title='About Us']").click()
        time.sleep(3)

    def clickContactUS(self):
        self.driver.find_element_by_xpath("//a[@title='Contact Us']").click()
        time.sleep(3)

    def clickMakePayment(self):
        self.driver.find_element_by_xpath("//a[@title='Make A Payment']").click()
        time.sleep(3)

        ####### FOOTER:

    def clickHowItWorksFooter(self):
        self.driver.find_element_by_xpath('//*[@id="footer"]/div[1]/ul/li[1]/a').click()
        time.sleep(3)

    def clickFAQFooter(self):
        self.driver.find_element_by_xpath('//*[@id="footer"]/div[1]/ul/li[2]/a').click()
        time.sleep(3)

    def clickContactUS_Footer(self):
        self.driver.find_element_by_xpath('//*[@id="footer"]/div[1]/ul/li[3]/a').click()
        time.sleep(3)

    def clickPrivacyPolicy(self):
        self.driver.find_element_by_xpath('//*[@id="footer"]/div[1]/ul/li[4]/a').click()
        time.sleep(3)

    def clickTerms(self):
        # self.driver.find_element_by_xpath('//*[@id="footer"]/div[1]/ul/li[5]/a').click()
        self.driver.find_element_by_link_text('Terms of Service').click()
        time.sleep(3)


    def clickUnsubscribe(self):
        self.driver.find_element_by_link_text('Unsubscribe').click()
        time.sleep(3)

    def goToHomePage(self):
        self.driver.get(self.base_url)
