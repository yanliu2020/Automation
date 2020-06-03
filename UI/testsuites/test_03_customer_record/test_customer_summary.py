#-*- coding: UTF-8 -*-

import datetime
import unittest
from utils.browser_engine import driver
from pageobjects.homepage.homePage import  HomePage
from pageobjects.common .topMenu import TopMenuPage
from pageobjects.customer.customerRecord import CustomerRecordPage
from pageobjects.customer.newCustomer import NewCustomerPage

nowTime = datetime.datetime.now().strftime("%Y/%m/%d %H:%M:%S")

class Customer_Summary(unittest.TestCase):

    # 初始化，打开浏览器，并进行登录(实例化)
    @classmethod
    def setUpClass(cls):
        cls.driver = driver
        # TopMenuPage(cls.driver).get_url()
        HomePage(cls.driver).quick_entrance("Customers","C000089009",2)

    def test_01_customer_edit(self):
        u"""edit customer"""
        CustomerRecordPage(self.driver).switch_tab("Entity")
        CustomerRecordPage(self.driver).entity_operator("Customer Summary", "Edit", "")
        NewCustomerPage(self.driver).business_entity("Organization", "Trust/Estate", "", "", "", "", "",
                                                     "", "UI Trust/Estate", "", "AK")
        self.assertTrue(NewCustomerPage.save())