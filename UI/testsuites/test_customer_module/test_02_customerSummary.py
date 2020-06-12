#-*- coding: UTF-8 -*-

import datetime
import unittest
from pageobjects.common.topMenu import TopMenuPage
from pageobjects.customer.newCustomer import NewCustomerPage
from utils.browser_engine import driver
from pageobjects.customer.customerRecord import CustomerRecordPage
from pageobjects.homepage.homePage import HomePage

nowTime = datetime.datetime.now().strftime("%Y/%m/%d %H:%M:%S")

class newCustomer(unittest.TestCase):

    # 初始化，打开浏览器，并进行登录(实例化)
    @classmethod
    def setUpClass(cls):
        cls.driver = driver
        # TopMenuPage(cls.driver).get_url()

    #
    # def test_01_new_individual(self):
    #     u"""New Individual"""
    #     TopMenuPage(cls.driver).select_multiple_menu(2, "customers", "New", "", "")
    #     NewCustomerPage(self.driver).business_entity("Person", "Individual", "Miss", "UI Individual", "UI Last", "Sr.",
    #                                                  "", "", "", "", "")
    #     NewCustomerPage(self.driver).contact(1, 1, "contact1", "contact1", "CPA", "Business", "test1@qq.com", "123",
    #                                          "4567890", "Home")
    #     self.assertTrue(NewCustomerPage(self.driver).save())
    #
    # def test_02_new_household(self):
    #     u"""New Household"""
    #     # TopMenuPage(self.driver).select_multiple_menu(2, "customers", "New", "", "")
    #     CustomerRecordPage(self.driver).top_operate("Actions ", "New")
    #     NewCustomerPage(self.driver).business_entity("Person", "Household", "", "", "", "", "UI Household",
    #                                                  "UI Default sort", "", "", "")
    #     NewCustomerPage(self.driver).contact(1, 1, "contact1", "contact1", "CPA", "Business", "test1@qq.com", "123",
    #                                          "4567890", "Home")
    #     self.assertTrue(NewCustomerPage(self.driver).save())
    #
    #
    # def test_03_new_company(self):
    #     u"""New Company"""
    #     # TopMenuPage(self.driver).select_multiple_menu(2, "customers", "New", "", "")
    #     TopMenuPage(self.driver).is_homepage()
    #     HomePage(self.driver).quick_entrance("Customers", "Add New", 0)
    #     # CustomerRecordPage(self.driver).top_operate("Actions ", "New")
    #     NewCustomerPage(self.driver).business_entity("Organization", "Company", "", "", "", "", "",
    #                                                  "", "UI Company", "Limited Liability Company", "AZ")
    #     NewCustomerPage(self.driver).contact(1, 1, "contact1", "contact1", "CPA", "Business", "test1@qq.com", "123",
    #                                          "4567890", "Home")
    #     self.assertTrue(NewCustomerPage(self.driver).save())

    def test_01_newRelateInfo(self):
        u"""New Trust/Estate"""
        TopMenuPage(self.driver).select_multiple_menu(2, "customers", "New", "", "")
        # CustomerRecordPage(self.driver).top_operate("Actions ", "New")
        NewCustomerPage(self.driver).business_entity("Person", "Sole Proprietor", "Dr.", "First", "Last", "Sr.", "",
                                                     "", "", "", "")
        NewCustomerPage(self.driver).contact(True,1, 1, "", "", "CPA", "Business", "test1@qq.com", "123",
                                             "4567890", "Home")
        NewCustomerPage(self.driver).add_phone("Phone 2", 1, 3, "111", "1111111", "Cell")
        NewCustomerPage(self.driver).add_phone("Phone 3", 1, 5, "222", "2222222", "Fax")
        NewCustomerPage(self.driver).contact(False,3, 1, "contact2", "contact2", "Agent", "Company", "test2@qq.com", "123",
                                             "4567890", "Home")
        NewCustomerPage(self.driver).add_phone("Phone 2", 3, 3, "111", "1111111", "Cell")
        NewCustomerPage(self.driver).add_phone("Phone 3", 3, 5, "222", "2222222", "Fax")
        NewCustomerPage(self.driver).address("Address", "Home", "Address", "changsha", "AK", "07311")
        NewCustomerPage(self.driver).identifier("Identifier", "SSN", "999999999")
        self.assertTrue(NewCustomerPage(self.driver).save())

    def test_02_entrance_history(self):
        u"""show customer history"""
        self.assertTrue(CustomerRecordPage(self.driver).top_operate("History", ""))

    def test_03_customer_detail(self):
        u"""show customer detail"""
        CustomerRecordPage(self.driver).switch_tab("Entity")
        CustomerRecordPage(self.driver).entity_operator("Customer Summary", "Details", "")
        self.assertTrue(CustomerRecordPage(self.driver).detail_history("Details"))

    def test_04_customer_history(self):
        u"""show customer history"""
        CustomerRecordPage(self.driver).entity_operator("Customer Summary", "History", "")
        self.assertTrue(CustomerRecordPage(self.driver).detail_history("History"))

    def test_05_customer_edit(self):
        u"""edit customer"""
        CustomerRecordPage(self.driver).entity_operator("Customer Summary", "Edit", "")
        CustomerRecordPage(self.driver).edit_entity("Organization", "Company", "", "", "", "", "",
                                                     "", "UI Edit Company", "Limited Liability Company", "AK")
        self.assertTrue(NewCustomerPage(self.driver).save())

    def test_06_customer_delete(self):
        u"""delete customer"""
        # TopMenuPage(self.driver).is_homepage()
        # HomePage(self.driver).quick_entrance("Customers", "C000089568", 2)
        CustomerRecordPage(self.driver).top_operate("Actions ", "Delete")
        self.assertTrue(CustomerRecordPage(self.driver).delete())







