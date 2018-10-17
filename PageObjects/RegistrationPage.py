import time

from selenium.webdriver.support.select import Select


from PageObjects.NavigationMenuPage import NavigationMenuPage





class RegistrationPage(NavigationMenuPage):
    def RegistrationPage1(self):
        driver = self.driver
        driver.get(self.base_url)

################## Page 1 Create Account  #########################

    def fillEmailAddress(self, email=None):
        self.driver.find_element_by_id("signup_email").send_keys(email)

    def fillConfirmEmailAddress(self, email=None):
        self.driver.find_element_by_id("signup_email_confirmation").send_keys(email)

    def fillUsername(self, username=None):
        self.driver.find_element_by_id("signup_username").send_keys(username)

    def fillCreatePassword(self, password=None):
        self.driver.find_element_by_id("signup_password").send_keys(password)

    def fillReTypePassword(self, passwordConfirm=None):
        self.driver.find_element_by_id("signup_verify").send_keys(passwordConfirm)

    def selectQuestion(self):
        select = Select(self.driver.find_element_by_id("signup_security_question"))
        select.select_by_visible_text("What is your mother's maiden name?")

    def fillSecurityAnswer(self, answer=None):
        self.driver.find_element_by_id('signup_security_answer').send_keys(answer)


    def fillZipCode(self, zipcode=None):
        self.driver.find_element_by_id('PostalCode').clear()
        self.driver.find_element_by_id('PostalCode').send_keys(zipcode)

    def selectTermsRadiobutton(self):
        self.driver.find_element_by_xpath("//*[@id='step1']/div/div[10]/label/span").click()

    def clickNext(self):
        self.driver.find_element_by_link_text("Next").click()
        time.sleep(3)

        ################## Page 2 Contact Information  #########################




    def fillFirstName(self, firstName=None):
       self.driver.find_element_by_id('FirstName').send_keys(firstName)

    def fillLastName(self, lastName=None):
       self.driver.find_element_by_id('LastName').send_keys(lastName)

    def fillAddress(self, address=None):
       self.driver.find_element_by_id('StreetAddress').send_keys(address)

    def fillMobilePhone(self, phone=None):
       self.driver.find_element_by_id('MobilePhoneNumber').send_keys(phone)

    def selectIwantToReceiveAlerts(self):
        self.driver.find_element_by_xpath("//span[@class='custom-checkbox-bg']").click()

  ################## Page 3 Employment Information   #########################

    def fillEmployerName(self, employerName=None):
       self.driver.find_element_by_id('EmployerName').send_keys(employerName)


    def fillEmplPhone(self, empPhone=None):
         self.driver.find_element_by_id('EmployerPhoneNumber').send_keys(empPhone)

    def selectPayFrequency(self):
        select = Select(self.driver.find_element_by_id('PayFrequency'))
        select.select_by_visible_text("Weekly")

    def selectNextPayrollDate(self):
        select = Select(self.driver.find_element_by_id('NextPayDate_Month'))
        select.select_by_value("5")

    def selectNextPayDateDay(self):
        select = Select(self.driver.find_element_by_id('NextPayDate_Day'))
        select.select_by_value("10")

    def fillIncome(self, income = None):
        self.driver.find_element_by_id('Income').send_keys(income)

    def fillOtherIncome(self, ohterIncome = None):
        self.driver.find_element_by_id('OtherIncomeSource').send_keys(ohterIncome)


    def selectNo(self):
        self.driver.find_element_by_xpath("//*[@id='lto-page']/div[12]/div/div[1]/div[2]/label/span").click()




################## Page 4 Personal Information   #########################

    def fillSocialSecurityNumber(self, ssn=None):
        self.driver.find_element_by_id('SocialSecurityNumber').send_keys(ssn)

    def fillDriverLicenseNumber(self, driverLic=None):
        self.driver.find_element_by_id('DriversLicenseNumber').send_keys(driverLic)

    def selectDriverLicenseState(self):
        select = Select(self.driver.find_element_by_id('StateOfIssue'))
        select.select_by_value("AZ")


    def selectAgeIndicator(self):
        self.driver.find_element_by_xpath('//*[@id="lto-page"]/div[4]/div[1]/div/div/div[4]/label/span').click()

    def selectAgeIndicatorUnder18(self):
        self.driver.find_element_by_xpath('//*[@id="lto-page"]/div[4]/div[1]/div/div/div[1]/label/span').click()


    ########3 Page 5     Payment Information   ###########################

    def selectAccType(self, accountType=None):
        select = Select(self.driver.find_element_by_id('AccountType'))
        select.select_by_value(accountType)

    def fillBankCardNumber(self, cardNumber=None):
        self.driver.find_element_by_id('DebitCreditCardNumber').send_keys(cardNumber)

    def fillCVVcode(self, cvv=None):
         self.driver.find_element_by_id('CVV2').send_keys(cvv)


    def selectExpirationMonth(self, month=None):
        select = Select(self.driver.find_element_by_id('ExpirationMonth'))
        select.select_by_visible_text(month)


    def selectExpirationYear(self, year=None):
        select = Select(self.driver.find_element_by_id('ExpirationYear'))
        select.select_by_visible_text(year)

    def selectCertify(self):
            self.driver.find_element_by_xpath('//*[@id="lto-page"]/div[8]/label/span').click()

    def selectAgree(self):
            self.driver.find_element_by_xpath('//*[@id="lto-page"]/div[9]/label/span').click()


    ############# Registration Success !!!   ######################


    def checkContinue(self):
            element = self.driver.find_element_by_xpath("//button[@]").is_displayed()
            return element






