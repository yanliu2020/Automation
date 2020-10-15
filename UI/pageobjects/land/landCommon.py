# -*- coding: utf-8 -*-
from  utils.base_page import  BasePage
from config.land.land_details_entity import LandDetailsEntity
from config.land.land_common_entity import LandCommonEntity
from utils.logger import logger

class LandCommonPage(BasePage):
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

    def entity_operator(self,sectionName,buttonName,row,textarea):
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
                # self.scroll_into_view(LandDetailsEntity().get_section_name(sectionName))
                if buttonName in ("New", "Relate"):
                    pass
                elif self.find_elements(LandDetailsEntity().get_section_records(section_item[0])):
                    if self.not_selected(section_item[0], row) == True:
                        self.click(LandDetailsEntity().get_select_record(section_item[0], row))
                    if buttonName in ("Details", "History"):
                        table = []
                        table_list = self.find_elements(LandDetailsEntity().get_column_value(section_item[0], row))
                        for i, item in enumerate(table_list):
                            value = item.text
                            table.append(value)
                        print("#####")
                        print(table)
                        print("#####")
                        self.click(LandDetailsEntity().get_section_operator(section_item[0], buttonName))
                        s = []
                        if buttonName == "Details":
                            input_list = self.find_elements(LandDetailsEntity.input_value)
                            for a, item in enumerate(input_list):
                                value = item.get_attribute('value')
                                s.append(value)
                            if textarea == 1:
                                for b, item in enumerate(self.find_elements(LandDetailsEntity.textarea_value)):
                                    value = item.text
                                    s.append(value)
                        else:
                            history_list = self.find_elements(LandDetailsEntity().get_history_value(row))
                            for a, item in enumerate(history_list):
                                value = item.text
                                s.append(value)
                        print("!!!!")
                        print(s)
                        print("!!!!")
                        self.sleep(2)
                        self.execute_script_click(LandCommonEntity.close)
                        if set(table) < set(s) or set(s) < set(table) or table == s:
                            return True
                        else:
                            return False
                self.click(LandDetailsEntity().get_section_operator(section_item[0], buttonName))


    def special_operator(self,sectionName,buttonName,row):
        """
        #Tabs
        :param sectionName,buttonName,row
        :return:
        """
        if self.is_land_details_page() == True:
            special_section_list = self.find_elements(LandDetailsEntity.special_section_list)
            # print(special_section_list)
            section_item = None
            for i, item in enumerate(special_section_list):
                if sectionName == item.text:
                    section_item = (i + 1, item)
                    break
            if section_item is None:
                logger.info(msg="sectionName %s not found!" % sectionName)
            else:
                # self.scroll_into_view(LandDetailsEntity().get_section_name(sectionName))
                if sectionName in ("Location From County Seat", "Locations", "Characteristics", "Management", "Uplands",
                                   "Survey"):
                    if buttonName == "History":
                        seciton_value_list = []
                        field_list = self.find_elements(LandDetailsEntity().get_section_value(section_item[0]))
                        for a, item in enumerate(field_list):
                            value = item.get_attribute('value')
                            seciton_value_list.append(value)
                        print("#####")
                        print(seciton_value_list)
                        print("#####")
                        self.click(LandDetailsEntity().get_specail_operator(section_item[0], buttonName))
                        s = []
                        history_list = self.find_elements(LandDetailsEntity().get_history_value(row))
                        for a, item in enumerate(history_list):
                            value = item.text
                            s.append(value)
                        print("!!!!")
                        print(s)
                        print("!!!!")
                        self.sleep(2)
                        self.execute_script_click(LandCommonEntity.close)
                        if set(seciton_value_list) < set(s) or set(s) < set(
                                seciton_value_list) or seciton_value_list == s:
                            return True
                        else:
                            return False
                    self.sleep(2)
                    self.click(LandDetailsEntity().get_specail_operator(section_item[0], buttonName))
                    self.sleep(2)


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

    def required_validation(self):
        self.sleep(1)
        # required_list = self.find_elements(LandCommonEntity.required_field)
        field_name_list = []
        msg_required_list = []
        # for i,item in enumerate(required_list):
        #     if item.text == "*":
        #         field_name_list.append((self.find_element(LandCommonEntity().get_field_name(i+1)).text).rstrip('*') + " is required.")
        print("1111")
        print(len(self.find_elements(LandCommonEntity.field_section)))
        print("1111")
        for i in range(1,len(self.find_elements(LandCommonEntity.field_section))):
            print("222")
            print(len(self.find_elements(LandCommonEntity().get_fields_of_section(i))))
            for j in range(1,len(self.find_elements(LandCommonEntity().get_fields_of_section(i)))):
                if  self.find_element(LandCommonEntity().get_required_name(i,j)):
                    print(len(self.find_elements(LandCommonEntity().get_fields_of_section(i))))
                    field_name_list.append((self.find_element(LandCommonEntity().get_fields_name(i,j)).text).rstrip(
                        '*') + " is required.")
        print("!!!!!")
        print(field_name_list)
        print("!!!!!")
        self.sleep(1)
        self.click(LandCommonEntity().get_land_button("Save"))
        required_message_list = self.find_elements(LandCommonEntity.required_field_message)
        for i,item in enumerate(required_message_list):
            value = item.text
            msg_required_list.append(value)
        print("#####")
        print(msg_required_list)
        print("#####")
        self.sleep(1)
        self.execute_script_click(LandCommonEntity.close)
        if  field_name_list == msg_required_list:
            return True
        else:
            return False







