#-*- coding: UTF-8 -*-
import unittest
from getdata.ExcelPointer import excelHandle
from utils.query_sql import dbConnect
from utils.browser_engine import driver
from pageobjects.homepage.homePage import  HomePage
from utils.base_page import BasePage
from pageobjects.land.landCommon import LandCommonPage
from pageobjects.land.Summary import SummaryPage

filepath = "E:\\Automation\\UI\\getdata\\TestData.xlsx"
sheetName = "LandDictionaryList"
class landSection(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = driver
        HomePage(cls.driver).quick_entrance("Land", "04-019662", 2)
        BasePage(cls.driver).switch_to_handle(1)

    def test_01_CountySeat_new(self):
        u"""new CountySeat"""
        LandCommonPage(self.driver).switch_tab("Location")
        direction = dbConnect().getdata(*(excelHandle(filepath,sheetName).read_excel("Direction from Seat")))
        deviation = dbConnect().getdata(*(excelHandle(filepath,sheetName).read_excel("Deviation from Seat")))
        LandCommonPage(self.driver).special_operator("Location From County Seat", "Edit", "")
        self.assertTrue(SummaryPage(self.driver).locationCountySeat(direction,deviation))

    def test_02_CountySeat_history(self):
      u"""CountySeat History"""
      self.assertTrue(LandCommonPage(self.driver).special_operator("Location From County Seat","History","1"))

    def test_03_CountySeat_edit(self):
        u"""edit CountySeat"""
        direction = dbConnect().getdata(*(excelHandle(filepath, sheetName).read_excel("Direction from Seat")))
        deviation = dbConnect().getdata(*(excelHandle(filepath, sheetName).read_excel("Deviation from Seat")))
        LandCommonPage(self.driver).special_operator("Location From County Seat", "Edit", "")
        self.assertTrue(SummaryPage(self.driver).locationCountySeat(direction,deviation))

    def test_04_Location_required(self):
        u"""Location required"""
        LandCommonPage(self.driver).special_operator("Location", "Edit", "")
        self.assertTrue(LandCommonPage(self.driver).required_validation())

    def test_05_Location_new(self):
        u"""new Location"""
        legalAccess = dbConnect().getdata(*(excelHandle(filepath,sheetName).read_excel("Legal Access Indicator")))
        withinCity = dbConnect().getdata(*(excelHandle(filepath,sheetName).read_excel("Within City Indicator")))
        LandCommonPage(self.driver).special_operator("Location", "Edit", "")
        self.assertTrue(SummaryPage(self.driver).location("Abbott",legalAccess,withinCity))

    def test_06_CountySeat_history(self):
      u"""Location History"""
      self.assertTrue(LandCommonPage(self.driver).special_operator("Location","History","1"))

    def test_07_CountySeat_edit(self):
        u"""edit Location"""
        legalAccess = dbConnect().getdata(*(excelHandle(filepath, sheetName).read_excel("Legal Access Indicator")))
        withinCity = dbConnect().getdata(*(excelHandle(filepath, sheetName).read_excel("Within City Indicator")))
        LandCommonPage(self.driver).special_operator("Location", "Edit", "")
        self.assertTrue(SummaryPage(self.driver).location("Abbott", legalAccess, withinCity))

