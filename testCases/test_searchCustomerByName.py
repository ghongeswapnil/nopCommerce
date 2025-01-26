import time

import pytest

from pageObjects.LoginPage import LoginPage
from pageObjects.AddcustomerPage import AddCustomer
from pageObjects.SearchCustomerPage import SearchCustomer
from utilities.customLogger import LogGen
from utilities.readProperties import ReadConfig


class Test_SearchCustomerByName_005:
    baseURL=ReadConfig.getApplicationURL()
    username=ReadConfig.getUseremail()
    password=ReadConfig.getPassword()
    logger=LogGen.loggen()        #Logger

    @pytest.mark.regression
    def test_searchCustomerByName(self,setup):
        self.logger.info("***************** SearchCustomerByName_005 **************")
        self.driver=setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.lp=LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        time.sleep(10)
        self.logger.info("************ Login Successful ************")

        self.logger.info("************* Starting Search Customer By Name ****************")

        self.addcust=AddCustomer(self.driver)
        self.addcust.ClickOnCustomersMenu()
        self.addcust.ClickOnCustomersMenuItem()

        self.logger.info("*************** searching customer by Name *********")
        searchcust=SearchCustomer(self.driver)
        searchcust.setFirstName("Victoria")
        searchcust.setLastName("Terces")
        searchcust.clickSearch()
        time.sleep(5)
        status=searchcust.searchCustomerByName("Victoria Terces")
        assert True==status
        self.logger.info("****************** TC_SeachCustomerByName_005 Finished ******")
        self.driver.close()


# pytest -v -s --html=Reports/report.html "E:\Automation\nopcommerceApp\testCases\test_searchCustomerByName.py" --browser chrome



