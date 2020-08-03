#-*- coding: UTF-8 -*-
import datetime
import unittest
import  ddt
from getdata.ExcelUtil import  excelHandle
from utils.basepath_helper import excel_path
from pageobjects.common.topMenu import TopMenuPage
from utils.browser_engine import driver
from pageobjects.customer.newCustomer import  NewCustomerPage
from pageobjects.customer.customerRecord import  CustomerRecordPage
nowTime = datetime.datetime.now().strftime("%Y/%m/%d %H:%M:%S")
filepath = excel_path +"test.xlsx"
sheetName = "new_customer"
@ddt.ddt
class newCustomer(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        #browser = BrowserEngine(cls)
        cls.driver = driver

    data = excelHandle(filepath, sheetName).read_excel()
    @ddt.data(*data)
    def test_addCustomer(self,data):
        u"""New Customer"""
        entityType = data['entityType']
        entityClass = data['entityClass']
        salutation = data['salutation']
        suffix = data['suffix']
        typeOfBusiness = data['typeOfBusiness']
        stateOfIncorporation = data['stateOfIncorporation']
        TopMenuPage(self.driver).select_multiple_menu(2, "customers", "New", "", "")
        NewCustomerPage(self.driver).business_entity(entityType, entityClass, salutation,suffix,typeOfBusiness,stateOfIncorporation)
        self.assertTrue(NewCustomerPage(self.driver).save())
        self.assertTrue(NewCustomerPage(self.driver).validation_data())

    @ddt.data(*data)
    def test_updateCustomer(self,data):
        u"""New Customer"""
        entityType = data['entityType']
        entityClass = data['entityClass']
        salutation = data['salutation']
        suffix = data['suffix']
        typeOfBusiness = data['typeOfBusiness']
        stateOfIncorporation = data['stateOfIncorporation']
        CustomerRecordPage(self.driver).top_operate("Actions ", "Edit")
        CustomerRecordPage(self.driver).edit_entity(entityType, entityClass, salutation,suffix,typeOfBusiness,stateOfIncorporation)
        self.assertTrue(NewCustomerPage(self.driver).save())
        self.assertTrue(NewCustomerPage(self.driver).validation_data())