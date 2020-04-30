#-*- coding: UTF-8 -*-

import datetime
import unittest
from pageobjects.customer.newCustomer import NewCustomerPage
from utils.browser_engine import driver
from selenium import webdriver
from utils.basepath_helper import logs_path, project_path, drivers_path, config_path
from pageobjects.homepage.homePage import  HomePage
from pageobjects.customer.customerRecord import CustomerRecordPage

nowTime = datetime.datetime.now().strftime("%Y/%m/%d %H:%M:%S")

class Customer_Record(unittest.TestCase):

    # 初始化，打开浏览器，并进行登录(实例化)
    @classmethod
    def setUpClass(cls):
        cls.driver = driver
        HomePage(cls.driver).quick_operator("Customers","C000088897",2)

    # switch tab
    def test_01_customer_detail(self):
        u"""query customer detail"""
        CustomerRecordPage(self.driver).switch_tab("Entity")
        CustomerRecordPage(self.driver).entity_contacts_operator("Customer Summary"," Details")

    def test_02_query_summary(self):
        u"""query customer summary"""
        CustomerRecordPage(self.driver).switch_tab("Summary")

    def test_03_contacts_detail(self):
        u"""query contacts detail"""
        CustomerRecordPage(self.driver).switch_tab("Contacts")
        CustomerRecordPage(self.driver).entity_contacts_operator("Email", " New")

    def test_04_related_detail(self):
        u"""query related detail"""
        CustomerRecordPage(self.driver).switch_tab("Related Leases/Lands")
        CustomerRecordPage(self.driver).related_leases_operator("Mineral Leases", " Delete Relationship")




