#-*- coding: UTF-8 -*-

import datetime
import unittest
from utils.browser_engine import driver
from pageobjects.homepage.homePage import  HomePage
from pageobjects.common .topMenu import TopMenuPage
from pageobjects.customer.customerRecord import CustomerRecordPage

nowTime = datetime.datetime.now().strftime("%Y/%m/%d %H:%M:%S")

class Customer_Summary(unittest.TestCase):

    # 初始化，打开浏览器，并进行登录(实例化)
    @classmethod
    def setUpClass(cls):
        cls.driver = driver
        TopMenuPage(cls.driver).get_url()
        HomePage(cls.driver).quick_entrance("Customers","C000089009",2)

    def test_01_entrance_history(self):
        u"""show customer history"""
        CustomerRecordPage(self.driver).switch_tab("Entity")
        self.assertTrue(CustomerRecordPage(self.driver).top_operate("History",""))


    def test_02_customer_detail(self):
        u"""show customer detail"""
        CustomerRecordPage(self.driver).entity_operator("Customer Summary", "Details","")
        self.assertTrue(CustomerRecordPage(self.driver).detail_history("Details"))

    # def test_03_customer_edit(self):
    #     u"""edit customer"""
    #     CustomerRecordPage(self.driver).entity_operator("Customer Summary", "Edit", "")

    def test_04_customer_history(self):
        u"""show customer history"""
        CustomerRecordPage(self.driver).entity_operator("Customer Summary", "History", "")
        self.assertTrue(CustomerRecordPage(self.driver).detail_history("History"))


    # def test_05_customer_New(self):
    #     u"""New forward"""
    #     CustomerRecordPage(self.driver).top_operate("Actions","New")
