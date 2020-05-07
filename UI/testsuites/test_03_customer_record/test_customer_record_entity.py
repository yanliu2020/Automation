#-*- coding: UTF-8 -*-

import datetime
import unittest
from utils.browser_engine import driver
from utils.base_page import  BasePage
from config.customer.customer_record_entity import CustomerRecordEntity
from pageobjects.homepage.homePage import  HomePage
from pageobjects.customer.customerRecord import CustomerRecordPage

nowTime = datetime.datetime.now().strftime("%Y/%m/%d %H:%M:%S")

class Customer_Record(unittest.TestCase):

    # 初始化，打开浏览器，并进行登录(实例化)
    @classmethod
    def setUpClass(cls):
        cls.driver = driver
        HomePage(cls.driver).quick_entrance("Customers","C000088898",2)

    def test_01_DBA_new(self):
        u"""new a DBA"""
        CustomerRecordPage(self.driver).switch_tab("Entity")
        CustomerRecordPage(self.driver).entity_operator("Doing Business As (DBA)", "New", "")
        self.assertTrue(CustomerRecordPage(self.driver).input_DBA_Website("alias", "UIAutomation"+nowTime))

    def test_02_query_summary(self):
        u"""show summary"""
        CustomerRecordPage(self.driver).switch_tab("Summary")

    def test_03_DBA_detail(self):
        u"""query DBA detail"""
        CustomerRecordPage(self.driver).switch_tab("Entity")
        CustomerRecordPage(self.driver).entity_operator("Doing Business As (DBA)","Details","1")
        self.assertTrue(CustomerRecordPage(self.driver).detail_history("Details"))


    # def test_03_DBA_edit(self):
    #     u"""edit DBA"""
    #     CustomerRecordPage(self.driver).switch_tab("Entity")
    #     CustomerRecordPage(self.driver).entity_operator("Doing Business As (DBA)","Edit","1")
    #     self.assertTrue(CustomerRecordPage(self.driver).input_DBA_Website("alias", "UIAutomationEdit"+nowTime))

    def test_04_DBA_delete(self):
        u"""delete DBA"""
        CustomerRecordPage(self.driver).switch_tab("Entity")
        CustomerRecordPage(self.driver).entity_operator("Doing Business As (DBA)","Delete","2")
        self.assertTrue(CustomerRecordPage(self.driver).delete())

    # def test_05_DBA_history(self):
    #     u"""show DBA history"""
    #     CustomerRecordPage(self.driver).switch_tab("Entity")
    #     CustomerRecordPage(self.driver).entity_operator("Doing Business As (DBA)","History","")
    #     self.assertTrue(CustomerRecordPage(self.driver).detail_history("History"))

    def test_06_Websites_new(self):
        u"""new Websites"""
        CustomerRecordPage(self.driver).entity_operator("Websites","New","")
        self.assertTrue(CustomerRecordPage(self.driver).input_DBA_Website("url","https://www.uiautomation.com"))

    def test_07_Websites_detail(self):
        u"""show Websites details"""
        CustomerRecordPage(self.driver).entity_operator("Websites","Details","1")
        self.assertTrue(CustomerRecordPage(self.driver).detail_history("Details"))

    def test_08_Websites_edit(self):
        u"""edit Websites"""
        CustomerRecordPage(self.driver).entity_operator("Websites", "Edit", "1")
        self.assertTrue(CustomerRecordPage(self.driver).input_DBA_Website("url", "https://www.uiautomationEdit.com"))

    def test_09_Websites_delete(self):
        u"""delete Websites"""
        CustomerRecordPage(self.driver).entity_operator("Websites", "Delete", "1")
        self.assertTrue(CustomerRecordPage(self.driver).delete())

    def test_10_Websites_history(self):
        u"""show Websites history"""
        CustomerRecordPage(self.driver).entity_operator("Websites", "History", "")
        self.assertTrue(CustomerRecordPage(self.driver).detail_history("History"))






