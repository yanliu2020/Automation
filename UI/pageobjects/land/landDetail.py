# -*- coding: utf-8 -*-
import random
from  utils.base_page import  BasePage
from config.land.land_details_entity import LandDetailsEntity
from config.land.land_common_entity import LandCommonEntity
from pageobjects.land.landCommon import LandCommonPage

class LandDetailPage(BasePage):
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

    def SaleDetails(self,multiTractSaleIndicator,reservationEasement):
        self.ctrl_all(LandCommonEntity().get_field_input("minimumBidAmount"))
        self.type(LandCommonEntity().get_field_input("minimumBidAmount"), BasePage(self.driver).randomData("number", 2))
        self.ctrl_all(LandCommonEntity().get_field_textarea("multiTractComment"))
        self.type(LandCommonEntity().get_field_textarea("multiTractComment"), BasePage(self.driver).randomData("string", 6))
        self.drop_select(LandCommonEntity().get_field_select("multiTractSale"), multiTractSaleIndicator)
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

    def locationCountySeat(self,directionFromCountySeat,deviationFromCountySeat):
        self.drop_select(LandCommonEntity().get_field_select("direction"),directionFromCountySeat)
        self.ctrl_all(LandCommonEntity().get_input_special("distance"))
        self.type(LandCommonEntity().get_input_special("distance"), BasePage(self.driver).randomData("number", 1))
        self.drop_select(LandCommonEntity().get_field_select("deviation"), deviationFromCountySeat)
        self.ctrl_all(LandCommonEntity().get_input_special("degree"))
        self.type(LandCommonEntity().get_input_special("degree"), BasePage(self.driver).randomData("number", 1))
        self.click(LandCommonEntity().get_land_button("Save"))
        if 'successfully' in LandCommonPage(self.driver).get_tips_msg():
            return True
        else:
            return False

    def location(self,legalAccessIndicator,withinCityIndicator):
        self.ctrl_all(LandCommonEntity().get_input_special("street1"))
        self.type(LandCommonEntity().get_input_special("street1"),
                  BasePage(self.driver).randomData("string", 6))
        self.ctrl_all(LandCommonEntity().get_textarea_specail("directions"))
        self.type(LandCommonEntity().get_textarea_specail("directions"),
                  BasePage(self.driver).randomData("string", 6))
        self.drop_select(LandCommonEntity().get_field_select("legalAccess"), legalAccessIndicator)
        self.drop_select(LandCommonEntity().get_field_select("withinCity"), withinCityIndicator)
        self.click(LandCommonEntity().get_land_button("Save"))
        if 'successfully' in LandCommonPage(self.driver).get_tips_msg():
            return True
        else:
            return False

    def characteristics(self,improvementsIndicator,utilitiesAvailableIndicator):
        self.drop_select(LandCommonEntity().get_field_select("hasImprovements"), improvementsIndicator)
        self.ctrl_all(LandCommonEntity().get_input_special("topography"))
        self.type(LandCommonEntity().get_input_special("topography"),
                  BasePage(self.driver).randomData("string", 6))
        self.drop_select(LandCommonEntity().get_field_select("utilitiesAvailable"), utilitiesAvailableIndicator)
        self.ctrl_all(LandCommonEntity().get_input_special("zoning"))
        self.type(LandCommonEntity().get_input_special("zoning"),
                  BasePage(self.driver).randomData("string", 6))
        self.click(LandCommonEntity().get_land_button("Save"))
        if 'successfully' in LandCommonPage(self.driver).get_tips_msg():
            return True
        else:
            return False

    def dispositionPlan(self,flag,dispositionAttribute):
        if flag == 1:
            self.drop_select(LandCommonEntity().get_field_select("attributes1"), dispositionAttribute)
            self.type(LandCommonEntity().get_input_special("comment1"),
                      BasePage(self.driver).randomData("string", 6))
            self.drop_select(LandCommonEntity().get_field_select("attributes2"), dispositionAttribute)
            self.type(LandCommonEntity().get_input_special("comment2"),
                      BasePage(self.driver).randomData("string", 6))
        else:
            self.drop_select(LandCommonEntity().get_field_select("attributes"), dispositionAttribute)
            self.ctrl_all(LandCommonEntity().get_textarea_specail("comment"))
            self.type(LandCommonEntity().get_textarea_specail("comment"),
                      BasePage(self.driver).randomData("string", 6))

        self.click(LandCommonEntity().get_land_button("Save"))
        if 'successfully' in LandCommonPage(self.driver).get_tips_msg():
            return True
        else:
            return False

    def improvement(self,improvementType):
        self.drop_select(LandCommonEntity().get_field_select("type"), improvementType)
        self.ctrl_all(LandCommonEntity().get_textarea_specail("note"))
        self.type(LandCommonEntity().get_textarea_specail("note"),
                  BasePage(self.driver).randomData("string", 6))
        self.click(LandCommonEntity().get_land_button("Save"))
        if 'successfully' in LandCommonPage(self.driver).get_tips_msg():
            return True
        else:
            return False

    def encumbrance(self,encumbranceClass):
        self.drop_select(LandCommonEntity().get_field_select("encumbranceClass"), encumbranceClass)
        self.ctrl_all(LandCommonEntity().get_textarea_specail("description"))
        self.type(LandCommonEntity().get_textarea_specail("description"),
                  BasePage(self.driver).randomData("string", 6))
        self.click(LandCommonEntity().get_land_button("Save"))
        if 'successfully' in LandCommonPage(self.driver).get_tips_msg():
            return True
        else:
            return False

    def surroundingUse(self,surroundingUseClass):
        self.drop_select(LandCommonEntity().get_field_select("propertyClass"), surroundingUseClass)
        self.ctrl_all(LandCommonEntity().get_textarea_specail("note"))
        self.type(LandCommonEntity().get_textarea_specail("note"),
                  BasePage(self.driver).randomData("string", 6))
        self.click(LandCommonEntity().get_land_button("Save"))
        if 'successfully' in LandCommonPage(self.driver).get_tips_msg():
            return True
        else:
            return False

    def utilities(self,utilityType):
        self.drop_select(LandCommonEntity().get_field_select("propertyClass"), utilityType)
        self.ctrl_all(LandCommonEntity().get_textarea_specail("note"))
        self.type(LandCommonEntity().get_textarea_specail("note"),
                  BasePage(self.driver).randomData("string", 6))
        self.click(LandCommonEntity().get_land_button("Save"))
        if 'successfully' in LandCommonPage(self.driver).get_tips_msg():
            return True
        else:
            return False