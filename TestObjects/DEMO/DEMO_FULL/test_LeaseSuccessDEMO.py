import time
import random

import pytest

from HelperTestBase import HelperTestBase

from PageObjects.RegistrationPage1 import RegistrationPage1
from PageObjects.RegistrationPage2 import RegistrationPage2
from PageObjects.RegistrationPage3 import RegistrationPage3
from PageObjects.RegistrationPage4 import RegistrationPage4
from PageObjects.RegistrationPage5 import RegistrationPage5

from PageObjects.LoginPage import LoginPage
from PageObjects.HomePage import HomePage
from PageObjects.SearchResultsPage import SearchResultsPage
from PageObjects.CartPage import CartPage
from PageObjects.LeasePage import LeasePage

from PageObjects.ConfiguratorPortalsStagePage import ConfiguratorPortalsStagePage

from PageObjects.VehicleInfoPage import VehiclenInfoPage
from PageObjects.ConfiguratorAdminPageOld import ConfiguratorAdminPage
from PageObjects.OrdersAdminPage import OrdersAdminPage


class TestLeaseCreatingSuccessDEMO(LeasePage):
    """Test scenario:
    1.User LogIn on Portal.
    2.Check that Cart is empty.
    3.The product added to Cart.
    4.Lease processing => OK, 'Thank you.' is displayed.
    5.Check that Cart is empty after purchased.
    6.Returt to start test data: Go to ADMIN and change order status to Canceled """

    # @pytest.mark.skip
    def test_LeaseSuccessSTAGE_CurrentUser(self):
        driver = self.driver
        driver.get(self.base_url + '/Account/Login')
        text1 = 'Thank you.'
        text2 = 'No items found in your cart.'
        url_2 = self.base_url + '/cart'
        s = '/Secure/Orders/OrderManagement/ViewOrders/Default.aspx'
        url_3 = 'https://admin.ltostage.com'

        LoginPage.logIn(self, "svetast6921", "Ss123456")

        ### test scope : add the item to Cart:

        HomePage.submitSearch(self, 'canon')  # 'canon' mainstreet
        SearchResultsPage.clickAddToCart(self)
        self.driver.get(url_2)
        time.sleep(5)
        ### test scope : click on Checkout button :
        CartPage.clickCheckoutButton(self)
        time.sleep(3)
        ### test scope : click on Price Reviewed Opt In , ReviewYourLease  buttons:
        CartPage.selectPriceReviewedOptIn(self)
        CartPage.clickReviewYourLease(self)

        ### test scope : check that user accepted the Lease:
        LeasePage.signAgreement(self, firstName='sveta', lastName=' step6921')
        time.sleep(100)
        self.assertIn(text1, self.driver.page_source)
        driver.get(url_2)
        time.sleep(8)
        self.assertIn(text2, self.driver.page_source)
        time.sleep(10)

        #####  Return Test Data ##########

        """driver.get(url_3)
        time.sleep(8)
        ConfiguratorAdminPage.loginAdminStage(self)
        driver.get(url_3 + s)
        time.sleep(10)
        OrdersAdminPage.findOrdersByLastname(self, 'step1968')
        OrdersAdminPage.clickManageOrder(self)
        OrdersAdminPage.clickUpdateOrderStatus(self)
        OrdersAdminPage.clickCancelOrder(self)
        time.sleep(5)
        OrdersAdminPage.clickBackToOrderList(self)"""

    # @pytest.mark.skip
    def test_LeaseSuccessSTAGE_NewUser(self):
        driver = self.driver
        driver.get(self.base_url)
        url_1 = self.base_url + '/Account/Signup'
        url_2 = self.base_url + '/Account/ApplyNow'
        url_3 = self.base_url + '/Account/ApplyNow#'
        x = random.randint(100, 10000)
        text3 = 'Employment Information'
        text4 = 'Personal Information'
        text5 = 'Payment Information'
        text6 = 'Congratulations!'
        PORTAL = 'ltodemo'

        s = '/Secure/Orders/OrderManagement/ViewOrders/Default.aspx'
        url_3 = 'https://admin.ltostage.com'

        time.sleep(3)
        driver.get(self.base_url + '/Account/Signup')

        # self.driver.refresh()

        ##### Page 1: START Let’s Create Your Account  ###########

        RegistrationPage1.fillForm1(self,
                                    email='svetlana_stepanova@microbilt.com',
                                    username='svetast' + str(x),
                                    password="Ss123456",
                                    passwordConfirm="Ss123456",
                                    answer='valya')

        # self.assertEqual(url_2, HelperTestBase.getURL(self))
        HelperTestBase.waitNextButton(self)

        ################## Page2 : Contact Information  #########################

        RegistrationPage2.fillForm2(self,
                                    firstName='sveta',
                                    lastName='step' + str(x),
                                    phone='121212121212',
                                    portal=PORTAL)

        time.sleep(5)
        self.assertIn(text3, self.driver.page_source)

        ################## Page3: Employment Information   #########################

        RegistrationPage3.fillForm3(self,
                                    employerName='Private Firm Niagara',
                                    empPhone='5986547899',
                                    income='9999',
                                    ohterIncome='')

        # time.sleep(5)
        # self.assertIn(text4, self.driver.page_source)

        ################## Page4: Personal Information   #########################

        RegistrationPage4.fillForm4(self,
                                    ssn='121512230',
                                    driverLic='555555555',
                                    state="AL")
        time.sleep(5)
        self.assertIn(text5, self.driver.page_source)

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
        url_3 = 'https://admin.ltostage.com'

        ### Precondition : check that Cart is empty:
        driver.get(url_2)
        self.assertIn(text2, self.driver.page_source)

        ### test scope : add the item to Cart:

        HomePage.submitSearch(self, 'canon')  # mainstreet
        # HomePage.submitSearch(self, 'dewalt')  # toolcabin
        SearchResultsPage.clickAddToCart(self)
        self.driver.get(url_2)
        time.sleep(5)
        ### test scope : click on Checkout button :
        CartPage.clickCheckoutButton(self)
        time.sleep(3)
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

        #####  Checking - Admin can canceled payment ##########

        # driver.get(url_3)
        # time.sleep(8)
        # ConfiguratorAdminPage.loginAdminStage(self)
        # driver.get(url_3 + s)
        # time.sleep(10)
        # OrdersAdminPage.findOrdersByLastname(self, 'step' + str(x))
        # OrdersAdminPage.clickManageOrder(self)
        # OrdersAdminPage.clickUpdateOrderStatus(self)
        # OrdersAdminPage.clickCancelOrder(self)
        # time.sleep(30)
        # OrdersAdminPage.clickBackToOrderList(self)"""

    @pytest.mark.skip
    def test_LeaseSuccessSmartTiresSTAGE(self):
        driver = self.driver
        driver.get(self.base_url + '/Account/Login')
        text10 = 'Thank you.'
        text5 = 'No items found in your cart.'
        url_2 = self.base_url + '/cart'
        url_3 = 'https://admin.ltostage.com'

        text1 = 'Is required'
        text2 = 'Only year from 1900 to 2099 is allowed for the Vehicle Year field'
        text11 = 'Only numbers are allowed (numbers should be from 0 to 99999999 and should not start from zero)'
        text3 = 'Please enter valid 3rd party phone'

        text4 = 'Upper and lower case letters, numbers, spaces are allowed'
        text6 = 'Only numbers are allowed'
        text8 = 'Upper and lower case letters, numbers are allowed'
        text9 = 'Only numbers allowed in the Year of your vehicle'

        LoginPage.logIn(self, "svetast1968", "Ss123456")

        ### Precondition : check that Cart is empty:
        driver.get(url_2)
        time.sleep(5)
        self.assertIn(text5, self.driver.page_source)
        HomePage.submitSearch(self, 'road')
        time.sleep(5)
        SearchResultsPage.clickAddToCart(self)
        driver.get(url_2)
        time.sleep(5)
        CartPage.clickCheckoutButton(self)
        time.sleep(3)

        ### Test scope  : check fields validation:

        self.driver.refresh()
        VehiclenInfoPage.fiilForm(self, make="", vehicleYear="", model="",
                                  vin="", mileage="", licenseTag="",
                                  state="", partyPhone="")
        time.sleep(4)
        self.assertIn(text1, self.driver.page_source)
        self.assertIn(text2, self.driver.page_source)
        self.assertIn(text11, self.driver.page_source)
        self.driver.refresh()

        VehiclenInfoPage.fiilForm(self, make="!@#$%^&*()_+<>?",
                                  vehicleYear="!@#$%^&*()_+<>?",
                                  model="!@#$%^&*()_+<>?",
                                  vin="!@#$%^&*()_+<>?",
                                  mileage="!@#$%^&*()_+<>?",
                                  licenseTag="!@#$%^&*()_+<>?",
                                  state="!@#$%^&*()_+<>?",
                                  partyPhone="!@#$%^&*()_+<>?")

        time.sleep(4)
        self.assertIn(text6, self.driver.page_source)
        self.assertIn(text4, self.driver.page_source)
        self.driver.refresh()

        VehiclenInfoPage.fiilForm(self, make="Qa 1",
                                  vehicleYear="Qa 1",
                                  model="Qa 1",
                                  vin="Qa 1",
                                  mileage="Qa 1",
                                  licenseTag="Qa 1",
                                  state="Qa 1",
                                  partyPhone="Qa 1")

        self.assertIn(text8, self.driver.page_source)
        self.assertIn(text2, self.driver.page_source)
        self.assertIn(text3, self.driver.page_source)
        self.driver.refresh()

        VehiclenInfoPage.fiilForm(self, make="Qa 1",
                                  vehicleYear="123",
                                  model="Qa 1",
                                  vin="123",
                                  mileage="123",
                                  licenseTag="Qa 1",
                                  state="Qa 1",
                                  partyPhone="123")
        self.assertIn(text3, self.driver.page_source)
        self.driver.refresh()

        VehiclenInfoPage.fiilForm(self, make="opel 2500",
                                  vehicleYear="2012",
                                  model="opel",
                                  vin="123",
                                  mileage="123",
                                  licenseTag="Qa 1",
                                  state="LA",
                                  partyPhone="1233666666")
        time.sleep(5)

        CartPage.selectPriceReviewedOptIn(self)
        CartPage.clickReviewYourLease(self)
        LeasePage.signAgreement(self, firstName='sveta', lastName=' step1968')
        time.sleep(60)
        self.assertIn(text10, self.driver.page_source)
        driver.get(url_2)
        time.sleep(8)
        self.assertIn(text5, self.driver.page_source)
        time.sleep(10)

        #####  Return Test Data ##########

        driver.get(url_3)
        ConfiguratorAdminPage.loginAdminStage(self)
        driver.get(url_3 + '/Secure/Orders/OrderManagement/ViewOrders/Default.aspx')
        OrdersAdminPage.findOrdersByLastname(self, 'step1968')
        OrdersAdminPage.clickManageOrder(self)
        OrdersAdminPage.clickUpdateOrderStatus(self)
        OrdersAdminPage.clickCancelOrder(self)
        time.sleep(25)
        OrdersAdminPage.clickBackToOrderList(self)
