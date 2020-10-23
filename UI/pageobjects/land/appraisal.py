# -*- coding: utf-8 -*-
from  utils.base_page import  BasePage
from config.land.land_common_entity import LandCommonEntity
from pageobjects.land.landCommon import LandCommonPage
import time
currentDate = time.strftime('%m/%d/%Y', time.localtime(time.time()))

class AppraisalPage(BasePage):
    def Appraisal(self,source,estimatedValueMethod):
        self.ctrl_all(LandCommonEntity().get_field_input("appraisalDate"))
        self.type(LandCommonEntity().get_field_input("appraisalDate"),currentDate)
        self.enter(LandCommonEntity().get_field_input("appraisalDate"))
        self.ctrl_all(LandCommonEntity().get_field_input("appraisedAcres"))
        self.type(LandCommonEntity().get_field_input("appraisedAcres"), BasePage(self.driver).randomData("number", 2))
        self.ctrl_all(LandCommonEntity().get_field_input("totalMarketValue"))
        self.type(LandCommonEntity().get_field_input("totalMarketValue"), BasePage(self.driver).randomData("number", 2))
        self.ctrl_all(LandCommonEntity().get_field_input("landValue"))
        self.type(LandCommonEntity().get_field_input("landValue"), BasePage(self.driver).randomData("number", 2))
        self.ctrl_all(LandCommonEntity().get_field_input("buildingValue"))
        self.type(LandCommonEntity().get_field_input("buildingValue"), BasePage(self.driver).randomData("number", 2))
        self.ctrl_all(LandCommonEntity().get_field_input("improvementValue"))
        self.type(LandCommonEntity().get_field_input("improvementValue"), BasePage(self.driver).randomData("number", 2))
        self.ctrl_all(LandCommonEntity().get_field_input("appraisalNumber"))
        self.type(LandCommonEntity().get_field_input("appraisalNumber"), BasePage(self.driver).randomData("number", 2))
        self.drop_select(LandCommonEntity().get_field_select("source"), source)
        self.drop_select(LandCommonEntity().get_field_select("methodProperty"),estimatedValueMethod)
        self.ctrl_all(LandCommonEntity().get_field_input("mineralValue"))
        self.type(LandCommonEntity().get_field_input("mineralValue"),BasePage(self.driver).randomData("number", 2))
        self.click(LandCommonEntity().get_land_button("Save"))
        if 'successfully' in LandCommonPage(self.driver).get_tips_msg():
            return True
        else:
            return False