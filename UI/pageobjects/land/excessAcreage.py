# -*- coding: utf-8 -*-
from  utils.base_page import  BasePage
from config.land.land_common_entity import LandCommonEntity
from pageobjects.land.landCommon import LandCommonPage
import time
currentDate = time.strftime('%m/%d/%Y', time.localtime(time.time()))

class ExcessAcreagePage(BasePage):
    def ExcessAcreage(self,countyName,mineralsSoldIndicator,prefix,suffix):
        self.ctrl_all(LandCommonEntity().get_field_input("applicationDate"))
        self.type(LandCommonEntity().get_field_input("applicationDate"), currentDate)
        self.enter(LandCommonEntity().get_field_input("applicationDate"))
        self.ctrl_all(LandCommonEntity().get_field_input("appraisalDate"))
        self.type(LandCommonEntity().get_field_input("appraisalDate"), currentDate)
        self.enter(LandCommonEntity().get_field_input("appraisalDate"))
        self.ctrl_all(LandCommonEntity().get_field_input("excessAcres"))
        self.type(LandCommonEntity().get_field_input("excessAcres"),
                  BasePage(self.driver).randomData("number", 2))
        self.ctrl_all(LandCommonEntity().get_field_input("excessAcresAppliedToPurchase"))
        self.type(LandCommonEntity().get_field_input("excessAcresAppliedToPurchase"),
                  BasePage(self.driver).randomData("string", 6))
        self.ctrl_all(LandCommonEntity().get_field_input("proRataShare"))
        self.type(LandCommonEntity().get_field_input("proRataShare"),
                  BasePage(self.driver).randomData("number", 2))
        self.ctrl_all(LandCommonEntity().get_field_input("appraisalValue"))
        self.type(LandCommonEntity().get_field_input("appraisalValue"),
                  BasePage(self.driver).randomData("number", 3))
        self.ctrl_all(LandCommonEntity().get_field_input("purchaseAmount"))
        self.type(LandCommonEntity().get_field_input("purchaseAmount"),
                  BasePage(self.driver).randomData("number", 3))
        self.ctrl_all(LandCommonEntity().get_field_input("mineralPerAcre"))
        self.type(LandCommonEntity().get_field_input("mineralPerAcre"),
                  BasePage(self.driver).randomData("number", 3))
        self.ctrl_all(LandCommonEntity().get_field_input("mineralTotal"))
        self.type(LandCommonEntity().get_field_input("mineralTotal"),
                  BasePage(self.driver).randomData("number", 3))
        self.ctrl_all(LandCommonEntity().get_field_input("surfacePerAcre"))
        self.type(LandCommonEntity().get_field_input("surfacePerAcre"),
                  BasePage(self.driver).randomData("number", 3))
        self.ctrl_all(LandCommonEntity().get_field_input("surfaceTotal"))
        self.type(LandCommonEntity().get_field_input("surfaceTotal"),
                  BasePage(self.driver).randomData("number", 3))
        self.ctrl_all(LandCommonEntity().get_field_input("applicantName"))
        self.type(LandCommonEntity().get_field_input("applicantName"),
                  BasePage(self.driver).randomData("string", 6))
        self.drop_select(LandCommonEntity().get_field_select("countyName"), countyName)
        self.drop_select(LandCommonEntity().get_field_select("mineralsSoldIndicator"), mineralsSoldIndicator)
        self.drop_select(LandCommonEntity().get_field_select("baseFiles.0.filePrefix"), prefix)
        self.drop_select(LandCommonEntity().get_field_select("baseFiles.0.fileSuffix"), suffix)
        self.ctrl_all(LandCommonEntity().get_field_input("baseFiles.0.fileNumber"))
        self.type(LandCommonEntity().get_field_input("baseFiles.0.fileNumber"),
                  BasePage(self.driver).randomData("number", 6))
        self.ctrl_all(LandCommonEntity().get_field_input("baseFiles.0.fileAppendAge"))
        self.type(LandCommonEntity().get_field_input("baseFiles.0.fileAppendAge"),
                  BasePage(self.driver).randomData("number", 3))
        self.click(LandCommonEntity().get_land_button("Save"))
        if 'successfully' in LandCommonPage(self.driver).get_tips_msg():
            return True
        else:
            return False