#-*- coding: UTF-8 -*-

import datetime
import unittest
from pageobjects.common.topMenu import TopMenuPage
from pageobjects.customer.newCustomer import NewCustomerPage
from utils.browser_engine import driver
from pageobjects.customer.customerRecord import CustomerRecordPage

nowTime = datetime.datetime.now().strftime("%Y/%m/%d %H:%M:%S")

class New_Customer(unittest.TestCase):

    # 初始化，打开浏览器，并进行登录(实例化)
    @classmethod
    def setUpClass(cls):
        cls.driver = driver

        # chrome_driver_path = drivers_path + 'chromedriver.exe'
        # driverOptions = webdriver.ChromeOptions()
        # driverOptions.add_argument(r"user-data-dir=C:\Users\ElenaTang\AppData\Local\Google\Chrome\User Data")
        # print(driverOptions)
        # cls.driver = webdriver.Chrome(chrome_driver_path, 0, driverOptions)
        TopMenuPage(cls.driver).get_url()
        TopMenuPage(cls.driver).select_multiple_menu(2,"customers","New","","")


    def test_01_new_individual(self):
        u"""New Individual"""
        NewCustomerPage(self.driver).Business_Entity("Person","Individual","Miss","UI Individual","UI Last","Sr.","","","","","")
        self.assertTrue(NewCustomerPage(self.driver).save())

    def test_02_new_Household(self):
        u"""New Household"""
        CustomerRecordPage(self.driver).top_operate("Actions ","New")
        NewCustomerPage(self.driver).Business_Entity("Person", "Household", "", "", "", "", "UI Household","UI Default sort","","","")
        self.assertTrue(NewCustomerPage(self.driver).save())

    def test_03_new_Company(self):
        u"""New Company"""
        CustomerRecordPage(self.driver).top_operate("Actions ", "New")
        NewCustomerPage(self.driver).Business_Entity("Organization", "Company", "", "", "", "", "",
                                                     "", "UI Company", "Limited Liability Company", "AZ")
        self.assertTrue(NewCustomerPage(self.driver).save())

    def test_04_new_TrustEstate(self):
        u"""New Trust/Estate"""
        CustomerRecordPage(self.driver).top_operate("Actions ", "New")
        NewCustomerPage(self.driver).Business_Entity("Organization", "Trust/Estate", "", "", "", "", "",
                                                     "", "UI Trust/Estate", "", "AK")
        self.assertTrue(NewCustomerPage(self.driver).save())

    def test_05_new_related(self):
        u"""New Individual"""
        CustomerRecordPage(self.driver).top_operate("Actions ", "New")
        NewCustomerPage(self.driver).Business_Entity("Person","Individual","Miss","UI Individual","UI Last","Sr.","","","","","")
        NewCustomerPage(self.driver).Address("Address","Home", "Address", "changsha", "AK")
        NewCustomerPage(self.driver).Identifier("Identifier","SSN", "999999999")
        self.assertTrue(NewCustomerPage(self.driver).save())



