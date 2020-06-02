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



