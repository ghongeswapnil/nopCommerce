import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class AddCustomer():
    #Add customer Page
    lnkCustomers_menu_xpath = "//a[@href='#']//p[contains(text(),'Customers')]"
    lnkCustomers_menuitem_xpath = "//a[@href='/Admin/Customer/List']//p[contains(text(),'Customers')]"
    btnAddnew_xpath = "//a[@class='btn btn-primary']"
    txtEmail_xpath = "//input[@id='Email']"
    txtPassword_xpath = "//input[@id='Password']"
    txtFirstName_xpath = "//input[@id='FirstName']"
    txtLastName_xpath = "//input[@id='LastName']"
    rdMaleGender_id = "Gender_Male"
    rdFemaleGender_id = "Gender_Female"
    txtDob_xpath = "//input[@id='DateOfBirth']"
    txtCompanyName_xpath = "//input[@id='Company']"
    txtNewsLetter_ixpath = "(//input[@role='searchbox'])[1]"
    lstitemYourStoreName_xpath = "//li[contains(text(),'Your store name')]"
    lstitemTestStore2_xpath = "//li[contains(text(),'Test store 2')]"
    txtCustomerRoles_xpath = "(//input[@role='searchbox'])[2]"
    lstitemAdministrators_xpath = "//li[contains(text(),'Administrators')]"
    lstitemForumModerators_xpath = "//li[contains(text(),'Forum Moderators')]"
    lstitemRegistered_xpath = "//li[contains(text(),'Registered')]"
    lstitemGuests_xpath = "//li[contains(text(),'Guests')]"
    lstitemVendors_xpath = "//li[contains(text(),'Vendors')]"
    lstitemtest_xpath = "//li[contains(text(),'test')]"
    drpmgrOfVendor_xpath = "//select[@id='VendorId']"
    txtAdminComment_xpath = "//textarea[@id='AdminComment']"
    btnSave_xpath = "//button[@name='save']"


    def __init__(self,driver):
        self.driver=driver

    def ClickOnCustomersMenu(self):
        self.driver.find_element(By.XPATH,self.lnkCustomers_menu_xpath).click()

    def ClickOnCustomersMenuItem(self):
        self.driver.find_element(By.XPATH,self.lnkCustomers_menuitem_xpath).click()

    def ClickOnAddnew(self):
        self.driver.find_element(By.XPATH,self.btnAddnew_xpath).click()

    def setEmail(self,email):
        self.driver.find_element(By.XPATH,self.txtEmail_xpath).send_keys(email)

    def setPassword(self,password):
        self.driver.find_element(By.XPATH,self.txtPassword_xpath).send_keys(password)

    def setCustomerRoles(self,role):
        self.driver.find_element(By.XPATH,self.txtCustomerRoles_xpath).click()
        time.sleep(3)
        if role == 'Registered' :
            self.listitem = self.driver.find_element(By.XPATH,self.lstitemRegistered_xpath)
        elif role == 'Administrators':
            self.listitem = self.driver.find_element(By.XPATH,self.lstitemAdministrators_xpath)
        elif role == 'Guest':
            # Here user can be registered (or) Guest, only one
            time.sleep(3)
            self.driver.find_element(By.XPATH,"//*[@id='SelectedCustomerRoleIds_taglist']/li/span[2]").click()
            self.listitem = self.driver.find_element(By.XPATH,self.lstitemGuests_xpath)
        elif role == 'Registered':
            self.listitem = self.driver.find_element(By.XPATH,self.lstitemRegistered_xpath)
        elif role == 'Vendors':
            self.listitem = self.driver.find_element(By.XPATH,self.lstitemVendors_xpath)
        else:
            self.listitem = self.driver.find_element(By.XPATH,self.lstitemGuests_xpath)
        time.sleep(3)

        self.driver.execute_script("arguments[0].click();",self.listitem)

    def setManagerOfVendor(self,value):
        drp=Select(self.driver.find_element(By.XPATH,self.drpmgrOfVendor_xpath))
        drp.select_by_visible_text(value)

    def setGender(self,gender):
        if gender == 'Male':
            self.driver.find_element(By.ID,self.rdMaleGender_id).click()
        elif gender == 'Female':
            self.driver.find_element(By.ID,self.rdFemaleGender_id).click()
        else:
            self.driver.find_element(By.ID,self.rdMaleGender_id).click()

    def setFirstName(self,fname):
        self.driver.find_element(By.XPATH,self.txtFirstName_xpath).send_keys(fname)

    def setLastName(self,lname):
        self.driver.find_element(By.XPATH,self.txtLastName_xpath).send_keys(lname)

    def setDob(self,dob):
        self.driver.find_element(By.XPATH,self.txtDob_xpath).send_keys(dob)

    def setCompanyName(self,comname):
        self.driver.find_element(By.XPATH,self.txtCompanyName_xpath).send_keys(comname)

    def setAdminComment(self,comment):
        self.driver.find_element(By.XPATH,self.txtAdminComment_xpath).send_keys(comment)

    def ClickOnSave(self):
        self.driver.find_element(By.XPATH,self.btnSave_xpath).click()