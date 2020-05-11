#-*- coding: UTF-8 -*-

import datetime
import unittest
from pageobjects.common.topMenu import TopMenuPage
from pageobjects.customer.newCustomer import NewCustomerPage
from pageobjects.homepage.homePage import  HomePage
from utils.browser_engine import driver
from pageobjects.customer.searchCustomer import  SearchCustomerPage
from selenium import webdriver
from utils.basepath_helper import logs_path, project_path, drivers_path, config_path

nowTime = datetime.datetime.now().strftime("%Y/%m/%d %H:%M:%S")

class New_Customer(unittest.TestCase):

    # 初始化，打开浏览器，并进行登录(实例化)
    @classmethod
    def setUpClass(cls):
        # open browser
        # browser = BrowserEngine(cls)
        cls.driver = driver

        # chrome_driver_path = drivers_path + 'chromedriver.exe'
        # driverOptions = webdriver.ChromeOptions()
        # driverOptions.add_argument(r"user-data-dir=C:\Users\ElenaTang\AppData\Local\Google\Chrome\User Data")
        # print(driverOptions)
        # cls.driver = webdriver.Chrome(chrome_driver_path, 0, driverOptions)
        TopMenuPage(cls.driver).get_url()
        TopMenuPage(cls.driver).select_multiple_menu(2,"customers","New","","")


    # New Individual Customer
    def test_01_new_customer(self):

        u"""New Individual Customer"""
        NewCustomerPage(self.driver).select_customer_type("Person","Individual")




