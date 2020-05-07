#-*- coding: UTF-8 -*-

import datetime
import unittest
from utils.browser_engine import driver
from pageobjects.homepage.homePage import  HomePage
from pageobjects.customer.customerRecord import CustomerRecordPage

nowTime = datetime.datetime.now().strftime("%Y/%m/%d %H:%M:%S")

class Customer_Record(unittest.TestCase):

    # 初始化，打开浏览器，并进行登录(实例化)
    @classmethod
    def setUpClass(cls):
        cls.driver = driver
        HomePage(cls.driver).quick_entrance("Customers","C000088898",2)

    # def test_01_contacts_new(self):
    #     u"""new a contact"""
    #     CustomerRecordPage(self.driver).switch_tab("Contacts")
    #     CustomerRecordPage(self.driver).contact_operator("Contacts", "New","")

    # def test_02_contacts_detail(self):
    #     u"""show contacts detail"""
    #     CustomerRecordPage(self.driver).contact_operator("Contacts", "Details","1")

    # def test_03_contacts_edit(self):
    #     u"""edit contact"""
    #     CustomerRecordPage(self.driver).contact_operator("Contacts", "Edit","1")

    def test_04_contacts_history(self):
        u"""query contact history"""
        CustomerRecordPage(self.driver).switch_tab("Contacts")
        CustomerRecordPage(self.driver).contact_operator("Contacts", "History","")
        self.assertTrue(CustomerRecordPage(self.driver).detail_history("History"))

    # def test_05_email_new(self):
    #     u"""new contact email"""
    #     CustomerRecordPage(self.driver).contact_operator("Email", "New","")

    # def test_06_email_detail(self):
    #     u"""show contact email detail"""
    #     CustomerRecordPage(self.driver).contact_operator("Email", "Details","1")

    # def test_07_email_edit(self):
    #     u"""edit contact email"""
    #     CustomerRecordPage(self.driver).contact_operator("Email", "Details","1")

    def test_08_email_delete(self):
        u"""delete contact email"""
        CustomerRecordPage(self.driver).contact_operator("Email", "Delete","1")
        self.assertTrue(CustomerRecordPage(self.driver).delete())

    def test_09_email_history(self):
        u"""show contact email history"""
        CustomerRecordPage(self.driver).contact_operator("Email", "History","")
        self.assertTrue(CustomerRecordPage(self.driver).detail_history("History"))

    # def test_10_phone_new(self):
    #     u"""new contact phone"""
    #     CustomerRecordPage(self.driver).contact_operator("Phone", "New","")

    # def test_11_phone_detail(self):
    #     u"""show contact phone detail"""
    #     CustomerRecordPage(self.driver).contact_operator("Phone", "Details","1")

    # def test_12_phone_edit(self):
    #     u"""edit contact phone"""
    #     CustomerRecordPage(self.driver).contact_operator("Phone", "Edit","1")

    def test_13_phone_delete(self):
        u"""delete contact phone"""
        CustomerRecordPage(self.driver).contact_operator("Phone", "Delete","1")
        self.assertTrue(CustomerRecordPage(self.driver).delete())

    def test_14_phone_history(self):
        u"""query contact phone history"""
        CustomerRecordPage(self.driver).contact_operator("Phone", "History","")
        self.assertTrue(CustomerRecordPage(self.driver).detail_history("History"))

    def test_15_contacts_delete(self):
        u"""delete contacts"""
        CustomerRecordPage(self.driver).contact_operator("Contacts", "Delete","1")
        self.assertTrue(CustomerRecordPage(self.driver).delete())


