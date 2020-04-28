#-*- coding: UTF-8 -*-

import datetime
import unittest
from pageobjects.common.topmenu import TopMenuPage
from utils.browser_engine import driver

nowTime = datetime.datetime.now().strftime("%Y/%m/%d %H:%M:%S")

class Logout(unittest.TestCase):

    # 初始化，打开浏览器，并进行登录(实例化)
    @classmethod
    def setUpClass(cls):
        # open browser
         #browser = BrowserEngine(cls)
        cls.driver = driver
        #TopMenuPage().get_url()

    # 退出登录
    def test_01_logout(self):

        u"""logout"""
        self.assertTrue(TopMenuPage(self.driver).logout())
