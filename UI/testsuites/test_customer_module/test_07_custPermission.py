#-*- coding: UTF-8 -*-
import unittest
from utils.browser_engine import driver
from pageobjects.homepage.homePage import  HomePage
from pageobjects.common.topMenu import TopMenuPage
from pageobjects.customer.customerRecord import CustomerRecordPage
from pageobjects.login.login import SystemLogin
from utils.base_page import BasePage

class custPermission(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = driver

    def test_01_customer_query(self):
        u"""validate have no access for customer record page"""
        BasePage(self.driver).refresh_page()
        TopMenuPage(self.driver).is_homepage()
        SystemLogin(self.driver).switch_account('1925719012@qq.com', 'Abc1234%')
        HomePage(self.driver).quick_entrance("Customers", "C000048473", 2)
        self.assertTrue(CustomerRecordPage(self.driver).validate_permission())

    def test_02_customer_new(self):
        u"""validate have no access for new customer page"""
        TopMenuPage(self.driver).select_multiple_menu(2, "customers", "New", "", "")
        self.assertTrue(CustomerRecordPage(self.driver).validate_permission())

    def test_03_usm(self):
        u"""validate have no access for user management"""
        TopMenuPage(self.driver).select_multiple_menu(2, "manage", "Authorization Management", "", "")
        self.assertTrue(CustomerRecordPage(self.driver).validate_permission())
        BasePage(self.driver).close_current_window()

    def test_04_customer_address(self):
        u"""validate have no access for new/edit/delete entity"""
        SystemLogin(self.driver).switch_account('tangjiu2020@163.com', 'Abc1234%')
        HomePage(self.driver).quick_entrance("Customers", "C000048473", 2)
        BasePage(self.driver).switch_to_handle(1)
        CustomerRecordPage(self.driver).switch_tab("Entity")
        CustomerRecordPage(self.driver).entity_operator("Addresses", "New", "")
        self.assertTrue(CustomerRecordPage(self.driver).validate_permission())
        CustomerRecordPage(self.driver).entity_operator("Addresses", "Edit", "1")
        self.assertTrue(CustomerRecordPage(self.driver).validate_permission())
        CustomerRecordPage(self.driver).entity_operator("Addresses", "Delete", "1")
        self.assertTrue(CustomerRecordPage(self.driver).validate_permission())
        BasePage(self.driver).close_current_window()

