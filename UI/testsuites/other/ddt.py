#-*- coding: UTF-8 -*-
import datetime
import unittest
import  ddt
from getdata.ExcelUtil import  ExcelUtil
from pageobjects.common.topMenu import TopMenuPage
from utils.browser_engine import driver
from pageobjects.customer.newCustomer import  NewCustomerPage

nowTime = datetime.datetime.now().strftime("%Y/%m/%d %H:%M:%S")
filepath = "E:\\Automation\\UI\\test\\test.xlsx"
sheetName = "new_customer"
@ddt.ddt
class NewCustomer(unittest.TestCase):

    # 初始化，打开浏览器，并进行登录(实例化)
    @classmethod
    def setUpClass(cls):
        # open browser
         #browser = BrowserEngine(cls)
        cls.driver = driver
        #TopMenuPage().get_url()

    data = ExcelUtil(filepath, sheetName).dict_data()

    # 加载测试数据
    @ddt.data(*data)
    def test_01_newCustomer(self,data):
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
        areaCode = data['areaCode']
        phone = data['phone']
        type = data['type']

        TopMenuPage(self.driver).select_multiple_menu(2, "customers", "New", "", "")
        NewCustomerPage(self.driver).business_entity(entityType,entityClass,salutation,firstName,lastName,suffix,fullName,default_sort,organizationName,typeOfBusiness,stateOfIncorporation)
        NewCustomerPage(self.driver).contact(1, 1, CfirstName,ClastName,role,emailType,email,areaCode,phone,type)
        self.assertTrue(NewCustomerPage(self.driver).save())