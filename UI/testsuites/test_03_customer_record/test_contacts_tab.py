#-*- coding: UTF-8 -*-

import datetime
import unittest
from utils.browser_engine import driver
from pageobjects.homepage.homePage import  HomePage
from pageobjects.common.topMenu import TopMenuPage
from utils.base_page import BasePage
from pageobjects.customer.customerRecord import CustomerRecordPage

nowTime = datetime.datetime.now().strftime("%Y/%m/%d %H:%M:%S")

class Contacts_Email_Phone(unittest.TestCase):

    # 初始化，打开浏览器，并进行登录(实例化)
    @classmethod
    def setUpClass(cls):
        cls.driver = driver
        TopMenuPage(cls.driver).get_url()
        HomePage(cls.driver).quick_entrance("Customers","C000089009",2)

    def test_01_contacts_new(self):
        u"""new a contact"""
        CustomerRecordPage(self.driver).switch_tab("Contacts")
        CustomerRecordPage(self.driver).contact_operator("Contacts", "New","")
        self.assertTrue(CustomerRecordPage(self.driver).operator_contact("Mr.","UI","","","Trustee","Accountant"))

    def test_02_contacts_detail(self):
        u"""show contacts detail"""
        CustomerRecordPage(self.driver).contact_operator("Contacts", "Details","1")
        self.assertTrue(CustomerRecordPage(self.driver).detail_history("Details"))

    def test_03_contacts_edit(self):
        u"""edit contact"""
        CustomerRecordPage(self.driver).contact_operator("Contacts", "Edit","1")
        self.assertTrue(CustomerRecordPage(self.driver).operator_contact("Miss", "UIedit", "", "", "et ux", "CPA"))

    def test_04_contacts_history(self):
        u"""query contact history"""
        CustomerRecordPage(self.driver).contact_operator("Contacts", "History","1")
        self.assertTrue(CustomerRecordPage(self.driver).detail_history("History"))

    def test_05_email_new(self):
        u"""new contact email"""
        CustomerRecordPage(self.driver).contact_operator("Email", "New","")
        self.assertTrue(CustomerRecordPage(self.driver).operator_email("uiautomation@qq.com","Business","false"))

    def test_06_email_detail(self):
        u"""show contact email detail"""
        CustomerRecordPage(self.driver).contact_operator("Email", "Details","1")
        self.assertTrue(CustomerRecordPage(self.driver).detail_history("Details"))

    def test_07_email_edit(self):
        u"""edit contact email"""
        CustomerRecordPage(self.driver).contact_operator("Email", "Edit","1")
        self.assertTrue(CustomerRecordPage(self.driver).operator_email("uiautomationEdit@qq.com", "Company", "true"))

    def test_08_email_history(self):
        u"""show contact email history"""
        CustomerRecordPage(self.driver).contact_operator("Email", "History","1")
        self.assertTrue(CustomerRecordPage(self.driver).detail_history("History"))

    def test_09_email_delete(self):
        u"""delete contact email"""
        CustomerRecordPage(self.driver).contact_operator("Email", "Delete","1")
        self.assertTrue(CustomerRecordPage(self.driver).delete())

    def test_10_phone_new(self):
        u"""new contact phone"""
        CustomerRecordPage(self.driver).contact_operator("Phone", "New","")
        self.assertTrue(CustomerRecordPage(self.driver).operator_phone("1","Fax","111","1234567","666"))

    def test_11_phone_detail(self):
        u"""show contact phone detail"""
        CustomerRecordPage(self.driver).contact_operator("Phone", "Details","1")
        self.assertTrue(CustomerRecordPage(self.driver).detail_history("Details"))

    def test_12_phone_edit(self):
        u"""edit contact phone"""
        CustomerRecordPage(self.driver).contact_operator("Phone", "Edit","1")
        self.assertTrue(CustomerRecordPage(self.driver).operator_phone("2", "Home", "666", "6666666", "111"))

    def test_13_phone_history(self):
        u"""query contact phone history"""
        CustomerRecordPage(self.driver).contact_operator("Phone", "History","1")
        self.assertTrue(CustomerRecordPage(self.driver).detail_history("History"))

    def test_14_phone_delete(self):
        u"""delete contact phone"""
        CustomerRecordPage(self.driver).contact_operator("Phone", "Delete","1")
        self.assertTrue(CustomerRecordPage(self.driver).delete())

    def test_15_contacts_delete(self):
        u"""delete contacts"""
        CustomerRecordPage(self.driver).contact_operator("Contacts", "Delete","1")
        self.assertTrue(CustomerRecordPage(self.driver).delete())


