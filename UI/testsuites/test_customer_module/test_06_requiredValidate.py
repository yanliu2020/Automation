#-*- coding: UTF-8 -*-
import unittest
import  ddt
from getdata.ExcelUtil import  excelHandle
from utils.basepath_helper import excel_path
from pageobjects.common.topMenu import TopMenuPage
from utils.browser_engine import driver
from pageobjects.customer.newCustomer import  NewCustomerPage
from utils.base_page import BasePage
filepath = excel_path +"TestData.xlsx"
sheetName = "Customer"
@ddt.ddt
class requiredFields(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = driver
        BasePage(cls.driver).close_current_window()
        TopMenuPage(cls.driver).select_multiple_menu(2, "customers", "New", "", "")

    data = excelHandle(filepath,sheetName).read_excel()
    @ddt.data(*data)
    def test_01_businessEntity_required(self,data):
        u"""new customer page validate required fields"""
        entityType = data['entityType']
        entityClass = data['entityClass']
        self.assertTrue(NewCustomerPage(self.driver).validate_required(entityType, entityClass,"Business Entity"))

    def test_02_contact_required(self):
        u"""new customer page validate contact required fields"""
        self.assertTrue(NewCustomerPage(self.driver).validate_required("Person","Sole Proprietor","Contact"))

    def test_03_addressIdentifier_required(self):
        u"""new customer page validate address/identifier required fields"""
        self.assertTrue(NewCustomerPage(self.driver).validate_required("Person","Individual","Address&Identifier"))