#-*- coding: UTF-8 -*-
import unittest
from getdata.ExcelPointer import excelHandle
from utils.query_sql import dbConnect
from utils.basepath_helper import excel_path
from utils.browser_engine import driver
from pageobjects.common.topMenu import TopMenuPage
from pageobjects.land.landCommon import LandCommonPage
from pageobjects.land.appraisal import AppraisalPage

filepath = excel_path +"TestData.xlsx"
sheetName = "LandDictionaryList"
class landAppraisal(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = driver
        TopMenuPage(cls.driver).select_multiple_menu(3, "land", "New", "Appraisal", "")

    def test_01_required(self):
        u"""top new Appraisal required"""
        # LandCommonPage(self.driver).top_operate("Land Appraisals","Actions ","New")
        self.assertTrue(LandCommonPage(self.driver).required_validation())

    def test_02_New_Appraisal(self):
        u"""new Appraisal"""
        source = dbConnect().getdata(*(excelHandle(filepath,sheetName).read_excel("source")))
        estimatedValueMethod = dbConnect().getdata(*(excelHandle(filepath, sheetName).read_excel("estimatedValueMethod")))
        self.assertTrue(AppraisalPage(self.driver).Appraisal(source,estimatedValueMethod))

    def test_03_edit_Appraisal(self):
        u"""edit Appraisal"""
        LandCommonPage(self.driver).top_operate("Land Appraisals","Actions ","Edit")
        source = dbConnect().getdata(*(excelHandle(filepath,sheetName).read_excel("source")))
        estimatedValueMethod = dbConnect().getdata(*(excelHandle(filepath, sheetName).read_excel("estimatedValueMethod")))
        self.assertTrue(AppraisalPage(self.driver).Appraisal(source,estimatedValueMethod))

    def test_04_delete_Appraisal(self):
        u"""delete Appraisal"""
        self.assertTrue(LandCommonPage(self.driver).top_operate("Land Appraisals","Actions ","Delete"))

    def test_05_relate_land(self):
        u"""relate Appraisal to land"""
        LandCommonPage(self.driver).switch_tab("Land Appraisals","Lands")
        LandCommonPage(self.driver).entity_operator("Land Appraisals", "Lands","Relate","","")


