import time

import pytest

from PageObjects.LoginPage import LoginPage
from HelperTestBase import HelperTestBase
from PageObjects.ContactUsPage import ContactUsPage
from PageObjects.ManageAccountPage import ManageAccountPage

from PageObjects.HomePage import HomePage


class TestManageAccount(ManageAccountPage):


    def test_checkNavigation(self):
        driver = self.driver
        driver.get(self.base_url + '/Account/Dashboard')
        text1 = self.base_url + '/account/orderhistory'
        text2 = self.base_url + '/account/ordershipping'
        text3 = self.base_url + '/account/Settings'
        text4 = self.base_url + '/account/addressbook'
        text5 = self.base_url + '/LTO/EditEmploymentInformation'
        text6 = self.base_url + '/LTO/EditPersonalInformation'
        text7 = 'Change Payment Method'
        text9 = self.base_url + '/account/dashboard'

        text10 = "Register to Make Payments"

        LoginPage.logIn(self, "svetast555", "Ss123456")

        ManageAccountPage.clickOrderHistory(self)
        time.sleep(2)
        self.assertEqual(text1, HelperTestBase.getURL(self))
        self.driver.back()

        ManageAccountPage.clickTrackShipping(self)
        time.sleep(2)
        self.assertEqual(text2, HelperTestBase.getURL(self))
        self.driver.back()

        ManageAccountPage.clickAccountSettings(self)
        time.sleep(2)
        self.assertEqual(text3, HelperTestBase.getURL(self))
        self.assertIs(True, ManageAccountPage.checkNewPasswordFieldPresent(self))
        self.assertIs(True, ManageAccountPage.checkNewEmailAddressFielfPresent(self))
        self.driver.back()
        time.sleep(3)

        ManageAccountPage.clickAddressAndPhone(self)
        time.sleep(2)
        self.assertEqual(text4, HelperTestBase.getURL(self))
        self.assertIs(True, ManageAccountPage.checkAddressFieldPresent(self))
        self.assertIs(True, ManageAccountPage.checkZipCodeFielfPresent(self))
        self.assertIs(True, ManageAccountPage.checkMobilePhoneFielfPresent(self))
        self.driver.back()
        time.sleep(2)

        ManageAccountPage.clickEmploymentInformation(self)
        time.sleep(2)
        self.assertEqual(text5, HelperTestBase.getURL(self))
        self.driver.back()
        time.sleep(2)


        ManageAccountPage.clickPersonalInformation(self)
        time.sleep(2)
        self.assertEqual(text6, HelperTestBase.getURL(self))
        self.assertIs(True, ManageAccountPage.checkSaveButton_Present(self))
        self.assertIs(True, ManageAccountPage.checkCancelButton_Present(self))
        self.assertIs(True, ManageAccountPage.checkSSNPresent(self))
        self.assertIs(True, ManageAccountPage.checkDriverLisensePresent(self))
        self.assertIs(True, ManageAccountPage.checkDriverLisenseStatePresent(self))
        self.driver.back()
        time.sleep(2)

        ManageAccountPage.clickChangePaymentMethod(self)
        time.sleep(2)
        self.assertIn(text7, self.driver.page_source)
        self.driver.back()
        time.sleep(2)

        ManageAccountPage.clickAccountSummary(self)
        time.sleep(2)
        self.assertEqual(text9, HelperTestBase.getURL(self))
        self.driver.back()
        time.sleep(2)

        ManageAccountPage.clickShopNow(self)
        time.sleep(2)
        self.assertIs(True, HomePage.checkINFOBannerPresent(self))
        self.driver.back()
        time.sleep(2)


        # #### add checking
        #
        # if self.driver.find_element_by_partial_link_text("Click Here to go to").is_displayed():
        #     ManageAccountPage.clickToGoTo(self)
        #     time.sleep(10)
        #     windows = driver.window_handles
        #     driver.switch_to.window(windows[1])
        #     self.assertIn(text10, self.driver.page_source)
        #     self.driver.back()
        #     time.sleep(2)


    # @pytest.mark.skip
    def test_changePassword(self):
        driver = self.driver
        driver.get(self.base_url + '/Account/Dashboard')
        text0 = 'Password is required.'
        text1 = 'New password is required.'
        text2 = 'Re-type new password is required.'
        text4 = 'Cannot use any of the four previous passwords.'
        text5 = 'Password must be at least 8 alphanumeric characters and contain at least one number'
        text6 = 'Password and Re-Type password do not match'
        text7 = 'Update Successful'

        LoginPage.logIn(self, "svetast999", "Ss123456")
        time.sleep(5)

        ManageAccountPage.clickAccountSettings(self)
        time.sleep(2)
        ManageAccountPage.changePassword(self, currentPW='', newPW='', reTypePW='')
        time.sleep(3)
        self.assertIn(text0, self.driver.page_source)
        self.assertIn(text1, self.driver.page_source)
        self.assertIn(text2, self.driver.page_source)
        self.driver.refresh()

        # Check validation  #######
        ManageAccountPage.changePassword(self, currentPW='Ss123456', newPW='Ss1!@#$%^&*()_+<>[]{}?',
                                         reTypePW='Ss1!@#$%^&*()_+<>?[]{}')
        time.sleep(4)
        self.assertIn(text5, self.driver.page_source)

        # Check that password shoul be consist minimum  of 8 symbols  #######
        ManageAccountPage.changePassword(self, currentPW='Ss123456', newPW='Ss12345', reTypePW='Ss12345')
        time.sleep(4)
        self.assertIn(text5, self.driver.page_source)

        # Check that User Can't use any of the four previous passwords:
        ManageAccountPage.changePassword(self, currentPW='Ss123456', newPW='Ss123456', reTypePW='Ss123456')
        time.sleep(3)
        self.assertIn(text4, self.driver.page_source)

        # Check that Password must be at least 8 alphanumeric characters and contain at least one number':
        ManageAccountPage.changePassword(self, currentPW='Ss123456', newPW='12345678', reTypePW='12345678')
        time.sleep(3)
        self.assertIn(text5, self.driver.page_source)

        # Check that Password must be at least 8 alphanumeric characters and contain at least one number':
        ManageAccountPage.changePassword(self, currentPW='Ss123456', newPW='Asdfghjk', reTypePW='Asdfghjk')
        time.sleep(3)
        self.assertIn(text5, self.driver.page_source)

        # Check that Password and Re-Type password should be match:
        ManageAccountPage.changePassword(self, currentPW='Ss123456', newPW='Ss123456', reTypePW='Ff123456')
        time.sleep(3)
        self.assertIn(text6, self.driver.page_source)

        # Check that Password and Re-Type password should be match:
        ManageAccountPage.changePassword(self, currentPW='Ss123456', newPW='Ff123456', reTypePW='Ss123456')
        time.sleep(3)
        self.assertIn(text6, self.driver.page_source)

        ###### Check that Password has been changed successfully after entered valid data:   ###########

        ManageAccountPage.changePassword(self, currentPW='Ss123456', newPW='Ff123456', reTypePW='Ff123456')
        time.sleep(3)
        self.assertIn(text7, self.driver.page_source)
        self.driver.refresh()

        ########   Return Test Data   ################

        ManageAccountPage.changePassword(self, currentPW='Ff123456', newPW='Rr123456', reTypePW='Rr123456')
        time.sleep(3)
        self.assertIn(text7, self.driver.page_source)
        self.driver.refresh()

        ManageAccountPage.changePassword(self, currentPW='Rr123456', newPW='Nn123456', reTypePW='Nn123456')
        time.sleep(3)
        self.assertIn(text7, self.driver.page_source)
        self.driver.refresh()

        ManageAccountPage.changePassword(self, currentPW='Nn123456', newPW='Mm123456', reTypePW='Mm123456')
        time.sleep(3)
        self.assertIn(text7, self.driver.page_source)
        self.driver.refresh()

        ManageAccountPage.changePassword(self, currentPW='Mm123456', newPW='Kk123456', reTypePW='Kk123456')
        time.sleep(3)
        self.assertIn(text7, self.driver.page_source)
        self.driver.refresh()

        ManageAccountPage.changePassword(self, currentPW='Kk123456', newPW='Ss123456', reTypePW='Ss123456')
        time.sleep(3)
        self.assertIn(text7, self.driver.page_source)
        self.driver.refresh()
        HomePage.logOut(self)
        time.sleep(3)
        LoginPage.logIn(self, "svetast999", "Ss123456")
        HelperTestBase.waitLogOutLink(self)
        self.assertIs(True, HomePage.checkLogOutLink(self))

    def test_changeEmail(self):
        driver = self.driver
        driver.get(self.base_url + '/Account/Dashboard')
        text1 = 'Update Successful'
        text2 = 'Email Address is required.'
        text3 = 'The emails do not match, please try again'
        text4 = 'Please enter a valid email address'

        LoginPage.logIn(self, "svetast999", "Ss123456")

        ManageAccountPage.clickAccountSettings(self)
        time.sleep(2)
        ########## Checking of Validation   ############

        ManageAccountPage.changeEmail(self, newEmailAddress='',
                                      newEmailAddressConfirmation='')
        time.sleep(2)
        self.assertIn(text2, self.driver.page_source)
        self.driver.refresh()

        ManageAccountPage.changeEmail(self, newEmailAddress='',
                                      newEmailAddressConfirmation='svetatestbox@gmail.com')
        time.sleep(2)
        self.assertIn(text2, self.driver.page_source)
        self.assertIn(text3, self.driver.page_source)
        self.driver.refresh()

        ManageAccountPage.changeEmail(self, newEmailAddress='svetatestbox@gmail.com',
                                      newEmailAddressConfirmation='')
        time.sleep(2)
        self.assertIn(text3, self.driver.page_source)
        self.driver.refresh()

        ManageAccountPage.changeEmail(self, newEmailAddress='svetatestbox@gmail.com',
                                      newEmailAddressConfirmation='sveta@gmail.com')
        time.sleep(2)
        self.assertIn(text3, self.driver.page_source)
        self.driver.refresh()

        ManageAccountPage.changeEmail(self, newEmailAddress='sveta@gmail.com',
                                      newEmailAddressConfirmation='svetatestbox@gmail.com')
        time.sleep(2)
        self.assertIn(text3, self.driver.page_source)
        self.driver.refresh()

        ManageAccountPage.changeEmail(self, newEmailAddress='w@e',
                                      newEmailAddressConfirmation='w@e')
        time.sleep(2)
        self.assertIn(text4, self.driver.page_source)
        self.driver.refresh()

        ########## Email has been changed successfully after entered valid data:  ############

        ManageAccountPage.changeEmail(self, newEmailAddress='svetatestbox@gmail.com',
                                      newEmailAddressConfirmation='svetatestbox@gmail.com')
        time.sleep(3)
        self.assertIn(text1, self.driver.page_source)
        self.driver.refresh()

        ### Return Test Data:     ########

        ManageAccountPage.changeEmail(self, newEmailAddress='Svetlana_Stepanova@microbilt.com',
                                      newEmailAddressConfirmation='Svetlana_Stepanova@microbilt.com')
        time.sleep(3)
        self.assertIn(text1, self.driver.page_source)
        self.driver.back()
