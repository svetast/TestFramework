import time



from PageObjects.LoginPage import LoginPage



class ForgotUsernamePage(LoginPage):
    def ForgotUsernamedPage(self):
        driver = self.driver
        driver.get(self.base_url)



    def fillForgotUsernameForm(self, userName=None, email=None, nameValid=None):
        self.driver.find_element_by_id("forgot_ZIP2").send_keys(userName)
        self.driver.find_element_by_id("forgot_email2").send_keys(email)
        self.driver.find_element_by_xpath("//*[@id='forgot_question_button2']/div/button").click()
        time.sleep(2)
        self.driver.find_element_by_id("forgot_security").send_keys(nameValid)


    def submitForgotUsernameForm(self):
        self.driver.find_element_by_xpath("//*[@id='forgot_reset_button2']/div/button").click()
