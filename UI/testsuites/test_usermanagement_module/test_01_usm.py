#-*- coding: UTF-8 -*-
import datetime
import unittest
from utils.browser_engine import driver
from pageobjects.common.topMenu import TopMenuPage
from pageobjects.usm.usm import UsmPage

nowTime = datetime.datetime.now().strftime("%Y/%m/%d %H:%M:%S")

class USM(unittest.TestCase):

    # 初始化，打开浏览器，并进行登录(实例化)
    @classmethod
    def setUpClass(cls):
        cls.driver = driver
        TopMenuPage(cls.driver).select_multiple_menu(2, "manage", "Authorization Management", "", "")

    def test_01_role_new(self):
        u"""new role"""
        # UsmPage(self.driver).switch_tab("Roles")
        UsmPage(self.driver).operator("Roles", "Details","1")