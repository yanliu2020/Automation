#-*- coding: UTF-8 -*-
import datetime
import unittest
import  ddt
from getdata.ExcelUtil import  excelHandle
from pageobjects.common.topMenu import TopMenuPage
from utils.browser_engine import driver
from pageobjects.customer.newCustomer import  NewCustomerPage
from utils.base_page import BasePage

nowTime = datetime.datetime.now().strftime("%Y/%m/%d %H:%M:%S")
nowTime1 = datetime.datetime.now().strftime("%Y/%m/%d")
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

    @ddt.data(*data)
    def test_01_Same_Above(self, data):
        u"""New Customer"""
        entityType = data['entityType']
        entityClass = data['entityClass']
        salutation = data['salutation']
        suffix = data['suffix']
        typeOfBusiness = data['typeOfBusiness']
        stateOfIncorporation = data['stateOfIncorporation']
        emailType = data['emailType']
        type1 = data['type1']
        TopMenuPage(self.driver).select_multiple_menu(2, "customers", "New", "", "")
        # CustomerRecordPage(self.driver).top_operate("Actions ", "New")
        NewCustomerPage(self.driver).business_entity(entityType, entityClass, salutation,suffix,typeOfBusiness,stateOfIncorporation)
        NewCustomerPage(self.driver).contact(True, 1, 1,"", emailType,type1)
        self.assertTrue(NewCustomerPage(self.driver).save())

    # 加载测试数据
    @ddt.data(*data)
    def test_02_addRelateInfo(self,data):
        u"""New Customer"""
        entityType = data['entityType']
        entityClass = data['entityClass']
        salutation = data['salutation']
        suffix = data['suffix']
        typeOfBusiness = data['typeOfBusiness']
        stateOfIncorporation = data['stateOfIncorporation']
        role = data['role']
        emailType = data['emailType']
        type1 = data['type1']
        type2 = data['type2']
        type3 = data['type3']
        TopMenuPage(self.driver).select_multiple_menu(2, "customers", "New", "", "")
        # CustomerRecordPage(self.driver).top_operate("Actions ", "New")
        NewCustomerPage(self.driver).business_entity(entityType, entityClass, salutation,suffix,typeOfBusiness,stateOfIncorporation)
        NewCustomerPage(self.driver).contact(False, 1, 1, role,emailType,type1)
        NewCustomerPage(self.driver).add_phone("Phone 2", 1, 3,type2)
        NewCustomerPage(self.driver).add_phone("Phone 3", 1, 5,type3)
        NewCustomerPage(self.driver).contact(False, 3, 1, role,emailType,type1)
        NewCustomerPage(self.driver).add_phone("Phone 2", 3, 3,type2)
        NewCustomerPage(self.driver).add_phone("Phone 3", 3, 5,type3)
        NewCustomerPage(self.driver).address("Address", "Home", "AK")
        NewCustomerPage(self.driver).identifier("Identifier", "SSN")
        self.assertTrue(NewCustomerPage(self.driver).save())

