#-*- coding: UTF-8 -*-
import unittest
from getdata.ExcelPointer import excelHandle
from utils.basepath_helper import excel_path
from utils.query_sql import dbConnect
from utils.browser_engine import driver
from pageobjects.homepage.homePage import  HomePage
from utils.base_page import BasePage
from pageobjects.land.landCommon import LandCommonPage
from pageobjects.land.landDetail import LandDetailPage

filepath = excel_path +"TestData.xlsx"
sheetName = "LandDictionaryList"
class landDetails(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = driver
        HomePage(cls.driver).quick_entrance("Land", "04-019662", 2)
        BasePage(cls.driver).switch_to_handle(1)

    def test_01_Interest_required(self):
        u"""Interest required"""
        LandCommonPage(self.driver).entity_operator("Land Details","Interest (Reservations)", "New", "","")
        self.assertTrue(LandCommonPage(self.driver).required_validation())

    def test_02_Interest_new(self):
        u"""new Interest"""
        interestClass = dbConnect().getdata(*(excelHandle(filepath,sheetName).read_excel("interestClass")))
        interestStatus = dbConnect().getdata(*(excelHandle(filepath,sheetName).read_excel("interestStatus")))
        self.assertTrue(LandDetailPage(self.driver).interest(interestClass,interestStatus))

    def test_03_Interest_details(self):
      u"""Interest Details"""
      self.assertTrue(LandCommonPage(self.driver).entity_operator("Land Details","Interest (Reservations)","Details",1,1))

    def test_04_Interest_history(self):
      u"""Interest History"""
      self.assertTrue(LandCommonPage(self.driver).entity_operator("Land Details","Interest (Reservations)","History",1,1))

    def test_05_Interest_edit(self):
        u"""edit Interest"""
        interestClass = dbConnect().getdata(*(excelHandle(filepath, sheetName).read_excel("interestClass")))
        interestStatus = dbConnect().getdata(*(excelHandle(filepath, sheetName).read_excel("interestStatus")))
        LandCommonPage(self.driver).entity_operator("Land Details","Interest (Reservations)", "Edit", "1","")
        self.assertTrue(LandDetailPage(self.driver).interest(interestClass,interestStatus))

    def test_06_Interest_delete(self):
        u"""delete Interest"""
        LandCommonPage(self.driver).entity_operator("Land Details","Interest (Reservations)", "Delete", "1","")
        self.assertTrue(LandCommonPage(self.driver).delete())

    def test_07_County_required(self):
        u"""County required"""
        LandCommonPage(self.driver).entity_operator("Land Details","Counties", "New", "","")
        self.assertTrue(LandCommonPage(self.driver).required_validation())

    def test_08_County_new(self):
        u"""new County"""
        county = dbConnect().getdata(*(excelHandle(filepath, sheetName).read_excel("county")))
        state = dbConnect().getdata(*(excelHandle(filepath, sheetName).read_excel("state")))
        self.assertTrue(LandDetailPage(self.driver).counties(county,state))

    def test_09_County_details(self):
      u"""County Details"""
      self.assertTrue(LandCommonPage(self.driver).entity_operator("Land Details","Counties","Details",1,""))

    def test_10_County_history(self):
      u"""County History"""
      self.assertTrue(LandCommonPage(self.driver).entity_operator("Land Details","Counties","History",1,1))

    def test_11_County_edit(self):
        u"""edit County"""
        county = dbConnect().getdata(*(excelHandle(filepath, sheetName).read_excel("county")))
        state = dbConnect().getdata(*(excelHandle(filepath, sheetName).read_excel("state")))
        LandCommonPage(self.driver).entity_operator("Land Details","Counties", "Edit", "1","")
        self.assertTrue(LandDetailPage(self.driver).counties(county,state))

    def test_12_County_delete(self):
        u"""delete County"""
        LandCommonPage(self.driver).entity_operator("Land Details","Counties", "Delete", "1","")
        self.assertTrue(LandCommonPage(self.driver).delete())

    def test_13_Utilization_required(self):
        u"""Utilization required"""
        LandCommonPage(self.driver).switch_tab("Land Details","Utilization")
        LandCommonPage(self.driver).entity_operator("Land Details","Land Utilization", "New", "", "")
        self.assertTrue(LandCommonPage(self.driver).required_validation())

    def test_14_Utilization_new(self):
        u"""new Utilization"""
        utilizationClass = dbConnect().getdata(*(excelHandle(filepath, sheetName).read_excel("utilizationClass")))
        utilizationType = dbConnect().getdata(*(excelHandle(filepath, sheetName).read_excel("utilizationType")))
        self.assertTrue(LandDetailPage(self.driver).utilization(utilizationClass,utilizationType))

    def test_15_Utilization_details(self):
      u"""Utilization Details"""
      self.assertTrue(LandCommonPage(self.driver).entity_operator("Land Details","Land Utilization","Details",1,""))

    def test_16_Utilization_history(self):
      u"""Utilization History"""
      self.assertTrue(LandCommonPage(self.driver).entity_operator("Land Details","Land Utilization","History",1,1))

    def test_17_Utilization_edit(self):
        u"""edit Utilization"""
        utilizationClass = dbConnect().getdata(*(excelHandle(filepath, sheetName).read_excel("utilizationClass")))
        utilizationType = dbConnect().getdata(*(excelHandle(filepath, sheetName).read_excel("utilizationType")))
        LandCommonPage(self.driver).entity_operator("Land Details","Land Utilization", "Edit", "1","")
        self.assertTrue(LandDetailPage(self.driver).utilization(utilizationClass,utilizationType))

    def test_18_Utilization_delete(self):
        u"""delete Utilization"""
        LandCommonPage(self.driver).entity_operator("Land Details","Land Utilization", "Delete", "1","")
        self.assertTrue(LandCommonPage(self.driver).delete())

    def test_19_Comments_required(self):
        u"""Comments required"""
        LandCommonPage(self.driver).switch_tab("Land Details","Comments")
        LandCommonPage(self.driver).entity_operator("Land Details","Comments", "New", "", "")
        self.assertTrue(LandCommonPage(self.driver).required_validation())

    def test_20_Comments_new(self):
        u"""new Comments"""
        commentClass = dbConnect().getdata(*(excelHandle(filepath, sheetName).read_excel("commentClass")))
        self.assertTrue(LandDetailPage(self.driver).comments(commentClass))

    def test_21_Comments_details(self):
      u"""Comments Details"""
      self.assertTrue(LandCommonPage(self.driver).entity_operator("Land Details","Comments","Details",1,1))

    def test_22_Comments_history(self):
      u"""Comments History"""
      self.assertTrue(LandCommonPage(self.driver).entity_operator("Land Details","Comments","History",1,1))

    def test_23_Comments_edit(self):
        u"""edit Comments"""
        commentClass = dbConnect().getdata(*(excelHandle(filepath, sheetName).read_excel("commentClass")))
        LandCommonPage(self.driver).entity_operator("Land Details","Comments", "Edit", "1","")
        self.assertTrue(LandDetailPage(self.driver).comments(commentClass))

    def test_24_Comments_delete(self):
        u"""delete Comments"""
        LandCommonPage(self.driver).entity_operator("Land Details","Comments", "Delete", "1","")
        self.assertTrue(LandCommonPage(self.driver).delete())

    def test_25_SaleDetails_new(self):
        u"""new SaleDetails"""
        LandCommonPage(self.driver).switch_tab("Land Details","Sale")
        multiTractSaleIndicator = dbConnect().getdata(
            *(excelHandle(filepath, sheetName).read_excel("multiTractSaleIndicator")))
        reservationEasement = dbConnect().getdata(
            *(excelHandle(filepath, sheetName).read_excel("reservationEasement")))
        LandCommonPage(self.driver).entity_operator("Land Details","Sale Details", "New", "","")
        self.assertTrue(LandDetailPage(self.driver).SaleDetails(multiTractSaleIndicator,reservationEasement))

    def test_26_SaleDetails_details(self):
      u"""Sale Details Details"""
      self.assertTrue(LandCommonPage(self.driver).entity_operator("Land Details","Sale Details","Details",1,1))

    def test_27_SaleDetails_history(self):
      u"""SaleDetails History"""
      self.assertTrue(LandCommonPage(self.driver).entity_operator("Land Details","Sale Details","History",1,1))

    def test_28_SaleDetails_edit(self):
        u"""edit SaleDetails"""
        multiTractSaleIndicator = dbConnect().getdata(
            *(excelHandle(filepath, sheetName).read_excel("multiTractSaleIndicator")))
        reservationEasement = dbConnect().getdata(
            *(excelHandle(filepath, sheetName).read_excel("reservationEasement")))
        LandCommonPage(self.driver).entity_operator("Land Details","Sale Details", "Edit", "1","")
        self.assertTrue(LandDetailPage(self.driver).SaleDetails(multiTractSaleIndicator,reservationEasement))

    def test_29_SaleDetails_delete(self):
        u"""delete SaleDetails"""
        LandCommonPage(self.driver).entity_operator("Land Details","Sale Details", "Delete", "1","")
        self.assertTrue(LandCommonPage(self.driver).delete())











