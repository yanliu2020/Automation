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
class landSummary(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = driver
        HomePage(cls.driver).quick_entrance("Land", "04-019662", 2)
        BasePage(cls.driver).switch_to_handle(1)

    def test_01_Interest_required(self):
        u"""Interest required"""
        LandCommonPage(self.driver).entity_operator("Interest (Reservations)", "New", "","")
        self.assertTrue(LandCommonPage(self.driver).required_validation())

    def test_02_Interest_new(self):
        u"""new Interest"""
        interestClass = dbConnect().getdata(*(excelHandle(filepath,sheetName).read_excel("interestClass")))
        interestStatus = dbConnect().getdata(*(excelHandle(filepath,sheetName).read_excel("interestStatus")))
        LandCommonPage(self.driver).entity_operator("Interest (Reservations)", "New", "","")
        self.assertTrue(SummaryPage(self.driver).interest(interestClass,interestStatus))

    def test_03_Interest_details(self):
      u"""Interest Details"""
      self.assertTrue(LandCommonPage(self.driver).entity_operator("Interest (Reservations)","Details",1,1))

    def test_04_Interest_history(self):
      u"""Interest History"""
      self.assertTrue(LandCommonPage(self.driver).entity_operator("Interest (Reservations)","History",1,1))

    def test_05_Interest_edit(self):
        u"""edit Interest"""
        interestClass = dbConnect().getdata(*(excelHandle(filepath, sheetName).read_excel("interestClass")))
        interestStatus = dbConnect().getdata(*(excelHandle(filepath, sheetName).read_excel("interestStatus")))
        LandCommonPage(self.driver).entity_operator("Interest (Reservations)", "Edit", "1","")
        self.assertTrue(SummaryPage(self.driver).interest(interestClass,interestStatus))

    def test_06_Interest_delete(self):
        u"""delete Interest"""
        LandCommonPage(self.driver).entity_operator("Interest (Reservations)", "Delete", "1","")
        self.assertTrue(LandCommonPage(self.driver).delete())

    def test_07_County_required(self):
        u"""County required"""
        LandCommonPage(self.driver).entity_operator("Counties", "New", "","")
        self.assertTrue(LandCommonPage(self.driver).required_validation())

    def test_08_County_new(self):
        u"""new County"""
        county = dbConnect().getdata(*(excelHandle(filepath, sheetName).read_excel("county")))
        state = dbConnect().getdata(*(excelHandle(filepath, sheetName).read_excel("state")))
        LandCommonPage(self.driver).entity_operator("Counties", "New", "","")
        self.assertTrue(SummaryPage(self.driver).counties(county,state))

    def test_09_County_details(self):
      u"""County Details"""
      self.assertTrue(LandCommonPage(self.driver).entity_operator("Counties","Details",1,""))

    def test_10_County_history(self):
      u"""County History"""
      self.assertTrue(LandCommonPage(self.driver).entity_operator("Counties","History",1,1))

    def test_11_County_edit(self):
        u"""edit County"""
        county = dbConnect().getdata(*(excelHandle(filepath, sheetName).read_excel("county")))
        state = dbConnect().getdata(*(excelHandle(filepath, sheetName).read_excel("state")))
        LandCommonPage(self.driver).entity_operator("Counties", "Edit", "1","")
        self.assertTrue(SummaryPage(self.driver).counties(county,state))

    def test_12_County_delete(self):
        u"""delete County"""
        LandCommonPage(self.driver).entity_operator("Counties", "Delete", "1","")
        self.assertTrue(LandCommonPage(self.driver).delete())

    def test_13_Utilization_required(self):
        u"""Utilization required"""
        LandCommonPage(self.driver).switch_tab("Utilization")
        LandCommonPage(self.driver).entity_operator("Land Utilization", "New", "", "")
        self.assertTrue(LandCommonPage(self.driver).required_validation())

    def test_14_Utilization_new(self):
        u"""new Utilization"""
        utilizationClass = dbConnect().getdata(*(excelHandle(filepath, sheetName).read_excel("Utilization Class")))
        utilizationType = dbConnect().getdata(*(excelHandle(filepath, sheetName).read_excel("Utilization Type")))
        LandCommonPage(self.driver).entity_operator("Land Utilization", "New", "","")
        self.assertTrue(SummaryPage(self.driver).utilization(utilizationClass,utilizationType))

    def test_15_Utilization_details(self):
      u"""Utilization Details"""
      self.assertTrue(LandCommonPage(self.driver).entity_operator("Land Utilization","Details",1,""))

    def test_16_Utilization_history(self):
      u"""Utilization History"""
      self.assertTrue(LandCommonPage(self.driver).entity_operator("Land Utilization","History",1,1))

    def test_17_Utilization_edit(self):
        u"""edit Utilization"""
        utilizationClass = dbConnect().getdata(*(excelHandle(filepath, sheetName).read_excel("Utilization Class")))
        utilizationType = dbConnect().getdata(*(excelHandle(filepath, sheetName).read_excel("Utilization Type")))
        LandCommonPage(self.driver).entity_operator("Land Utilization", "Edit", "1","")
        self.assertTrue(SummaryPage(self.driver).utilization(utilizationClass,utilizationType))

    def test_18_Utilization_delete(self):
        u"""delete Utilization"""
        LandCommonPage(self.driver).entity_operator("Land Utilization", "Delete", "1","")
        self.assertTrue(LandCommonPage(self.driver).delete())

    def test_19_Comments_required(self):
        u"""Comments required"""
        LandCommonPage(self.driver).switch_tab("Comments")
        LandCommonPage(self.driver).entity_operator("Comments", "New", "", "")
        self.assertTrue(LandCommonPage(self.driver).required_validation())

    def test_20_Comments_new(self):
        u"""new Comments"""
        commentClass = dbConnect().getdata(*(excelHandle(filepath, sheetName).read_excel("Land Comment Class")))
        LandCommonPage(self.driver).entity_operator("Comments", "New", "","")
        self.assertTrue(SummaryPage(self.driver).comments(commentClass))

    def test_21_Comments_details(self):
      u"""Comments Details"""
      self.assertTrue(LandCommonPage(self.driver).entity_operator("Comments","Details",1,1))

    def test_22_Comments_history(self):
      u"""Comments History"""
      self.assertTrue(LandCommonPage(self.driver).entity_operator("Comments","History",1,1))

    def test_23_Comments_edit(self):
        u"""edit Comments"""
        commentClass = dbConnect().getdata(*(excelHandle(filepath, sheetName).read_excel("Land Comment Class")))
        LandCommonPage(self.driver).entity_operator("Comments", "Edit", "1","")
        self.assertTrue(SummaryPage(self.driver).comments(commentClass))

    def test_24_Comments_delete(self):
        u"""delete Comments"""
        LandCommonPage(self.driver).entity_operator("Comments", "Delete", "1","")
        self.assertTrue(LandCommonPage(self.driver).delete())

    def test_25_SaleDetails_new(self):
        u"""new SaleDetails"""
        LandCommonPage(self.driver).switch_tab("Sale")
        multiTractSale = dbConnect().getdata(
            *(excelHandle(filepath, sheetName).read_excel("Multi Tract Sale Indicator")))
        reservationEasement = dbConnect().getdata(
            *(excelHandle(filepath, sheetName).read_excel("Reservation Easement")))
        LandCommonPage(self.driver).entity_operator("Sale Details", "New", "","")
        self.assertTrue(SummaryPage(self.driver).SaleDetails(multiTractSale,reservationEasement))

    def test_26_SaleDetails_details(self):
      u"""Sale Details Details"""
      self.assertTrue(LandCommonPage(self.driver).entity_operator("Sale Details","Details",1,1))

    def test_27_SaleDetails_history(self):
      u"""SaleDetails History"""
      self.assertTrue(LandCommonPage(self.driver).entity_operator("Sale Details","History",1,1))

    def test_28_SaleDetails_edit(self):
        u"""edit SaleDetails"""
        multiTractSale = dbConnect().getdata(
            *(excelHandle(filepath, sheetName).read_excel("Multi Tract Sale Indicator")))
        reservationEasement = dbConnect().getdata(
            *(excelHandle(filepath, sheetName).read_excel("Reservation Easement")))
        LandCommonPage(self.driver).entity_operator("Sale Details", "Edit", "1","")
        self.assertTrue(SummaryPage(self.driver).SaleDetails(multiTractSale,reservationEasement))

    def test_29_SaleDetails_delete(self):
        u"""delete SaleDetails"""
        LandCommonPage(self.driver).entity_operator("Sale Details", "Delete", "1","")
        self.assertTrue(LandCommonPage(self.driver).delete())











