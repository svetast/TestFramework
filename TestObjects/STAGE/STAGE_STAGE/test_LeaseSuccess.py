import time

import random

from HelperTestBase import HelperTestBase

import pytest

import HelperTestBase
from PageObjects.LoginPage import LoginPage
from PageObjects.HomePage import HomePage
from PageObjects.SearchResultsPage import SearchResultsPage
from PageObjects.CartPage import CartPage
from PageObjects.LeasePage import LeasePage

from PageObjects.RegistrationPage1 import RegistrationPage1
from PageObjects.RegistrationPage2 import RegistrationPage2
from PageObjects.RegistrationPage3 import RegistrationPage3
from PageObjects.RegistrationPage4 import RegistrationPage4
from PageObjects.RegistrationPage5 import RegistrationPage5

from PageObjects.ConfiguratorAdmin import ConfiguratorAdmin
from PageObjects.OrdersAdminPage import OrdersAdminPage


class TestLeaseCreatingSuccessPROD(LeasePage):
    """Test scenario:
        1.User LogIn on Portal.
        2.Check that Cart is empty.
        3.The product added to Cart.
        4.Lease processing => OK, 'Thank you.' is displayed.
        5.Check that Cart is empty after purchased.
        6.Returt to start test data: Go to ADMIN and change order status to Canceled """

    # @pytest.mark.skip
    def test_LeaseSuccessPROD_NewUser(self):
        driver = self.driver

        url_1 = self.base_url + '/Account/Signup'
        driver.get(url_1)
        url_2 = self.base_url + '/Account/ApplyNow'
        url_3 = self.base_url + '/Account/ApplyNow#'
        x = random.randint(100, 10000)
        text3 = 'Employment Information'
        text4 = 'Personal Information'
        text5 = 'Payment Information'
        text6 = 'Congratulations!'

        # time.sleep(3)

        # self.driver.refresh()

        ##### Page 1: START Let’s Create Your Account  ###########

        RegistrationPage1.fillForm1(self,
                                    email='svetatestbox@gmail.com',
                                    username='svetast' + str(x),
                                    password="Ss123456",
                                    passwordConfirm="Ss123456",
                                    answer='valya')

        ################## Page2 : Contact Information  #########################

        RegistrationPage2.fillForm2(self,
                                    firstName='sveta',
                                    lastName='step' + str(x),
                                    phone='121212121212',
                                    portal='mainstreet')

        ################## Page3: Employment Information   #########################

        RegistrationPage3.fillForm3(self,
                                    employerName='Private Firm Niagara',
                                    empPhone='5986547899',
                                    income='9999',
                                    ohterIncome='')

        ################## Page4: Personal Information   #########################

        RegistrationPage4.fillForm4(self,
                                    ssn='121512230',
                                    driverLic='555555555',
                                    state="AL")

        ######## Page5:     Payment Information   ###########################

        RegistrationPage5.fillForm5(self, accountType='DebitCard',
                                    cardNumber='5454-5454-5454-5454',
                                    cvv="1234",
                                    month='12',
                                    year='2021')

        time.sleep(35)
        self.assertIn(text6, self.driver.page_source)
        RegistrationPage5.clickContinueButton(self)
        time.sleep(15)
        self.assertIs(True, HomePage.checkINFOBannerPresent(self))

        text1 = 'Thank you.'
        text2 = 'No items found in your cart.'
        url_2 = self.base_url + '/cart'

        ### Precondition : check that Cart is empty:
        driver.get(url_2)
        self.assertIn(text2, self.driver.page_source)

        ### test scope : add the item to Cart:

        HomePage.submitSearch(self, 'canon')
        SearchResultsPage.clickAddToCart(self)
        self.driver.get(url_2)
        time.sleep(5)
        ### test scope : click on Checkout button :
        CartPage.clickCheckoutButton(self)
        time.sleep(5)
        ### test scope : click on Price Reviewed Opt In , ReviewYourLease  buttons:
        CartPage.selectPriceReviewedOptIn(self)
        CartPage.clickReviewYourLease(self)

        ### test scope : check that user accepted the Lease:
        LeasePage.signAgreement(self, firstName='sveta', lastName=' step' + str(x))
        time.sleep(100)
        self.assertIn(text1, self.driver.page_source)
        driver.get(url_2)
        time.sleep(8)
        self.assertIn(text2, self.driver.page_source)
        # time.sleep(10)

    @pytest.mark.skip
    def test_LeaseSuccessPROD_Tires(self):
        driver = self.driver
        driver.get(self.base_url + '/Account/Login')
        text1 = 'Thank you.'
        text2 = 'No items found in your cart.'
        url_3 = 'https://admin.ltomall.com'
        url_2 = self.base_url + '/cart'

        LoginPage.logIn(self, "svetast1968", "Ss123456")
        HomePage.submitSearch(self, 'road')
        SearchResultsPage.clickAddToCart(self)
        driver.get(url_2)
        time.sleep(8)
        CartPage.clickCheckoutButton(self)
        time.sleep(3)
        CartPage.selectPriceReviewedOptIn(self)
        CartPage.clickReviewYourLease(self)
        LeasePage.signAgreement(self, firstName='sveta', lastName=' step1968')
        time.sleep(30)
        self.assertIn(text1, self.driver.page_source)
        driver.get(url_2)
        time.sleep(5)
        self.assertIn(text2, self.driver.page_source)

        #####  Return Test Data ##########
        driver.get(url_3)
        ConfiguratorAdmin.loginAdminProd(self)
        driver.get(url_3 + '/Secure/Orders/OrderManagement/ViewOrders/Default.aspx')
        OrdersAdminPage.findOrdersByLastname(self, 'step1968')
        OrdersAdminPage.clickManageOrder(self)
        OrdersAdminPage.clickUpdateOrderStatus(self)
        OrdersAdminPage.clickCancelOrder(self)
        time.sleep(10)
        OrdersAdminPage.clickBackToOrderList(self)
