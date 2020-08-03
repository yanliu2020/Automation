#-*- coding: UTF-8 -*-
import unittest
from utils.browser_engine import driver
from pageobjects.homepage.homePage import  HomePage
from pageobjects.common.topMenu import TopMenuPage
from pageobjects.customer.customerRecord import CustomerRecordPage
from pageobjects.login.login import SystemLogin

class deleteRelated(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = driver
        SystemLogin(cls.driver).switch_account('1925719012@qq.com', 'Abc1234%')
        TopMenuPage(cls.driver).is_homepage()


    def test_01_customer_query(self):
        u"""validate have no access for query"""
        HomePage(self.driver).quick_entrance("Customers", "C000048473", 2)
        self.assertTrue(CustomerRecordPage(self.driver).validate_permission())

    def test_02_customer_new(self):
        u"""validate have no access for new"""
        TopMenuPage(self.driver).select_multiple_menu(2, "customers", "New", "", "")
        self.assertTrue(CustomerRecordPage(self.driver).validate_permission())

    def test_03_customer_address(self):
        u"""validate have no access for address"""
        SystemLogin(self.driver).switch_account('tangjiu2020@163.com', 'Abc1234%')
        HomePage(self.driver).quick_entrance("Customers", "C000048473", 2)
        CustomerRecordPage(self.driver).switch_tab("Entity")
        CustomerRecordPage(self.driver).entity_operator("Addresses", "New", "")
        self.assertTrue(CustomerRecordPage(self.driver).validate_permission())
        CustomerRecordPage(self.driver).entity_operator("Addresses", "Edit", "1")
        self.assertTrue(CustomerRecordPage(self.driver).validate_permission())
        CustomerRecordPage(self.driver).entity_operator("Addresses", "Delete", "1")
        self.assertTrue(CustomerRecordPage(self.driver).validate_permission())

