import time

import pytest

from pageObjects.LoginPage import LoginPage
from pageObjects.AddcustomerPage import AddCustomer
from pageObjects.SearchCustomerPage import SearchCustomer
from utilities.customLogger import LogGen
from utilities.readProperties import ReadConfig


class Test_SearchCustomerByEmail_004:
    baseURL=ReadConfig.getApplicationURL()
    username=ReadConfig.getUseremail()
    password=ReadConfig.getPassword()
    logger=LogGen.loggen()        #Logger

    # @pytest.mark.regression
    def test_searchCustomerByEmail(self,setup):
        self.logger.info("***************** SearchCustomerByEmail_004 **************")
        self.driver=setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.lp=LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.logger.info("************ Login Successful ************")

        self.logger.info("************* Starting Search Customer By Email ****************")

        self.addcust=AddCustomer(self.driver)
        self.addcust.ClickOnCustomersMenu()
        self.addcust.ClickOnCustomersMenuItem()

        self.logger.info("*************** searching customer by emailID *********")
        searchcust=SearchCustomer(self.driver)
        searchcust.setEmail("victoria_victoria@nopCommerce.com")
        searchcust.clickSearch()
        time.sleep(5)
        # status=searchcust.searchCustomerByEmail("victoria_victoria@nopCommerce.com")
        # assert True==status
        self.logger.info("****************** TC_SeachCustomerByEmail_004 Finished ******")
        self.driver.close()


# pytest -v -s --html=Reports/report.html "E:\Automation\nopcommerceApp\testCases\test_searchCustomerByEmail.py" --browser chrome



