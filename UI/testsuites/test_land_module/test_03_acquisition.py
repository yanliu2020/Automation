#-*- coding: UTF-8 -*-
import unittest
from getdata.ExcelPointer import excelHandle
from utils.query_sql import dbConnect
from utils.basepath_helper import excel_path
from utils.browser_engine import driver
from pageobjects.common.topMenu import TopMenuPage
from pageobjects.land.landCommon import LandCommonPage
from pageobjects.land.acquisition import AcquisitionPage

filepath = excel_path +"TestData.xlsx"
sheetName = "LandDictionaryList"
class LandAcquisition(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = driver
        TopMenuPage(cls.driver).select_multiple_menu(3, "land", "New", "Acquisition", "")

    def test_01_Acquisition_required(self):
        u"""top new Acquisition required"""
        # LandCommonPage(self.driver).top_operate("Acquisition Land", "Actions ", "New")
        self.assertTrue(LandCommonPage(self.driver).required_validation())

    def test_02_New_Acquisition(self):
        u"""new Acquisition"""
        acquisitionClass = dbConnect().getdata(*(excelHandle(filepath,sheetName).read_excel("acquisitionClass")))
        acquisitionMethod = dbConnect().getdata(*(excelHandle(filepath, sheetName).read_excel("acquisitionMethod")))
        self.assertTrue(
            AcquisitionPage(self.driver).Acquisition(acquisitionClass,acquisitionMethod))

    def test_03_edit_Acquisition(self):
        u"""edit Acquisition"""
        LandCommonPage(self.driver).top_operate("Acquisition Land","Actions ","Edit")
        acquisitionClass = dbConnect().getdata(*(excelHandle(filepath, sheetName).read_excel("acquisitionClass")))
        acquisitionMethod = dbConnect().getdata(*(excelHandle(filepath, sheetName).read_excel("acquisitionMethod")))
        self.assertTrue(
            AcquisitionPage(self.driver).Acquisition(acquisitionClass, acquisitionMethod))

    def test_04_delete_Acquisition(self):
        u"""delete Acquisition"""
        self.assertTrue(LandCommonPage(self.driver).top_operate("Acquisition Land","Actions ","Delete"))


