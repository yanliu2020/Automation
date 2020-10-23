#-*- coding: UTF-8 -*-
import unittest
import  ddt
from getdata.ExcelUtil import  excelHandle
from utils.basepath_helper import excel_path
from utils.browser_engine import driver
from pageobjects.land.landDownload import LandDownLoad
from utils.base_page import BasePage
filepath = excel_path +"TestData.xlsx"
sheetName = "Land_Forms"
sheetName2 = "Land_Reports"
@ddt.ddt
class DownLoad(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        #browser = BrowserEngine(cls)
        cls.driver = driver

    data = excelHandle(filepath, sheetName).read_excel()
    @ddt.data(*data)
    def test_Inventory_Update_Forms(self,data):
        u"""download forms"""
        first_menu = data['first_menu']
        second_menu = data['second_menu']
        third_menu = data['third_menu']
        four_menu = data['four_menu']
        url = data['url']
        self.assertTrue(LandDownLoad(self.driver).download(4, first_menu, second_menu, third_menu, four_menu, url))

    data2 = excelHandle(filepath, sheetName2).read_excel()
    @ddt.data(*data2)
    def test_Reports(self, data):
        u"""download reports"""
        first_menu = data['first_menu']
        second_menu = data['second_menu']
        third_menu = data['third_menu']
        url = data['url']
        self.assertTrue(
            LandDownLoad(self.driver).download(3,first_menu,second_menu, third_menu,"", url))
        BasePage(self.driver).switch_to_handle(1)
        BasePage(self.driver).close_current_window()