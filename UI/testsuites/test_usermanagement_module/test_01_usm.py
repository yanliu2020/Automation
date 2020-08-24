#-*- coding: UTF-8 -*-
import unittest
from utils.browser_engine import driver
from pageobjects.usm.usm import UsmPage
from pageobjects.common.topMenu import TopMenuPage

class USM(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = driver
        TopMenuPage(cls.driver).select_multiple_menu(2, "manage", "Authorization Management", "", "")

    def test_01_noCapability_assignOneUser(self):
        u"""new role: noCapability_assignOneUser"""
        UsmPage(self.driver).click_button("Roles", "New","","")
        capabilityNamelist = []
        self.assertTrue(UsmPage(self.driver).operation("add",1,"Roles","New",capabilityNamelist))

    def test_02_cancelCapability_removeOneUser(self):
        u"""edit role:cancel Capability removeOneUser"""
        UsmPage(self.driver).click_button("Roles", "Edit","1","1")
        capabilityNamelist = ['Business Entity']
        self.assertTrue(UsmPage(self.driver).operation("remove",1,"Roles","Edit",capabilityNamelist))
        UsmPage(self.driver).click_button("Roles", "Inactivate", "1","1")
        capabilityNamelist1 = []
        self.assertTrue(UsmPage(self.driver).operation("","","Roles","Inactivate",capabilityNamelist1))

    def test_03_addCapability_assignMultiUsers(self):
        u"""new role:add Capability assignMultiUsers"""
        UsmPage(self.driver).click_button("Roles", "New","","")
        capabilityNamelist = ['Business Entity']
        self.assertTrue(UsmPage(self.driver).operation("add","","Roles","New",capabilityNamelist))

    def test_04_removeMultiCapability_removeMultiUser(self):
        u"""edit role:remove MultiCapability removeMultiUser"""
        UsmPage(self.driver).click_button("Roles", "Edit","1","1")
        capabilityNamelist = ['Business Entity', 'Business Entity Alias']
        self.assertTrue(UsmPage(self.driver).operation("remove","","Roles","Edit",capabilityNamelist))

    def test_05_role_inactivate(self):
        u"""inactivate role"""
        UsmPage(self.driver).click_button("Roles", "Inactivate","1","1")
        capabilityNamelist = []
        self.assertTrue(UsmPage(self.driver).operation("","","Roles","Inactivate",capabilityNamelist))

    def test_06_user_assign1Role(self):
        u"""edit a user"""
        UsmPage(self.driver).switch_tab("Users")
        UsmPage(self.driver).click_button("Users", "Edit","1","1")
        capabilityNamelist = []
        self.assertTrue(UsmPage(self.driver).operation("add",1,"Users","Edit",capabilityNamelist))

    def test_07_user_remove1Role(self):
        u"""edit a user"""
        UsmPage(self.driver).switch_tab("Users")
        UsmPage(self.driver).click_button("Users", "Edit","1","1")
        capabilityNamelist = []
        self.assertTrue(UsmPage(self.driver).operation("remove",1,"Users","Edit",capabilityNamelist))

    def test_08_user_assgin2Role(self):
        u"""edit a user"""
        UsmPage(self.driver).switch_tab("Users")
        UsmPage(self.driver).click_button("Users", "Edit","1","1")
        capabilityNamelist = []
        self.assertTrue(UsmPage(self.driver).operation("add","","Users","Edit",capabilityNamelist))

    def test_09_user_remove2Role(self):
        u"""edit a user"""
        UsmPage(self.driver).switch_tab("Users")
        UsmPage(self.driver).click_button("Users", "Edit","1","1")
        capabilityNamelist = []
        self.assertTrue(UsmPage(self.driver).operation("remove","","Users","Edit",capabilityNamelist))



