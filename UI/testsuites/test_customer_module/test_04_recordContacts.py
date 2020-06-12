#-*- coding: UTF-8 -*-

import datetime
import unittest
from utils.browser_engine import driver
from pageobjects.homepage.homePage import  HomePage
from pageobjects.common.topMenu import TopMenuPage
from utils.base_page import BasePage
from pageobjects.customer.customerRecord import CustomerRecordPage

nowTime = datetime.datetime.now().strftime("%Y/%m/%d %H:%M:%S")

class recordContacts(unittest.TestCase):

    # 初始化，打开浏览器，并进行登录(实例化)
    @classmethod
    def setUpClass(cls):
        cls.driver = driver
        # TopMenuPage(cls.driver).get_url()
        # TopMenuPage(cls.driver).is_homepage()
        # HomePage(cls.driver).quick_entrance("Customers","C000089464",2)



    def test_01_email_new(self):
        u"""new contact email"""
        CustomerRecordPage(self.driver).switch_tab("Contacts")
        CustomerRecordPage(self.driver).contact_operator("Email", "New","")
        self.assertTrue(CustomerRecordPage(self.driver).operator_email("uiautomation@qq.com","Business","false"))

    def test_02_email_detail(self):
        u"""show contact email detail"""
        CustomerRecordPage(self.driver).contact_operator("Email", "Details","1")
        self.assertTrue(CustomerRecordPage(self.driver).detail_history("Details"))

    def test_03_email_edit(self):
        u"""edit contact email"""
        CustomerRecordPage(self.driver).contact_operator("Email", "Edit","1")
        self.assertTrue(CustomerRecordPage(self.driver).operator_email("uiautomationEdit@qq.com", "Company", "true"))

    def test_04_email_history(self):
        u"""show contact email history"""
        CustomerRecordPage(self.driver).contact_operator("Email", "History","1")
        self.assertTrue(CustomerRecordPage(self.driver).detail_history("History"))

    def test_05_email_delete(self):
        u"""delete contact email"""
        CustomerRecordPage(self.driver).contact_operator("Email", "Delete","1")
        self.assertTrue(CustomerRecordPage(self.driver).delete())

    def test_06_phone_new(self):
        u"""new contact phone"""
        CustomerRecordPage(self.driver).contact_operator("Phone", "New","")
        self.assertTrue(CustomerRecordPage(self.driver).operator_phone("Fax","111","1234567","extension"))

    def test_07_phone_detail(self):
        u"""show contact phone detail"""
        CustomerRecordPage(self.driver).contact_operator("Phone", "Details","1")
        self.assertTrue(CustomerRecordPage(self.driver).detail_history("Details"))

    def test_08_phone_edit(self):
        u"""edit contact phone"""
        CustomerRecordPage(self.driver).contact_operator("Phone", "Edit","1")
        self.assertTrue(CustomerRecordPage(self.driver).operator_phone("Home", "666", "6666666", "edit"))

    def test_09_phone_history(self):
        u"""query contact phone history"""
        CustomerRecordPage(self.driver).contact_operator("Phone", "History","1")
        self.assertTrue(CustomerRecordPage(self.driver).detail_history("History"))

    def test_10_phone_delete(self):
        u"""delete contact phone"""
        CustomerRecordPage(self.driver).contact_operator("Phone", "Delete","1")
        self.assertTrue(CustomerRecordPage(self.driver).delete())

    def test_11_contacts_new(self):
        u"""new a contact"""
        CustomerRecordPage(self.driver).switch_tab("Contacts")
        CustomerRecordPage(self.driver).contact_operator("Contacts", "New", "")
        self.assertTrue(CustomerRecordPage(self.driver).operator_contact("Mr.", "UI", "", "", "Trustee", "Accountant"))

    def test_12_contacts_detail(self):
        u"""show contacts detail"""
        CustomerRecordPage(self.driver).contact_operator("Contacts", "Details", "1")
        self.assertTrue(CustomerRecordPage(self.driver).detail_history("Details"))

    def test_13_contacts_edit(self):
        u"""edit contact"""
        CustomerRecordPage(self.driver).contact_operator("Contacts", "Edit", "1")
        self.assertTrue(CustomerRecordPage(self.driver).operator_contact("Miss", "UIedit", "", "", "et ux", "CPA"))

    def test_14_contacts_history(self):
        u"""query contact history"""
        CustomerRecordPage(self.driver).contact_operator("Contacts", "History", "1")
        self.assertTrue(CustomerRecordPage(self.driver).detail_history("History"))

    def test_15_contacts_delete(self):
        u"""delete contacts"""
        CustomerRecordPage(self.driver).contact_operator("Contacts", "Delete","1")
        self.assertTrue(CustomerRecordPage(self.driver).delete())
    #
    # def test_16_customer_delete(self):
    #     u"""delete customer"""
    #     # TopMenuPage(self.driver).is_homepage()
    #     # HomePage(self.driver).quick_entrance("Customers", "C000089568", 2)
    #     CustomerRecordPage(self.driver).top_operate("Actions ", "Delete")
    #     self.assertTrue(CustomerRecordPage(self.driver).delete())




