# -*- coding: utf-8 -*-
import datetime
from  utils.base_page import  BasePage
from config.usm.usm_entity import  UsmEntity
from pageobjects.customer.customerRecord import CustomerRecordPage
from selenium.webdriver.support.ui import Select
from utils.logger import logger
nowTime = datetime.datetime.now().strftime("%Y/%m/%d %H:%M:%S")

class UsmPage(BasePage):
    def is_usm_page(self):
        if self.find_element(UsmEntity.default_text):
            return True

    def switch_tab(self,tabName):
        """
        #Switch Tab
        :param  tabName : Roles，Users
        :return:
        """
        if self.is_usm_page() == True:
            self.find_element_by_wait("xpath", UsmEntity().get_record_tab(tabName))
            self.click(UsmEntity().get_record_tab(tabName))

    def click_button(self,buttonName,row):
        """
        #Click button
        :param tabName,buttonName,row
        :return:
        """
        if self.is_usm_page() == True:
            self.sleep(2)
            if buttonName in ("Edit","Inactivate"):
                self.ctrl_all(UsmEntity.list_filter)
                self.type(UsmEntity.list_filter, "automation")
                # self.type(UsmEntity.list_filter, self.find_element(UsmEntity().get_select_column(row,column)).text)
                self.sleep(2)
                if "background" not in self.find_element(
                        UsmEntity().get_select_record(row)).get_attribute('style'):
                    self.click(UsmEntity().get_select_record(row))
            self.click(UsmEntity().get_operator(buttonName))

    def operation(self,flag,index,section,buttonName,capabilityNamelist=[]):
        """
        :param flag,index,section,buttonName,capabilityNamelist=[]
        :return:
        """
        if self.is_usm_page() == True:
            if buttonName == "New" or (section == "Roles" and buttonName == "Edit"):
                self.ctrl_all(UsmEntity().get_input_textbox("name"))
                self.type(UsmEntity().get_input_textbox("name"), "UI automation" + nowTime)
                self.ctrl_all(UsmEntity().get_input_textbox("description"))
                self.type(UsmEntity().get_input_textbox("description"), BasePage(self.driver).randomData("string", 6))
                self.sleep(2)
                permission_list = ["Read", "Update", "Create", "Delete", "MassUpdate"]
                # capability_list = self.find_elements(UsmEntity.capabilitity_list)
                capability_item = None
                capability_index = []
                for i in capabilityNamelist:
                    self.ctrl_all(UsmEntity.filter)
                    self.type(UsmEntity.filter, i)
                    capability_list = self.find_elements(UsmEntity.capabilitity_list)
                    for j, item in enumerate(capability_list):
                        if i == item.text:
                            capability_item = j
                            capability_index.append(capability_item)
                            for b in permission_list:
                                self.click(UsmEntity().get_capability(b, capability_index[0]))
                    if capability_item is None:
                        logger.info(msg="capabilityName %s not found!" % i)
                # for a in capability_index:
                #     for b in permission_list:
                #         self.click(UsmEntity().get_capability(b, a))
            elif section == "Users":
                self.ctrl_all(UsmEntity().get_input_textbox("userName"))
                self.type(UsmEntity().get_input_textbox("userName"), BasePage(self.driver).randomData("string", 6))
                self.ctrl_all(UsmEntity().get_input_textbox("firstName"))
                self.type(UsmEntity().get_input_textbox("firstName"), BasePage(self.driver).randomData("string", 6))
                self.ctrl_all(UsmEntity().get_input_textbox("lastName"))
                self.type(UsmEntity().get_input_textbox("lastName"), BasePage(self.driver).randomData("string", 6))
            elif buttonName == "Inactivate":
                self.click(UsmEntity.confirm_delete)
            if buttonName == "New" or buttonName == "Edit":
                if index == 1:
                    if section == "Roles":
                        self.click(UsmEntity().get_button("Next"))
                        list = "Users"
                    else:
                        list = "Roles"
                    if flag == "add":
                        self.type(UsmEntity.filter,
                                  self.find_element(
                                      UsmEntity().get_list_value("available" + list + "Selected", "1")).text)
                        Select(
                            self.find_element(
                                UsmEntity().get_two_list("available" + list + "Selected"))).select_by_index(0)
                        self.sleep(1)
                        self.click(UsmEntity().get_button("Add"))
                    elif flag == "remove":
                        Select(self.find_element(
                            UsmEntity().get_two_list("assigned" + list + "Selected"))).select_by_index(
                            0)
                        self.sleep(1)
                        self.click(UsmEntity().get_button("Remove"))
                else:
                    if section == "Roles":
                        self.click(UsmEntity().get_switch_tab("Users"))
                        list = "Users"
                    else:
                        list = "Roles"
                    if flag == "add":
                        self.ctrl_multiSelect(UsmEntity().get_list_value("available" + list + "Selected", "1"),
                                              UsmEntity().get_list_value("available" + list + "Selected", "2"))
                        self.sleep(1)
                        self.click(UsmEntity().get_button("Add"))
                    elif flag == "remove":
                        self.ctrl_multiSelect(UsmEntity().get_list_value("assigned" + list + "Selected", "1"),
                                              UsmEntity().get_list_value("assigned" + list + "Selected", "2"))
                        self.sleep(1)
                        self.click(UsmEntity().get_button("Remove"))
                self.click(UsmEntity().get_button("Finish"))
            self.sleep(2)
            if "successfully" in CustomerRecordPage(self.driver).get_tips_msg():
                return True
            else:
                return False










