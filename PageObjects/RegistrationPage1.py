import time
from telnetlib import EC

from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from HelperTestBase import HelperTestBase

from PageObjects.NavigationMenuPage import NavigationMenuPage


class RegistrationPage1(NavigationMenuPage):
    def RegistrationPage1(self):
        driver = self.driver
        driver.get(self.base_url)

    ################## Page 1 Create Account  #########################

    def fillForm1(self, email=None,
                  username=None,
                  password=None,
                  passwordConfirm=None,
                  answer=None,
                  zipcode=None):
        time.sleep(2)

        self.driver.find_element_by_id("signup_email").send_keys(email)

        self.driver.find_element_by_id("signup_email_confirmation").send_keys(email)

        self.driver.find_element_by_id("signup_username").send_keys(username)

        self.driver.find_element_by_id("signup_password").send_keys(password)

        self.driver.find_element_by_id("signup_verify").send_keys(passwordConfirm)

        select = Select(self.driver.find_element_by_id("signup_security_question"))
        select.select_by_visible_text("What is your mother's maiden name?")

        self.driver.find_element_by_id('signup_security_answer').send_keys(answer)

        ###### DON'T fill  Zipcode field => Zipcode field has been filling outed by AUTOMATICALLY:

        # self.driver.find_element_by_id('PostalCode').clear()
        # self.driver.find_element_by_id('PostalCode').send_keys("19116")

        self.driver.find_element_by_xpath("//span[@class='custom-checkbox-bg']").click()

        HelperTestBase.waitNextButton(self)
        self.driver.find_element_by_link_text("Next").click()

    # def waitNextButton(self):
    #     element_present = EC.visibility_of_element_located((By.XPATH, "//a[@class='button theme-bg']"))
    #     WebDriverWait(self.driver, 80).until(element_present)
