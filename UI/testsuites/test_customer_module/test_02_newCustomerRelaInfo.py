#-*- coding: UTF-8 -*-
import datetime
import unittest
import  ddt
from utils.connect_sql import dbConnect
from getdata.ExcelUtil import excelHandle
from pageobjects.common.topMenu import TopMenuPage
from utils.browser_engine import driver
from pageobjects.customer.newCustomer import  NewCustomerPage
from utils.basepath_helper import excel_path

nowTime = datetime.datetime.now().strftime("%Y/%m/%d %H:%M:%S")
filepath = excel_path +"test.xlsx"
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
        u"""New Customer selected same as above"""
        entityType = data['entityType']
        salutation = data['salutation']
        entityClass = data['entityClass']
        suffix = data['suffix']
        typeOfBusiness = data['typeOfBusiness']
        stateOfIncorporation = data['stateOfIncorporation']
        emailType = data['emailType']
        phoneType = data['type1']

        TopMenuPage(self.driver).select_multiple_menu(2, "customers", "New", "", "")
        # CustomerRecordPage(self.driver).top_operate("Actions ", "New")
        NewCustomerPage(self.driver).business_entity(entityType, entityClass, salutation, suffix, typeOfBusiness,
                                                     stateOfIncorporation)
        NewCustomerPage(self.driver).contact(True, 1, 1,"", emailType, phoneType)
        self.assertTrue(NewCustomerPage(self.driver).save())
        self.assertTrue(NewCustomerPage(self.driver).validation_data())

    # 加载测试数据
    @ddt.data(*data)
    def test_02_two_contact(self,data):
        u"""New Customer with two contact,address,identifier"""
        entityType = data['entityType']
        entityClass = data['entityClass']
        salutation = data['salutation']
        suffix = data['suffix']
        typeOfBusiness = data['typeOfBusiness']
        stateOfIncorporation = data['stateOfIncorporation']
        role = data['role']
        emailType = data['emailType']
        phoneType1 = data['type1']
        phoneType2 = data['type2']
        phoneType3 = data['type3']
        # addressType = data['addressType']
        # stateCode = data['stateCode']
        # type = data['identifierName']
        addressType = dbConnect().getdata('MCDH', 'addressType','')
        stateCode = dbConnect().getdata('ALAMO', 'stateCode','')
        type = dbConnect().getdata('MCDH', 'identifierNameWithoutBan','')

        TopMenuPage(self.driver).select_multiple_menu(2, "customers", "New", "", "")
        # CustomerRecordPage(self.driver).top_operate("Actions ", "New")
        NewCustomerPage(self.driver).business_entity(entityType, entityClass, salutation, suffix,
                                                     typeOfBusiness, stateOfIncorporation)
        NewCustomerPage(self.driver).contact(False, 1, 1, role, emailType, phoneType1)
        NewCustomerPage(self.driver).add_phone("Phone 2", 1, 3, phoneType2)
        NewCustomerPage(self.driver).add_phone("Phone 3", 1, 5, phoneType3)
        NewCustomerPage(self.driver).contact(False, 3, 1, role, emailType, phoneType1)
        NewCustomerPage(self.driver).add_phone("Phone 2", 3, 3, phoneType2)
        NewCustomerPage(self.driver).add_phone("Phone 3", 3, 5, phoneType3)
        NewCustomerPage(self.driver).address("Address", addressType, stateCode)
        NewCustomerPage(self.driver).identifier("Identifier", type)
        self.assertTrue(NewCustomerPage(self.driver).save())
        self.assertTrue(NewCustomerPage(self.driver).validation_data())

