#-*- coding: UTF-8 -*-

import datetime
import unittest
from utils.browser_engine import driver
from pageobjects.homepage.homePage import  HomePage
from pageobjects.common.topMenu import TopMenuPage
from utils.connect_sql import dbConnect
from pageobjects.customer.customerRecord import CustomerRecordPage

nowTime = datetime.datetime.now().strftime("%Y/%m/%d %H:%M:%S")

class recordContacts(unittest.TestCase):

    # 初始化，打开浏览器，并进行登录(实例化)
    @classmethod
    def setUpClass(cls):
        cls.driver = driver
        # TopMenuPage(cls.driver).is_homepage()
        # HomePage(cls.driver).quick_entrance("Customers","C000048473",2)


    def test_01_email_new(self):
        u"""new contact email"""
        CustomerRecordPage(self.driver).switch_tab("Contacts")
        emailType = dbConnect().getdata('MCDH', 'emailType')
        CustomerRecordPage(self.driver).contact_operator("Email", "New","")
        self.assertTrue(CustomerRecordPage(self.driver).operator_email(emailType,"false"))

    def test_02_email_edit(self):
        u"""edit contact email"""
        emailType = dbConnect().getdata('MCDH', 'emailType')
        CustomerRecordPage(self.driver).contact_operator("Email", "Edit","1")
        self.assertTrue(CustomerRecordPage(self.driver).operator_email(emailType, "true"))

    def test_03_email_delete(self):
        u"""delete contact email"""
        CustomerRecordPage(self.driver).contact_operator("Email", "Delete","1")
        self.assertTrue(CustomerRecordPage(self.driver).delete())

    def test_04_phone_new(self):
        u"""new contact phone"""
        phoneType = dbConnect().getdata('MCDH', 'phoneType')
        CustomerRecordPage(self.driver).contact_operator("Phone", "New","")
        self.assertTrue(CustomerRecordPage(self.driver).operator_phone(phoneType))

    def test_05_phone_edit(self):
        u"""edit contact phone"""
        phoneType = dbConnect().getdata('MCDH', 'phoneType')
        CustomerRecordPage(self.driver).contact_operator("Phone", "Edit","1")
        self.assertTrue(CustomerRecordPage(self.driver).operator_phone(phoneType))

    def test_06_phone_delete(self):
        u"""delete contact phone"""
        CustomerRecordPage(self.driver).contact_operator("Phone", "Delete","1")
        self.assertTrue(CustomerRecordPage(self.driver).delete())

    def test_07_contacts_new(self):
        u"""new a contact"""
        salutation = dbConnect().getdata('MCDH', 'salutation')
        CustomerRecordPage(self.driver).switch_tab("Contacts")
        suffix = dbConnect().getdata('MCDH', 'suffix')
        CustomerRecordPage(self.driver).contact_operator("Contacts", "New", "")
        role = dbConnect().getdata('MCDH', 'roleType')
        self.assertTrue(CustomerRecordPage(self.driver).operator_contact(salutation, suffix, role))

    def test_08_contacts_edit(self):
        u"""edit contact"""
        salutation = dbConnect().getdata('MCDH', 'salutation')
        CustomerRecordPage(self.driver).switch_tab("Contacts")
        suffix = dbConnect().getdata('MCDH', 'suffix')
        CustomerRecordPage(self.driver).contact_operator("Contacts", "Edit", "1")
        role = dbConnect().getdata('MCDH', 'roleType')
        self.assertTrue(CustomerRecordPage(self.driver).operator_contact(salutation, suffix, role))

    def test_09_contacts_delete(self):
        u"""delete contacts"""
        CustomerRecordPage(self.driver).contact_operator("Contacts", "Delete","1")
        self.assertTrue(CustomerRecordPage(self.driver).delete())

    def test_10_customer_delete(self):
        u"""delete customer"""
        CustomerRecordPage(self.driver).top_operate("Actions ", "Delete")
        self.assertTrue(CustomerRecordPage(self.driver).delete())




