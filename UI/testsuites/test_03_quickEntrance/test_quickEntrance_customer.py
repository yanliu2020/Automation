#-*- coding: UTF-8 -*-

import datetime
import unittest
from pageobjects.common.topmenu import TopMenuPage
from pageobjects.customer.newcustomer import NewCustomerPage
from utils.browser_engine import driver
from pageobjects.customer.searchpage import  SearchCustomerPage
from selenium import webdriver
from utils.basepath_helper import logs_path, project_path, drivers_path, config_path
from pageobjects.homepage.homepage import  HomePage

nowTime = datetime.datetime.now().strftime("%Y/%m/%d %H:%M:%S")

class New_Customer(unittest.TestCase):

    # 初始化，打开浏览器，并进行登录(实例化)
    @classmethod
    def setUpClass(cls):
        # open browser
        # browser = BrowserEngine(cls)
        cls.driver = driver
        # chrome_driver_path = drivers_path + 'chromedriver.exe'
        # cls.driver = webdriver.Chrome(chrome_driver_path)
        # TopMenuPage(cls.driver).get_url()
        HomePage(cls.driver).search_or_add("Customers"," Add New")


    # New Individual Customer
    def test_01_new_customer(self):

        u"""New Individual Customer"""
        NewCustomerPage(self.driver).choose_cust_type('Person','Individual')




