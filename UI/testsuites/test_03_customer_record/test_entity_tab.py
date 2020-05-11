#-*- coding: UTF-8 -*-

import datetime
import unittest
from utils.browser_engine import driver
from utils.base_page import  BasePage
from pageobjects.common.topMenu import TopMenuPage
from pageobjects.homepage.homePage import  HomePage
from pageobjects.customer.customerRecord import CustomerRecordPage

nowTime = datetime.datetime.now().strftime("%Y/%m/%d %H:%M:%S")

class Identifier_Address(unittest.TestCase):

    # 初始化，打开浏览器，并进行登录(实例化)
    @classmethod
    def setUpClass(cls):
        cls.driver = driver
        TopMenuPage(cls.driver).get_url()
        #BasePage(cls.driver).refresh_page()
        HomePage(cls.driver).quick_entrance("Customers","C000088923",2)

    # def test_01_Identifier_new(self):
    #     u"""new identifier"""
    #     CustomerRecordPage(self.driver).switch_tab("Entity")
    #     CustomerRecordPage(self.driver).entity_operator("Business Identifiers", "New", "")
    #     self.assertTrue(CustomerRecordPage(self.driver).operator_identifier("SSN","123456789"))
    #
    # def test_02_Identifier_detail(self):
    #     u"""show identifier detail"""
    #     CustomerRecordPage(self.driver).entity_operator("Business Identifiers", "Detail", "1")
    #     self.assertTrue(CustomerRecordPage(self.driver).detail_history("Detail"))
    #
    # def test_03_Identifier_edit(self):
    #     u"""edit identifier"""
    #     CustomerRecordPage(self.driver).entity_operator("Business Identifiers", "Edit", "1")
    #     self.assertTrue(CustomerRecordPage(self.driver).operator_identifier("State Tax ID","111111"))
    #
    # def test_04_Identifier_delete(self):
    #     u"""delete identifier"""
    #     CustomerRecordPage(self.driver).entity_operator("Business Identifiers", "Delete", "1")
    #     self.assertTrue(CustomerRecordPage(self.driver).delete())

    def test_05_Identifier_history(self):
        u"""show identifier history"""
        CustomerRecordPage(self.driver).switch_tab("Entity")
        CustomerRecordPage(self.driver).entity_operator("Business Identifiers", "History", "")
        self.assertTrue(CustomerRecordPage(self.driver).delete())

    # def test_06_Address_new(self):
    #     u"""new address"""
    #     CustomerRecordPage(self.driver).entity_operator("Addresses", "New", "")
    #     self.assertTrue(CustomerRecordPage(self.driver).operator_identifier("SSN","123456789"))
    #
    # def test_07_Address_detail(self):
    #     u"""show address detail"""
    #     CustomerRecordPage(self.driver).entity_operator("Addresses", "Detail", "1")
    #     self.assertTrue(CustomerRecordPage(self.driver).detail_history("Detail"))
    #
    # def test_08_Address_edit(self):
    #     u"""edit address"""
    #     CustomerRecordPage(self.driver).entity_operator("Addresses", "Edit", "1")
    #     self.assertTrue(CustomerRecordPage(self.driver).detail_history("Detail"))
    #
    # def test_09_Address_delete(self):
    #     u"""delete address"""
    #     CustomerRecordPage(self.driver).entity_operator("Addresses", "Delete", "1")
    #     self.assertTrue(CustomerRecordPage(self.driver).delete())

    def test_10_Address_history(self):
        u"""show address history"""
        CustomerRecordPage(self.driver).entity_operator("Addresses", "History", "")
        self.assertTrue(CustomerRecordPage(self.driver).detail_history("History"))

