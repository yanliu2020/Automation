#-*- coding: UTF-8 -*-
import unittest
from getdata.ExcelPointer import excelHandle
from utils.query_sql import dbConnect
from utils.basepath_helper import excel_path
from utils.browser_engine import driver
from pageobjects.homepage.homePage import  HomePage
from utils.base_page import BasePage
from pageobjects.land.landCommon import LandCommonPage
from pageobjects.land.landDetail import LandDetailPage

filepath = excel_path +"TestData.xlsx"
sheetName = "LandDictionaryList"
class landDetailsSpecial(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = driver
        # HomePage(cls.driver).quick_entrance("Land", "04-019662", 2)
        # BasePage(cls.driver).switch_to_handle(1)

    def test_01_countySeat(self):
        u"""New/Edit CountySeat"""
        LandCommonPage(self.driver).switch_tab("Land Details","Location")
        directionFromCountySeat = dbConnect().getdata(*(excelHandle(filepath,sheetName).read_excel("directionFromCountySeat")))
        deviationFromCountySeat = dbConnect().getdata(*(excelHandle(filepath,sheetName).read_excel("deviationFromCountySeat")))
        LandCommonPage(self.driver).special_operator("Land Details","Location From County Seat", "Edit", "")
        self.assertTrue(LandDetailPage(self.driver).locationCountySeat(directionFromCountySeat,deviationFromCountySeat))

    def test_02_location(self):
        u"""New/Edit Location"""
        legalAccessIndicator = dbConnect().getdata(*(excelHandle(filepath,sheetName).read_excel("legalAccessIndicator")))
        withinCityIndicator = dbConnect().getdata(*(excelHandle(filepath,sheetName).read_excel("withinCityIndicator")))
        LandCommonPage(self.driver).special_operator("Land Details","Location", "Edit", "")
        self.assertTrue(LandDetailPage(self.driver).location(legalAccessIndicator,withinCityIndicator))

