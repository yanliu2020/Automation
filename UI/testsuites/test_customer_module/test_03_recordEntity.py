#-*- coding: UTF-8 -*-
import datetime
import unittest
from utils.connect_sql import dbConnect
from utils.browser_engine import driver
from pageobjects.common.topMenu import TopMenuPage
from pageobjects.homepage.homePage import  HomePage
from pageobjects.customer.customerRecord import CustomerRecordPage
from utils.base_page import BasePage
nowTime = datetime.datetime.now().strftime("%Y/%m/%d %H:%M:%S")
class recordEntity(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = driver
        # HomePage(cls.driver).quick_entrance("Customers", "C000048473", 2)
        # CustomerRecordPage(cls.driver).switch_tab("Entity")

    def test_01_Address_new(self):
        u"""new address"""
        addressType = dbConnect().getdata('MCDH', 'addressType','')
        CustomerRecordPage(self.driver).switch_tab("Entity")
        stateCode = dbConnect().getdata('ALAMO', 'stateCode','')
        CustomerRecordPage(self.driver).entity_operator("Addresses", "New", "")
        self.assertTrue(CustomerRecordPage(self.driver).operator_address(addressType,stateCode))

    def test_02_Address_edit(self):
        u"""edit address"""
        CustomerRecordPage(self.driver).entity_operator("Addresses", "Edit", "1")
        addressType = dbConnect().getdata('MCDH', 'addressType','')
        stateCode = dbConnect().getdata('ALAMO', 'stateCode','')
        self.assertTrue(CustomerRecordPage(self.driver).operator_address(addressType,stateCode))

    def test_03_Address_delete(self):
        u"""delete address"""
        CustomerRecordPage(self.driver).entity_operator("Addresses", "Delete", "1")
        self.assertTrue(CustomerRecordPage(self.driver).delete())

    def test_04_Websites_new(self):
        u"""new Websites"""
        CustomerRecordPage(self.driver).entity_operator("Website", "New", "")
        self.assertTrue(CustomerRecordPage(self.driver).input_DBA_Website("url"))

    def test_05_Websites_edit(self):
        u"""edit Websites"""
        CustomerRecordPage(self.driver).entity_operator("Website", "Edit", "1")
        self.assertTrue(CustomerRecordPage(self.driver).input_DBA_Website("url"))

    def test_06_Websites_delete(self):
        u"""delete Websites"""
        CustomerRecordPage(self.driver).entity_operator("Website", "Delete", "1")
        self.assertTrue(CustomerRecordPage(self.driver).delete())

    def test_07_DBA_new(self):
        u"""new a DBA"""
        BasePage(self.driver).refresh_page()
        CustomerRecordPage(self.driver).entity_operator("Doing Business As (DBA)", "New", "")
        self.assertTrue(CustomerRecordPage(self.driver).input_DBA_Website("alias"))

    def test_08_DBA_edit(self):
        u"""edit DBA"""
        CustomerRecordPage(self.driver).entity_operator("Doing Business As (DBA)", "Edit", "1")
        self.assertTrue(CustomerRecordPage(self.driver).input_DBA_Website("alias"))

    def test_09_DBA_delete(self):
        u"""delete DBA"""
        CustomerRecordPage(self.driver).entity_operator("Doing Business As (DBA)", "Delete", "1")
        self.assertTrue(CustomerRecordPage(self.driver).delete())

    def test_10_Identifier_new(self):
        u"""new identifier"""
        type = dbConnect().getdata('MCDH', 'identifierName','')
        CustomerRecordPage(self.driver).entity_operator("Business Identifier", "New", "")
        self.assertTrue(CustomerRecordPage(self.driver).operator_identifier("new",type))

    def test_11_Identifier_edit(self):
        u"""edit identifier"""
        type = dbConnect().getdata('MCDH', 'identifierNameWithoutBan','')
        CustomerRecordPage(self.driver).entity_operator("Business Identifier", "Edit", "1")
        self.assertTrue(CustomerRecordPage(self.driver).operator_identifier("edit",type))

    def test_12_Identifier_delete(self):
        u"""delete identifier"""
        CustomerRecordPage(self.driver).entity_operator("Business Identifier", "Delete", "1")
        self.assertTrue(CustomerRecordPage(self.driver).operator_identifier("Delete",""))







