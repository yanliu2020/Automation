#-*- coding: UTF-8 -*-
import datetime
import unittest
from utils.browser_engine import driver
from pageobjects.common.topMenu import TopMenuPage
from pageobjects.usm.usm import UsmPage

nowTime = datetime.datetime.now().strftime("%Y/%m/%d %H:%M:%S")

class USM(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = driver
        TopMenuPage(cls.driver).select_multiple_menu(2, "manage", "Authorization Management", "", "")

    def test_01_noCapability_assignOneUser(self):
        u"""new role: noCapability_assignOneUser"""
        UsmPage(self.driver).click_button("Roles", "New","")
        capabilityNamelist = ['']
        self.assertTrue(UsmPage(self.driver).operation("add",1,"Roles","New",capabilityNamelist))

    def test_02_cancelCapability_removeOneUser(self):
        u"""edit role:cancelCapability_removeOneUser"""
        UsmPage(self.driver).click_button("Roles", "Edit","1")
        capabilityNamelist = ['Business Entity']
        self.assertTrue(UsmPage(self.driver).operation("remove",1,"Roles","Edit",capabilityNamelist))

    def test_03_addCapability_assignMultiUsers(self):
        u"""new role:addCapability_assignMultiUsers"""
        UsmPage(self.driver).click_button("Roles", "New","")
        capabilityNamelist = ['Business Entity']
        self.assertTrue(UsmPage(self.driver).operation("add",2,"Roles","New",capabilityNamelist))

    def test_04_addMultiCapability_removeMultiUser(self):
        u"""edit role:addMultiCapability_removeMultiUser"""
        UsmPage(self.driver).click_button("Roles", "Edit","1")
        capabilityNamelist = ['Business Entity', 'Business Entity Alias']
        self.assertTrue(UsmPage(self.driver).operation("remove","","Roles","Edit",capabilityNamelist))

    # # def test_03_role_inactivate(self):
    # #     u"""inactivate role"""
    # #     UsmPage(self.driver).click_button("Roles", "inactivate","1")
    # #     self.assertTrue(UsmPage(self.driver).operation("inactivate"))

    def test_04_user_edit(self):
        u"""edit a user"""
        UsmPage(self.driver).switch_tab("Users")
        UsmPage(self.driver).click_button("Users", "Edit","1")
        self.assertTrue(UsmPage(self.driver).operation("Users","Edit"))