#-*- coding: UTF-8 -*-
import datetime
import unittest
import  ddt
from ddt import ddt, data, unpack
from utils.get_data import  excelHandle
from pageobjects.common.topMenu import TopMenuPage
from utils.browser_engine import driver
from pageobjects.customer.newCustomer import  NewCustomerPage
from pageobjects.customer.customerRecord import  CustomerRecordPage

nowTime = datetime.datetime.now().strftime("%Y/%m/%d %H:%M:%S")
filepath = "E:\\Automation\\UI\\getdata\\testData.xlsx"
sheetName = "new_customer"
@ddt
class newCustomer(unittest.TestCase):

    # 初始化，打开浏览器，并进行登录(实例化)
    @classmethod
    def setUpClass(cls):
        # open browser
        #browser = BrowserEngine(cls)
        cls.driver = driver

    data = excelHandle(filepath, sheetName).read_excel()

    # 加载测试数据
    @data(*data)
    @unpack
    def addCustomer(self,entityType, entityClass, salutation, firstName, lastName, suffix,
                                                     fullName, default_sort, organizationName, typeOfBusiness,
                                                     stateOfIncorporation):
        u"""New Customer"""
        TopMenuPage(self.driver).select_multiple_menu(2, "customers", "New", "", "")
        NewCustomerPage(self.driver).business_entity(entityType, entityClass, salutation, firstName, lastName, suffix,
                                                     fullName, default_sort, organizationName, typeOfBusiness,
                                                     stateOfIncorporation)
        self.assertTrue(NewCustomerPage(self.driver).save())
