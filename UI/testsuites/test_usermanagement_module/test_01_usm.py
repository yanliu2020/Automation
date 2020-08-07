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

    def test_01_role_new(self):
        u"""new role"""
        UsmPage(self.driver).click_button("Roles", "New","")
        capabilityNamelist = ['Business Entity','Business Entity Contact']
        self.assertTrue(UsmPage(self.driver).operation("Roles","New",capabilityNamelist))

    def test_02_role_edit(self):
        u"""edit role"""
        UsmPage(self.driver).click_button("Roles", "Edit","1")
        capabilityNamelist = ['Business Entity', 'Business Entity Alias']
        self.assertTrue(UsmPage(self.driver).operation("Roles","Edit",capabilityNamelist))

    # def test_03_role_inactivate(self):
    #     u"""inactivate role"""
    #     UsmPage(self.driver).click_button("Roles", "inactivate","1")
    #     self.assertTrue(UsmPage(self.driver).operation("inactivate"))

    def test_04_user_edit(self):
        u"""edit a user"""
        UsmPage(self.driver).switch_tab("Users")
        UsmPage(self.driver).click_button("Users", "Edit","1")
        self.assertTrue(UsmPage(self.driver).operation("Users","Edit"))