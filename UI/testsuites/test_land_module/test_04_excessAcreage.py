#-*- coding: UTF-8 -*-
import unittest
from getdata.ExcelPointer import excelHandle
from utils.query_sql import dbConnect
from utils.basepath_helper import excel_path
from utils.browser_engine import driver
from pageobjects.common.topMenu import TopMenuPage
from pageobjects.land.landCommon import LandCommonPage
from pageobjects.land.excessAcreage import ExcessAcreagePage

filepath = excel_path +"TestData.xlsx"
sheetName = "LandDictionaryList"
class landExcessAcreage(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = driver
        TopMenuPage(cls.driver).select_multiple_menu(3, "land", "New", "Excess Acreage", "")

    def test_01_EventCalendar_required(self):
        u"""top new ExcessAcreage required"""
        # LandCommonPage(self.driver).top_operate("Excess Acreage", "Actions ", "New")
        self.assertTrue(LandCommonPage(self.driver).required_validation())

    def test_02_New_ExcessAcreage(self):
        u"""new ExcessAcreage"""
        countyName = dbConnect().getdata(*(excelHandle(filepath,sheetName).read_excel("countyName")))
        mineralsSoldIndicator = dbConnect().getdata(*(excelHandle(filepath, sheetName).read_excel("mineralsSoldIndicator")))
        prefix = dbConnect().getdata(*(excelHandle(filepath, sheetName).read_excel("prefix")))
        suffix = dbConnect().getdata(*(excelHandle(filepath, sheetName).read_excel("suffix")))
        self.assertTrue(
            ExcessAcreagePage(self.driver).ExcessAcreage(countyName, mineralsSoldIndicator, prefix, suffix))

    def test_03_edit_EventCalendar(self):
        u"""edit ExcessAcreage"""
        LandCommonPage(self.driver).top_operate("Excess Acreage","Actions ","Edit")
        countyName = dbConnect().getdata(*(excelHandle(filepath, sheetName).read_excel("countyName")))
        mineralsSoldIndicator = dbConnect().getdata(
            *(excelHandle(filepath, sheetName).read_excel("mineralsSoldIndicator")))
        prefix = dbConnect().getdata(*(excelHandle(filepath, sheetName).read_excel("prefix")))
        suffix = dbConnect().getdata(*(excelHandle(filepath, sheetName).read_excel("suffix")))
        self.assertTrue(
            ExcessAcreagePage(self.driver).ExcessAcreage(countyName,mineralsSoldIndicator,prefix,suffix))

    def test_04_delete_EventCalendar(self):
        u"""delete ExcessAcreage"""
        self.assertTrue(LandCommonPage(self.driver).top_operate("Excess Acreage","Actions ","Delete"))


