import random
import string
import time

import pytest
from selenium.webdriver.common.by import By

from pageObjects.AddcustomerPage import AddCustomer
from pageObjects.LoginPage import LoginPage
from utilities.customLogger import LogGen
from utilities.readProperties import ReadConfig


class Test_003_AddCustomer:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()    #Logger

    @pytest.mark.sanity
    def test_addCustomer(self,setup):
        self.logger.info("***************** Test_003_AddCustomer ***************")
        self.driver=setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.lp= LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        time.sleep(10)
        self.logger.info("**************** Login Successful ***************")

        self.logger.info("*************** Starting Add Customer Test ***********")

        self.addcust=AddCustomer(self.driver)
        self.addcust.ClickOnCustomersMenu()
        self.addcust.ClickOnCustomersMenuItem()
        self.addcust.ClickOnAddnew()

        self.logger.info("***************** Providing customer info *****************")

        # self.email = random_generator() + "@gmail.com"
        # self.addcust.setEmail(self.email)
        self.addcust.setEmail("abc@gmail.com")
        self.addcust.setPassword("test123")
        self.addcust.setCustomerRoles("Guests")
        self.addcust.setManagerOfVendor("Vendor 2")
        self.addcust.setGender("Male")
        self.addcust.setFirstName("Swapnil")
        self.addcust.setLastName("Ghonge")
        self.addcust.setDob("02/10/1992")         #Format: DD/MM/YYYY
        self.addcust.setCompanyName("ABC Pvt.Ltd.")
        self.addcust.setAdminComment("This is for testing......")
        self.addcust.ClickOnSave()

        self.logger.info("***************** Saving customer info ******************")

        self.logger.info("************* Add customer validation started ************")

        self.msg = self.driver.find_element(By.TAG_NAME,"body").text

        print(self.msg)
        if "customer has been added successfully." in self.msg:
            assert True == True
            self.logger.info("************** Add customer Test pass**********")
        else:
            self.driver.save_screenshot(".\\Screenshots\\"+"test_addCustomer_src.png")    #Screenshot
            self.logger.error("*************** Add customer Test Failed ***************")
            assert True == False

        self.driver.close()
        self.logger.info("***************** Ending Add Customer Test **************")



def random_generator(size=8,chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for x in range(size))









# pytest -v -s -n=2 --html=Reports/report.html "E:\Automation\nopcommerceApp\testCases\test_addCustomer.py" --browser chrome