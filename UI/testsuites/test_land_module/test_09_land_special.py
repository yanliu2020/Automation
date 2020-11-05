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
        LandCommonPage(self.driver).special("Land Details","Location From County Seat", "Edit", "","")
        self.assertTrue(LandDetailPage(self.driver).locationCountySeat(directionFromCountySeat,deviationFromCountySeat))

    def test_02_countySeat_history(self):
      u"""countySeat History"""
      self.assertTrue(LandCommonPage(self.driver).special("Land Details","Location From County Seat","History",1,1))

    def test_03_location(self):
        u"""New/Edit Location"""
        legalAccessIndicator = dbConnect().getdata(*(excelHandle(filepath,sheetName).read_excel("legalAccessIndicator")))
        withinCityIndicator = dbConnect().getdata(*(excelHandle(filepath,sheetName).read_excel("withinCityIndicator")))
        LandCommonPage(self.driver).special("Land Details","Location", "Edit", "","")
        self.assertTrue(LandDetailPage(self.driver).location(legalAccessIndicator,withinCityIndicator))

    def test_04_location_history(self):
      u"""location History"""
      self.assertTrue(LandCommonPage(self.driver).special("Land Details","Location","History",1,1))

    def test_05_characteristic(self):
        u"""New/Edit characteristic"""
        LandCommonPage(self.driver).switch_tab("Land Details", "Characteristics")
        improvementsIndicator = dbConnect().getdata(*(excelHandle(filepath,sheetName).read_excel("improvementsIndicator")))
        utilitiesAvailableIndicator = dbConnect().getdata(*(excelHandle(filepath,sheetName).read_excel("utilitiesAvailableIndicator")))
        LandCommonPage(self.driver).special("Land Details","Characteristics", "Edit", "","")
        self.assertTrue(LandDetailPage(self.driver).characteristics(improvementsIndicator,utilitiesAvailableIndicator))

    def test_06_characteristic_history(self):
      u"""characteristic History"""
      self.assertTrue(LandCommonPage(self.driver).special("Land Details","Characteristics","History",1,1))

    def test_07_dispositionPlan_new(self):
        u"""New dispositionPlan"""
        dispositionAttribute = dbConnect().getdata(*(excelHandle(filepath,sheetName).read_excel("dispositionAttribute")))
        LandCommonPage(self.driver).special("Land Details","Disposition Attributes", "New", "","")
        self.assertTrue(LandDetailPage(self.driver).dispositionPlan(1,dispositionAttribute))

    def test_08_dispositionPlan_details(self):
        u"""dispositionPlan Details"""
        self.assertTrue(LandCommonPage(self.driver).special("Land Details","Disposition Attributes","Details",1,""))

    def test_09_dispositionPlan_history(self):
        u"""dispositionPlan history"""
        self.assertTrue(LandCommonPage(self.driver).special("Land Details", "Disposition Attributes", "History", 1, 1))

    def test_10_dispositionPlan_edit(self):
        u"""edit dispositionPlan"""
        dispositionAttribute = dbConnect().getdata(*(excelHandle(filepath,sheetName).read_excel("dispositionAttribute")))
        LandCommonPage(self.driver).special("Land Details","Disposition Attributes", "Edit", "1","")
        self.assertTrue(LandDetailPage(self.driver).dispositionPlan("",dispositionAttribute))

    def test_11_dispositionPlan_delete(self):
        u"""delete dispositionPlan"""
        LandCommonPage(self.driver).special("Land Details","Disposition Attributes", "Delete", "1","")
        self.assertTrue(LandCommonPage(self.driver).delete())

    def test_12_improvement_required(self):
        u"""improvement required"""
        LandCommonPage(self.driver).special("Land Details","Improvements", "New", "","")
        self.assertTrue(LandCommonPage(self.driver).required_validation())

    def test_13_improvement_new(self):
        u"""New improvement"""
        improvementType = dbConnect().getdata(*(excelHandle(filepath,sheetName).read_excel("improvementType")))
        self.assertTrue(LandDetailPage(self.driver).improvement(improvementType))

    def test_14_improvement_details(self):
      u"""improvement Details"""
      self.assertTrue(LandCommonPage(self.driver).special("Land Details","Improvements","Details",1,""))

    def test_15_improvement_history(self):
        u"""improvement history"""
        self.assertTrue(LandCommonPage(self.driver).special("Land Details", "Improvements", "History", 1, 1))

    def test_16_improvement_edit(self):
        u"""edit improvement"""
        improvementType = dbConnect().getdata(*(excelHandle(filepath,sheetName).read_excel("improvementType")))
        LandCommonPage(self.driver).special("Land Details","Improvements", "Edit", "1","")
        self.assertTrue(LandDetailPage(self.driver).improvement(improvementType))

    def test_17_improvement_delete(self):
        u"""delete improvement"""
        LandCommonPage(self.driver).special("Land Details","Improvements", "Delete", "1","")
        self.assertTrue(LandCommonPage(self.driver).delete())

    def test_18_encumbrance_required(self):
        u"""encumbrance required"""
        LandCommonPage(self.driver).special("Land Details","Encumbrances", "New", "","")
        self.assertTrue(LandCommonPage(self.driver).required_validation())

    def test_19_encumbrance_new(self):
        u"""New encumbrance"""
        encumbranceClass = dbConnect().getdata(*(excelHandle(filepath,sheetName).read_excel("encumbranceClass")))
        self.assertTrue(LandDetailPage(self.driver).encumbrance(encumbranceClass))

    def test_20_encumbrance_details(self):
      u"""encumbrance Details"""
      self.assertTrue(LandCommonPage(self.driver).special("Land Details","Encumbrances","Details",1,""))

    def test_21_encumbrance_history(self):
        u"""encumbrance history"""
        self.assertTrue(LandCommonPage(self.driver).special("Land Details", "Encumbrances", "History", 1, 1))

    def test_22_encumbrance_edit(self):
        u"""edit encumbrance"""
        encumbranceClass = dbConnect().getdata(*(excelHandle(filepath,sheetName).read_excel("encumbranceClass")))
        LandCommonPage(self.driver).special("Land Details","Encumbrances", "Edit", "1","")
        self.assertTrue(LandDetailPage(self.driver).encumbrance(encumbranceClass))

    def test_23_encumbrance_delete(self):
        u"""delete encumbrance"""
        LandCommonPage(self.driver).special("Land Details","Encumbrances", "Delete", "1","")
        self.assertTrue(LandCommonPage(self.driver).delete())

    def test_24_surroundingUse_new(self):
        u"""New surroundingUse"""
        surroundingUseClass = dbConnect().getdata(*(excelHandle(filepath,sheetName).read_excel("surroundingUseClass")))
        LandCommonPage(self.driver).special("Land Details", "Surrounding Use", "New", "", "")
        self.assertTrue(LandDetailPage(self.driver).surroundingUse(surroundingUseClass))

    def test_25_surroundingUse_details(self):
      u"""surroundingUse Details"""
      self.assertTrue(LandCommonPage(self.driver).special("Land Details","Surrounding Use","Details",1,""))

    def test_26_surroundingUse_history(self):
        u"""surroundingUse history"""
        self.assertTrue(LandCommonPage(self.driver).special("Land Details", "Surrounding Use", "History", 1, 1))

    def test_27_surroundingUse_edit(self):
        u"""edit surroundingUse"""
        surroundingUseClass = dbConnect().getdata(*(excelHandle(filepath,sheetName).read_excel("surroundingUseClass")))
        LandCommonPage(self.driver).special("Land Details","Surrounding Use", "Edit", "1","")
        self.assertTrue(LandDetailPage(self.driver).surroundingUse(surroundingUseClass))

    def test_28_surroundingUse_delete(self):
        u"""delete surroundingUse"""
        LandCommonPage(self.driver).special("Land Details","Surrounding Use", "Delete", "1","")
        self.assertTrue(LandCommonPage(self.driver).delete())

    def test_29_utilities_required(self):
        u"""utilities required"""
        LandCommonPage(self.driver).special("Land Details","Utilities", "New", "","")
        self.assertTrue(LandCommonPage(self.driver).required_validation())

    def test_30_utilities_new(self):
        u"""New utilities"""
        utilityType = dbConnect().getdata(*(excelHandle(filepath,sheetName).read_excel("utilityType")))
        self.assertTrue(LandDetailPage(self.driver).utilities(utilityType))

    def test_31_utilities_details(self):
      u"""utilities Details"""
      self.assertTrue(LandCommonPage(self.driver).special("Land Details","Utilities","Details",1,""))

    def test_32_utilities_history(self):
        u"""utilities history"""
        self.assertTrue(LandCommonPage(self.driver).special("Land Details", "Utilities", "History", 1, 1))

    def test_33_utilities_edit(self):
        u"""edit utilities"""
        utilityType = dbConnect().getdata(*(excelHandle(filepath,sheetName).read_excel("utilityType")))
        LandCommonPage(self.driver).special("Land Details","Utilities", "Edit", "1","")
        self.assertTrue(LandDetailPage(self.driver).utilities(utilityType))

    def test_34_utilities_delete(self):
        u"""delete utilities"""
        LandCommonPage(self.driver).special("Land Details","Utilities", "Delete", "1","")
        self.assertTrue(LandCommonPage(self.driver).delete())
