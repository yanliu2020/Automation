#-*- coding: UTF-8 -*-

import datetime
import unittest
from utils.browser_engine import driver
from utils.base_page import  BasePage
from pageobjects.common.topMenu import TopMenuPage
from pageobjects.homepage.homePage import  HomePage
from pageobjects.customer.customerRecord import CustomerRecordPage

nowTime = datetime.datetime.now().strftime("%Y/%m/%d %H:%M:%S")

class recordEntity(unittest.TestCase):

    # 初始化，打开浏览器，并进行登录(实例化)
    @classmethod
    def setUpClass(cls):
        cls.driver = driver
        TopMenuPage(cls.driver).is_homepage()
        HomePage(cls.driver).quick_entrance("Customers","C000089557",2)

    def test_01_Address_new(self):
        u"""new address"""
        CustomerRecordPage(self.driver).switch_tab("Entity")
        CustomerRecordPage(self.driver).entity_operator("Addresses", "New", "")
        self.assertTrue(CustomerRecordPage(self.driver).operator_address("Home", "Address", "changsha", "AK"))

    def test_02_Address_edit(self):
        u"""edit address"""
        CustomerRecordPage(self.driver).entity_operator("Addresses", "Edit", "1")
        self.assertTrue(CustomerRecordPage(self.driver).operator_address("Office", "Address1", "changsha", "AK"))

    def test_03_Address_delete(self):
        u"""delete address"""
        CustomerRecordPage(self.driver).entity_operator("Addresses", "Delete", "1")
        self.assertTrue(CustomerRecordPage(self.driver).delete())

    def test_04_Websites_new(self):
        u"""new Websites"""
        CustomerRecordPage(self.driver).entity_operator("Website", "New", "")
        self.assertTrue(CustomerRecordPage(self.driver).input_DBA_Website("url", "http://www.uiautomation.com"))

    def test_05_Websites_edit(self):
        u"""edit Websites"""
        CustomerRecordPage(self.driver).entity_operator("Website", "Edit", "1")
        self.assertTrue(CustomerRecordPage(self.driver).input_DBA_Website("url", "http://www.uiautomationEdit.com"))

    def test_06_Websites_delete(self):
        u"""delete Websites"""
        CustomerRecordPage(self.driver).entity_operator("Website", "Delete", "1")
        self.assertTrue(CustomerRecordPage(self.driver).delete())

    def test_07_DBA_new(self):
        u"""new a DBA"""
        CustomerRecordPage(self.driver).entity_operator("Doing Business As (DBA)", "New", "")
        self.assertTrue(CustomerRecordPage(self.driver).input_DBA_Website("alias", "UIAutomation" + nowTime))

    def test_08_DBA_edit(self):
        u"""edit DBA"""
        CustomerRecordPage(self.driver).entity_operator("Doing Business As (DBA)", "Edit", "1")
        self.assertTrue(CustomerRecordPage(self.driver).input_DBA_Website("alias", "UIAutomationEdit" + nowTime))

    def test_09_DBA_delete(self):
        u"""delete DBA"""
        CustomerRecordPage(self.driver).entity_operator("Doing Business As (DBA)", "Delete", "1")
        self.assertTrue(CustomerRecordPage(self.driver).delete())

    def test_10_Identifier_new(self):
        u"""new identifier"""
        CustomerRecordPage(self.driver).entity_operator("Business Identifier", "New", "")
        self.assertTrue(CustomerRecordPage(self.driver).operator_identifier("SSN", "123456789"))

    def test_11_Identifier_edit(self):
        u"""edit identifier"""
        CustomerRecordPage(self.driver).entity_operator("Business Identifier", "Edit", "1")
        self.assertTrue(CustomerRecordPage(self.driver).operator_identifier("State Tax ID", "11111111111"))

    def test_12_Identifier_delete(self):
        u"""delete identifier"""
        CustomerRecordPage(self.driver).entity_operator("Business Identifier", "Delete", "1")
        self.assertTrue(CustomerRecordPage(self.driver).delete())







