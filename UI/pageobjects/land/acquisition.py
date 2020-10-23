# -*- coding: utf-8 -*-
import random
from  utils.base_page import  BasePage
from config.land.land_common_entity import LandCommonEntity
from pageobjects.land.landCommon import LandCommonPage
import time
currentDate = time.strftime('%m/%d/%Y', time.localtime(time.time()))

class AcquisitionPage(BasePage):
    def Acquisition(self,acquisitionClass,acquisitionMethod):
        self.ctrl_all(LandCommonEntity().get_field_input("acquisitionDate"))
        self.type(LandCommonEntity().get_field_input("acquisitionDate"),currentDate)
        self.enter(LandCommonEntity().get_field_input("acquisitionDate"))
        self.ctrl_all(LandCommonEntity().get_field_input("cost"))
        self.type(LandCommonEntity().get_field_input("cost"), BasePage(self.driver).randomData("number", 2))
        self.ctrl_all(LandCommonEntity().get_field_input("expenses"))
        self.type(LandCommonEntity().get_field_input("expenses"), BasePage(self.driver).randomData("number", 2))
        self.drop_select(LandCommonEntity().get_field_select("classProperty"), acquisitionClass)
        self.drop_select(LandCommonEntity().get_field_select("methodProperty"), acquisitionMethod)
        self.ctrl_all(LandCommonEntity().get_field_input("namecurrent"))
        self.type(LandCommonEntity().get_field_input("namecurrent"), BasePage(self.driver).randomData("string", 6))
        self.ctrl_all(LandCommonEntity().get_field_input("nameoriginal"))
        self.type(LandCommonEntity().get_field_input("nameoriginal"), BasePage(self.driver).randomData("string", 6))
        self.click(LandCommonEntity().get_land_button("Save"))
        if 'successfully' in LandCommonPage(self.driver).get_tips_msg():
            return True
        else:
            return False