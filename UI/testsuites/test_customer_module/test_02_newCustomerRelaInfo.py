#-*- coding: UTF-8 -*-
import datetime
import unittest
import  ddt
from getdata.ExcelUtil import  excelHandle
from pageobjects.common.topMenu import TopMenuPage
from utils.browser_engine import driver
from pageobjects.customer.newCustomer import  NewCustomerPage
from pageobjects.homepage.homePage import HomePage
from pageobjects.customer.customerRecord import  CustomerRecordPage

nowTime = datetime.datetime.now().strftime("%Y/%m/%d %H:%M:%S")
filepath = "E:\\Automation\\UI\\getdata\\test.xlsx"
sheetName = "two_contact"
@ddt.ddt
class newCustomerRelaInfo(unittest.TestCase):

    # 初始化，打开浏览器，并进行登录(实例化)
    @classmethod
    def setUpClass(cls):
        # open browser
        cls.driver = driver

    data = excelHandle(filepath, sheetName).read_excel()

    # 加载测试数据
    @ddt.data(*data)
    def test_01_newRelateInfo(self,data):
        u"""New Customer"""
        entityType = data['entityType']
        entityClass = data['entityClass']
        salutation = data['salutation']
        firstName = data['firstName']
        lastName = data['lastName']
        suffix = data['suffix']
        fullName = data['fullName']
        default_sort = data['default_sort']
        organizationName = data['organizationName']
        typeOfBusiness = data['typeOfBusiness']
        stateOfIncorporation = data['stateOfIncorporation']
        CfirstName = data['CfirstName']
        ClastName = data['ClastName']
        role = data['role']
        emailType = data['emailType']
        email = data['email']
        areaCode1 = data['areaCode1']
        phone1 = data['phone1']
        type1 = data['type1']
        areaCode2 = data['areaCode2']
        phone2 = data['phone2']
        type2 = data['type2']
        areaCode3 = data['areaCode3']
        phone3 = data['phone3']
        type3 = data['type3']

        # TopMenuPage(self.driver).select_multiple_menu(2, "customers", "New", "", "")
        CustomerRecordPage(self.driver).top_operate("Actions ", "New")
        NewCustomerPage(self.driver).business_entity(entityType, entityClass, salutation, firstName, lastName, suffix,
                                                     fullName, default_sort, organizationName, typeOfBusiness,
                                                     stateOfIncorporation)
        NewCustomerPage(self.driver).contact(False, 1, 1, CfirstName, ClastName, role, emailType, email, areaCode1,
                                             phone1, type1)
        NewCustomerPage(self.driver).add_phone("Phone 2", 1, 3, areaCode2, phone2, type2)
        NewCustomerPage(self.driver).add_phone("Phone 3", 1, 5, areaCode3, phone3, type3)
        NewCustomerPage(self.driver).contact(False, 3, 1, CfirstName, ClastName, role, emailType, email, areaCode1,
                                             phone1, type1)
        NewCustomerPage(self.driver).add_phone("Phone 2", 3, 3, areaCode2, phone2, type2)
        NewCustomerPage(self.driver).add_phone("Phone 3", 3, 5, areaCode3, phone3, type3)
        NewCustomerPage(self.driver).address("Address", "Home", "Address", "changsha", "AK", "07311")
        NewCustomerPage(self.driver).identifier("Identifier", "SSN", "999999999")
        self.assertTrue(NewCustomerPage(self.driver).save())

    @ddt.data(*data)
    def test_02_Same_Above(self, data):
        u"""New Customer"""
        entityType = data['entityType']
        entityClass = data['entityClass']
        salutation = data['salutation']
        firstName = data['firstName']
        lastName = data['lastName']
        suffix = data['suffix']
        fullName = data['fullName']
        default_sort = data['default_sort']
        organizationName = data['organizationName']
        typeOfBusiness = data['typeOfBusiness']
        stateOfIncorporation = data['stateOfIncorporation']
        emailType = data['emailType']
        email = data['email']
        areaCode1 = data['areaCode1']
        phone1 = data['phone1']
        type1 = data['type1']

        # TopMenuPage(self.driver).select_multiple_menu(2, "customers", "New", "", "")
        CustomerRecordPage(self.driver).top_operate("Actions ", "New")
        NewCustomerPage(self.driver).business_entity(entityType, entityClass, salutation, firstName, lastName, suffix,
                                                     fullName, default_sort, organizationName, typeOfBusiness,
                                                     stateOfIncorporation)
        NewCustomerPage(self.driver).contact(True, 1, 1, "", "", "", emailType, email, areaCode1,
                                             phone1, type1)
        self.assertTrue(NewCustomerPage(self.driver).save())
