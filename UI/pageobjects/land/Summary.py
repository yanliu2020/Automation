# -*- coding: utf-8 -*-
import random
from  utils.base_page import  BasePage
from config.land.land_details_entity import LandDetailsEntity
from config.land.land_common_entity import LandCommonEntity
from pageobjects.land.landCommon import LandCommonPage

class SummaryPage(BasePage):
    def interest(self,interestClass,interestStatus):
        self.drop_select(LandCommonEntity().get_field_select("class"),interestClass)
        self.ctrl_all(LandCommonEntity().get_field_input("percent"))
        self.type(LandCommonEntity().get_field_input("percent"),BasePage(self.driver).randomData("number", 2))
        self.drop_select(LandCommonEntity().get_field_select("status"), interestStatus)
        self.ctrl_all(LandCommonEntity().get_field_textarea("comment"))
        self.type(LandCommonEntity().get_field_textarea("comment"),BasePage(self.driver).randomData("string", 6) )
        self.click(LandCommonEntity().get_land_button("Save"))
        if 'successfully' in LandCommonPage(self.driver).get_tips_msg():
            return True
        else:
            return False

    def counties(self,county,state):
        self.drop_select(LandCommonEntity().get_field_select("name"),county)
        self.drop_select(LandCommonEntity().get_field_select("state"), state)
        self.ctrl_all(LandCommonEntity().get_field_input("acres"))
        self.type(LandCommonEntity().get_field_input("acres"), BasePage(self.driver).randomData("number", 3))
        self.click(LandCommonEntity().get_land_button("Save"))
        if 'successfully' in LandCommonPage(self.driver).get_tips_msg():
            return True
        else:
            return False

    def utilization(self,utilizationClass,utilizationType):
        self.drop_select(LandCommonEntity().get_field_select("propertyClass"),utilizationClass)
        self.drop_select(LandCommonEntity().get_field_select("type"), utilizationType)
        self.ctrl_all(LandCommonEntity().get_field_input("percent"))
        self.type(LandCommonEntity().get_field_input("percent"), BasePage(self.driver).randomData("number", 2))
        self.click(LandCommonEntity().get_land_button("Save"))
        if 'successfully' in LandCommonPage(self.driver).get_tips_msg():
            return True
        else:
            return False

    def comments(self,commentClass):
        self.drop_select(LandCommonEntity().get_field_select("commentClass"),commentClass)
        self.ctrl_all(LandCommonEntity().get_field_textarea("comment"))
        self.type(LandCommonEntity().get_field_textarea("comment"), BasePage(self.driver).randomData("string", 6))
        self.click(LandCommonEntity().get_land_button("Save"))
        if 'successfully' in LandCommonPage(self.driver).get_tips_msg():
            return True
        else:
            return False

    def SaleDetails(self,multiTractSale,reservationEasement):
        self.ctrl_all(LandCommonEntity().get_field_input("minimumBidAmount"))
        self.type(LandCommonEntity().get_field_input("minimumBidAmount"), BasePage(self.driver).randomData("number", 2))
        self.ctrl_all(LandCommonEntity().get_field_textarea("multiTractComment"))
        self.type(LandCommonEntity().get_field_textarea("multiTractComment"), BasePage(self.driver).randomData("string", 6))
        self.drop_select(LandCommonEntity().get_field_select("multiTractSale"), multiTractSale)
        self.ctrl_all(LandCommonEntity().get_field_input("nearestCommunity"))
        self.type(LandCommonEntity().get_field_input("nearestCommunity"), BasePage(self.driver).randomData("string", 6))
        self.drop_select(LandCommonEntity().get_field_select("reservationEasementRequired"), reservationEasement)
        reservations_list = self.find_elements(LandDetailsEntity.reservations)
        rows = random.sample(range(1, len(reservations_list)), 3)
        for i in rows:
            self.click(LandDetailsEntity().get_reservation(i))
        self.click(LandCommonEntity().get_land_button("Save"))
        if 'successfully' in LandCommonPage(self.driver).get_tips_msg():
            return True
        else:
            return False

    def locationCountySeat(self,direction,deviation):
        self.drop_select(LandCommonEntity().get_field_select("direction"),direction)
        self.ctrl_all(LandCommonEntity().get_field_special_input("distance"))
        self.type(LandCommonEntity().get_field_special_input("distance"), BasePage(self.driver).randomData("number", 1))
        self.drop_select(LandCommonEntity().get_field_select("deviation"), deviation)
        self.ctrl_all(LandCommonEntity().get_field_special_input("degree"))
        self.type(LandCommonEntity().get_field_special_input("degree"), BasePage(self.driver).randomData("number", 1))
        self.click(LandCommonEntity().get_land_button("Save"))
        if 'successfully' in LandCommonPage(self.driver).get_tips_msg():
            return True
        else:
            return False

    def location(self,city,legalAccess,withinCity):
        # self.drop_select(LandCommonEntity().get_field_select("city"), city)
        self.drop_select(LandCommonEntity().get_field_select("legalAccess"), legalAccess)
        self.drop_select(LandCommonEntity().get_field_select("withinCity"), withinCity)
