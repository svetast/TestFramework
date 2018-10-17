import time
from telnetlib import EC

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from PageObjects.LoginPage import LoginPage


class ForgotPasswordPage(LoginPage):
    def ForgotPasswordPage(self):
        driver = self.driver
        driver.get(self.base_url)

    def fillForgotPasswordForm(self, userName=None, email=None):
        self.driver.find_element_by_id("forgot_username").send_keys(userName)
        self.driver.find_element_by_id("forgot_email").send_keys(email)
        time.sleep(3)
        self.driver.find_element_by_xpath("//*[@id='forgot_question_button']/div/button").click()

    def fillSequreAnswer(self, nameValid=None):
        self.driver.find_element_by_xpath("//*[@id='forgot_reset_button']/div/button").click()

    def submitForgotPasswordForm(self, userName=None, email=None, nameValid=None):
        self.driver.find_element_by_xpath("//*[@id='forgot_reset_button']/div/button").click()

    def fillForgotUserNameForm(self, zip=None, email=None):
        self.driver.find_element_by_id("forgot_ZIP2").send_keys(zip)
        self.driver.find_element_by_id("forgot_email2").send_keys(email)
        self.driver.find_element_by_xpath('//*[@id="forgot_question_button2"]/div/button').click()

    def waitForgotPW(self):
        element_present = EC.visibility_of_element_located((By.ID, "forgot-form"))
        WebDriverWait(self.driver, 80).until(element_present)

    def getErrorMessage(self):
        error = self.driver.find_element_by_id("reset-error-message").text
        return error
