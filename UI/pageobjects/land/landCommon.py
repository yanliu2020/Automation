# -*- coding: utf-8 -*-
from  utils.base_page import  BasePage
from config.land.land_common_entity import LandCommonEntity
from utils.logger import logger

class LandCommonPage(BasePage):
    def is_details_page(self,title):
        """
        #Details Page
        :param:title
        :return:
        """
        if self.find_element(LandCommonEntity().get_default_text(title)):
            return True
        else:
            return False

    def switch_tab(self,title,tabName):
        """
        #Details Page Switch Tab
        :param:title, tabName
        :return:
        """
        if self.is_details_page(title) == True:
            self.find_element_by_wait("xpath", LandCommonEntity().get_record_tab(tabName))
            self.click(LandCommonEntity().get_record_tab(tabName))

    def not_selected(self,section,row):
        """
        # Not selected record
        :param : section
        :param : row
        :return:
        """
        selected = self.find_element(
            LandCommonEntity().get_select_record(section, row)).get_attribute('style')
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
        return  self.find_element(LandCommonEntity.tips_msg).text

    def list_operation(self,title,sectionName,buttonName,row,textarea):
        """
        #Tabs
        :param:title,sectionName,buttonName,row,textarea
        :return:
        """
        if self.is_details_page(title) == True:
            section_list = self.find_elements(LandCommonEntity.section_list)
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
                elif self.exist_element(LandCommonEntity().get_section_records(section_item[0])):
                    if self.not_selected(section_item[0], row) == True:
                        self.click(LandCommonEntity().get_select_record(section_item[0], row))
                    if buttonName in ("Details", "History"):
                        table_field_value = []
                        table_column_list = self.find_elements(LandCommonEntity().get_column_value(section_item[0], row))
                        for i, item in enumerate(table_column_list):
                            value = item.text
                            table_field_value.append(value)
                        print("#####")
                        print(table_field_value)
                        print("#####")
                        self.click(LandCommonEntity().get_section_operator(section_item[0], buttonName))
                        dialog_field_value = []
                        if buttonName == "Details":
                            input_list = self.find_elements(LandCommonEntity.input_value)
                            for a, item in enumerate(input_list):
                                value = item.get_attribute('value')
                                dialog_field_value.append(value)
                            if textarea == 1:
                                for b, item in enumerate(self.find_elements(LandCommonEntity.textarea_value)):
                                    value = item.text
                                    dialog_field_value.append(value)
                        else:
                            history_column_list = self.find_elements(LandCommonEntity().get_history_value(row))
                            for a, item in enumerate(history_column_list):
                                value = item.text
                                dialog_field_value.append(value)
                        print("!!!!")
                        print(dialog_field_value)
                        print("!!!!")
                        self.sleep(2)
                        self.execute_script_click(LandCommonEntity.close)
                        if set(table_field_value) < set(dialog_field_value) or set(dialog_field_value) < set(table_field_value) or table_field_value == dialog_field_value:
                            return True
                        else:
                            return False
                self.click(LandCommonEntity().get_section_operator(section_item[0], buttonName))

    def delete(self):
        """
        # execute delete
        :return:
        """
        self.sleep(1)
        self.click(LandCommonEntity.delete_confirm)
        # msg = self.get_tips_msg()
        if "successfully" in self.get_tips_msg():
            return True
        else:
            return False

    def required_validation(self):
        """
        #validate the required fields
        :param:
        :return:
        """
        self.sleep(1)
        expect_message_list = []
        actual_message_list = []
        for i in range(1,len(self.find_elements(LandCommonEntity.field_section))+1):
            for j in range(1,len(self.find_elements(LandCommonEntity().get_fields_of_section(i)))+1):
                if  self.exist_element(LandCommonEntity().get_required_name(i,j)) != False:
                    if self.find_element(LandCommonEntity().get_fields_name(i,j)).text.rstrip(
                        '*') in ("Encumbrance Class","State"):
                        pass
                    else:
                        expect_message_list.append((self.find_element(LandCommonEntity().get_fields_name(i,j)).text).rstrip(
                        '*') + " is required.")
        print("!!!!!")
        print(expect_message_list)
        print("!!!!!")
        self.sleep(1)
        self.click(LandCommonEntity().get_land_button("Save"))
        actual_error_list = self.find_elements(LandCommonEntity.required_field_message)
        for i,item in enumerate(actual_error_list):
            value = item.text
            actual_message_list.append(value)
        print("#####")
        print(actual_message_list)
        print("#####")
        # self.sleep(1)
        # if flag == 1:
        #     self.execute_script_click(LandCommonEntity.close)
        # else:
        #     self.execute_script_click(LandCommonEntity().get_land_button("Cancel"))
        if  actual_message_list == expect_message_list:
            return True
        else:
            return False


    def top_operate(self,title,buttonName,acitonName):
        """
        # Action Drop List
        :param : title,buttonName,acitonName
        :return:
        """
        #self.scroll_into_view(CustomerRecordEntity().get_customer_operate(buttonName))
        if self.is_details_page(title) == True:
            self.click(LandCommonEntity().get_top_operate(buttonName))
            if buttonName == "Actions ":
                self.click(LandCommonEntity().get_actions(acitonName))
                if acitonName == "Delete":
                    self.delete()


    def summary_operation(self,title,sectionName,buttonName,row,textarea):
        """
        #Location tab, Characteristics tab,Survey tab
        :param:title,sectionName,buttonName,row,textarea
        :return:
        """
        if self.is_details_page(title) == True:
            if sectionName in ("Location From County Seat", "Location", "Characteristics", "Management", "Uplands",
                               "Survey"):
                if buttonName == "History":
                    summay_value_list = []
                    summary_field_list = self.summary_field_list(sectionName)
                    for a, item in enumerate(summary_field_list):
                        value = item.get_attribute('value')
                        summay_value_list.append(value)
                    print("#####")
                    print(summay_value_list)
                    print("#####")
                    self.choose_button(sectionName,buttonName)
                    history_value_list = []
                    history_column_list = self.find_elements(LandCommonEntity().get_history_value(row))
                    for a, item in enumerate(history_column_list):
                        value = item.text
                        history_value_list.append(value)
                    print("!!!!")
                    print(history_value_list)
                    print("!!!!")
                    self.sleep(2)
                    self.execute_script_click(LandCommonEntity.close)
                    if set(summay_value_list) < set(history_value_list) or set(history_value_list) < set(
                            summay_value_list) or summay_value_list == history_value_list:
                        return True
                    else:
                        return False
                self.sleep(2)
                self.choose_button(sectionName,buttonName)
                self.sleep(2)
            else:
                section_list = self.find_elements(LandCommonEntity.section_list)
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
                    if buttonName in ("New"):
                        pass
                    elif self.exist_element(LandCommonEntity().get_section_records(section_item[0]+1)):
                        if self.not_selected(section_item[0]+1, row) == True:
                            self.click(LandCommonEntity().get_select_record(section_item[0]+1, row))
                        if buttonName in ("Details", "History"):
                            table_field_value = []
                            table_column_list = self.find_elements(LandCommonEntity().get_column_value(section_item[0]+1, row))
                            for i, item in enumerate(table_column_list):
                                value = item.text
                                table_field_value.append(value)
                            print("#####")
                            print(table_field_value)
                            print("#####")
                            self.click(LandCommonEntity().get_section_button(section_item[0]+1, buttonName))
                            dialog_field_value = []
                            if buttonName == "Details":
                                input_list = self.find_elements(LandCommonEntity.input_value)
                                for a, item in enumerate(input_list):
                                    value = item.get_attribute('value')
                                    dialog_field_value.append(value)
                                if textarea == 1:
                                    for b, item in enumerate(self.find_elements(LandCommonEntity.textarea_value)):
                                        value = item.text
                                        dialog_field_value.append(value)
                            else:
                                history_column_list = self.find_elements(LandCommonEntity().get_history_value(row))
                                for a, item in enumerate(history_column_list):
                                    value = item.text
                                    dialog_field_value.append(value)
                            print("!!!!")
                            print(dialog_field_value)
                            print("!!!!")
                            self.sleep(2)
                            self.execute_script_click(LandCommonEntity.close)
                            if set(table_field_value) < set(dialog_field_value) or set(dialog_field_value) < set(table_field_value) or table_field_value == dialog_field_value:
                                return True
                            else:
                                return False
                    self.click(LandCommonEntity().get_section_button(section_item[0]+1, buttonName))


    def choose_button(self,sectionName,buttonName):
        """
        #The Edit, History button on Location tab, Characteristics tab,Survey tab
        :param: sectionName,buttonName
        :return:
        """
        if sectionName in ("Location From County Seat", "Characteristics", "Disposition Plan"):
            self.click(LandCommonEntity().get_left_button(buttonName))
        elif sectionName in ("Location", "Management"):
            self.click(LandCommonEntity().get_right_button(1, buttonName))
        elif sectionName in ("Uplands"):
            self.click(LandCommonEntity().get_right_button(2, buttonName))
        elif sectionName in ("Land Survey"):
            self.click(LandCommonEntity().get_survey_button(buttonName))

    def summary_field_list(self,sectionName):
        """
        #The fields value on Location tab, Characteristics tab,Survey tab
        :param: sectionName
        :return:
        """
        if sectionName in ("Location From County Seat", "Characteristics"):
            summary_field_list = self.find_elements(LandCommonEntity().get_field_list("col-md-5",1,1))
        elif sectionName in ("Disposition Plan"):
            summary_field_list = self.find_elements(LandCommonEntity().get_field_list("col-md-5", 1, 2))
        elif sectionName in ("Location", "Management"):
            summary_field_list = self.find_elements(LandCommonEntity().get_field_list("col-md-7", 1, 1))
        elif sectionName in ("Uplands"):
            summary_field_list = self.find_elements(LandCommonEntity().get_field_list("col-md-7", 2, 2))
        elif sectionName in ("Land Survey"):
            summary_field_list = self.find_elements(LandCommonEntity().get_field_list("col-md-12", 1, 1))
        return summary_field_list













