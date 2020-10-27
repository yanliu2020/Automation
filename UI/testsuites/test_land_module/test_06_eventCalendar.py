#-*- coding: UTF-8 -*-
import unittest
from getdata.ExcelPointer import excelHandle
from utils.query_sql import dbConnect
from utils.basepath_helper import excel_path
from utils.browser_engine import driver
from pageobjects.common.topMenu import TopMenuPage
from pageobjects.land.landCommon import LandCommonPage
from pageobjects.land.eventCalendar import EventCalendarPage

filepath = excel_path +"TestData.xlsx"
sheetName = "LandDictionaryList"
class landEventCalendar(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = driver
        TopMenuPage(cls.driver).select_multiple_menu(3, "land", "New", "Event Calendar", "")

    def test_01_required(self):
        u"""top new Appraisal required"""
        # LandCommonPage(self.driver).top_operate("Event Calendar", "Actions ", "New")
        self.assertTrue(LandCommonPage(self.driver).required_validation())

    def test_01_new(self):
        u"""new EventCalendar"""
        eventType = dbConnect().getdata(*(excelHandle(filepath,sheetName).read_excel("eventType")))
        self.assertTrue(EventCalendarPage(self.driver).EventCalendar(eventType))

    def test_03_edit(self):
        u"""edit EventCalendar"""
        LandCommonPage(self.driver).top_operate("Event Calendar","Actions ","Edit")
        eventType = dbConnect().getdata(*(excelHandle(filepath, sheetName).read_excel("eventType")))
        self.assertTrue(EventCalendarPage(self.driver).EventCalendar(eventType))

    def test_04_delete(self):
        u"""delete EventCalendar"""
        self.assertTrue(LandCommonPage(self.driver).top_operate("Event Calendar","Actions ","Delete"))

    # def test_05_relate(self):
    #     u"""relate EventCalendar to land"""
    #     LandCommonPage(self.driver).switch_tab("Event Calendar","Lands")
    #     LandCommonPage(self.driver).entity_operator("Event Calendar", "Lands","Relate","","")


