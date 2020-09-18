# -*- coding: utf-8 -*-
from  utils.base_page import  BasePage
from config.land.land_details_entity import LandDetailsEntity
from config.land.land_common_entity import LandCommonEntity
from utils.logger import logger
from utils.connect_sql import dbConnect

class LandDetailsPage(BasePage):
    def is_land_details_page(self):
        if self.find_element(LandDetailsEntity.default_text):
            return True
        else:
            return False

    def switch_tab(self,tabName):
        """
        #Land Details Page Switch Tab
        :param  tabName :
        :return:
        """
        if self.is_land_details_page() == True:
            self.find_element_by_wait("xpath", LandDetailsEntity().get_record_tab(tabName))
            self.click(LandDetailsEntity().get_record_tab(tabName))

    def not_selected(self,section,row):
        """
        # Not selected record
        :param : section
        :param : row
        :return:
        """
        selected = self.find_element(
            LandDetailsEntity().get_select_record(section, row)).get_attribute('style')
        if "background" in  selected:
            pass
        else:
            return True

    def get_tips_msg(self):
        """
        # get the msg
        :return:
        """
        self.sleep(2)
        return  self.find_element(LandDetailsEntity.tips_msg).text

    def entity_operator(self,sectionName,buttonName,row):
        """
        #Tabs
        :param sectionName,buttonName,row
        :return:
        """
        if self.is_land_details_page() == True:
            section_list = self.find_elements(LandDetailsEntity.section_list)
            # print(section_list)
            section_item = None
            for i, item in enumerate(section_list):
                if sectionName == item.text:
                    section_item = (i + 1, item)
                    break
            if section_item is None:
                logger.info(msg="sectionName %s not found!" % sectionName)
            else:
                self.scroll_into_view(LandDetailsEntity().get_section_name(sectionName))
                if sectionName in ("Location From County Seat", "Locations" ,"Characteristics" ,"Management"
                   ,"Uplands" , "Survey","Location From County Seat" , "Locations" , "Characteristics" , "Management"
                    ,"Uplands" ,"Survey" ):
                    self.click(LandDetailsEntity().get_location_operator(section_item[0], buttonName))
                elif buttonName in ("New","Relate","History"):
                    self.click(LandDetailsEntity().get_section_operator(section_item[0], buttonName))
                else:
                    if self.find_elements(LandDetailsEntity().get_section_records(section_item[0])):
                        if self.not_selected(section_item[0], row) == True:
                            self.click(LandDetailsEntity().get_select_record(section_item[0], row))
                    else:
                        logger.info("sectionName %s have no record!" % sectionName)

    def delete(self):
        """
        # Execute delete
        :return:
        """
        self.sleep(1)
        self.click(LandDetailsEntity.delete_confirm)
        # msg = self.get_tips_msg()
        if "successfully" in self.get_tips_msg():
            return True
        else:
            return False

