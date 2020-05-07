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

    def test_01_related_delete(self):
        u"""delete related relationship"""
        CustomerRecordPage(self.driver).switch_tab("Related Leases/Lands")
        CustomerRecordPage(self.driver).related_leases_operator("Mineral Leases", "Delete Relationship","")

    def test_02_related_detail(self):
        u"""delete related relationship"""
        CustomerRecordPage(self.driver).related_leases_operator("Mineral Leases", "Link Details", "")
