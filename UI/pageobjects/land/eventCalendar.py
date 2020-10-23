# -*- coding: utf-8 -*-
from  utils.base_page import  BasePage
from config.land.land_common_entity import LandCommonEntity
from pageobjects.land.landCommon import LandCommonPage
import time
CurrentDate = time.strftime('%m/%d/%Y', time.localtime(time.time()))

class EventCalendarPage(BasePage):
    def EventCalendar(self,eventType):
        self.ctrl_all(LandCommonEntity().get_field_input("eventDate"))
        self.type(LandCommonEntity().get_field_input("eventDate"),CurrentDate)
        self.enter(LandCommonEntity().get_field_input("eventDate"))
        self.ctrl_all(LandCommonEntity().get_field_input("eventName"))
        self.type(LandCommonEntity().get_field_input("eventName"), BasePage(self.driver).randomData("string", 6))
        self.drop_select(LandCommonEntity().get_field_select("eventType"), eventType)
        self.ctrl_all(LandCommonEntity().get_field_textarea("description"))
        self.type(LandCommonEntity().get_field_textarea("description"),BasePage(self.driver).randomData("string", 6))
        self.click(LandCommonEntity().get_land_button("Save"))
        if 'successfully' in LandCommonPage(self.driver).get_tips_msg():
            return True
        else:
            return False