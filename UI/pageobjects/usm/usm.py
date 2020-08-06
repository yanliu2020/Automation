# -*- coding: utf-8 -*-
from  utils.base_page import  BasePage
from config.usm.usm_entity import  UsmEntity
from pageobjects.customer.customerRecord import CustomerRecordPage
from selenium.webdriver.support.ui import Select
from utils.logger import logger

class UsmPage(BasePage):
    def switch_tab(self,tabName):
        """
        #Switch Tab
        :param  tabName : Roles，Users
        :return:
        """
        self.find_element_by_wait("xpath",UsmEntity().get_record_tab(tabName))
        self.click(UsmEntity().get_record_tab(tabName))

    def click_button(self,tabName,buttonName,row):
        """
        #Click button
        :param tabName,buttonName,row
        :return:
        """
        self.sleep(1)
        if (tabName == "Roles" and buttonName != "New") or tabName == "Users":
            if "background" not in self.find_element(
            UsmEntity().get_select_record(row)).get_attribute('style'):
                self.click(UsmEntity().get_select_record(row))
        self.click(UsmEntity().get_operator(buttonName))

    def operation(self,section,buttonName,capabilityNamelist=[]):
        """
        :param section,buttonName,capabilityNamelist=[]
        :return:
        """
        if buttonName == "New" or ( section == "Roles" and buttonName == "Edit"):
            self.ctrl_all(UsmEntity().get_input_textbox("name"))
            self.type(UsmEntity().get_input_textbox("name"), BasePage(self.driver).randomData("string", 6))
            self.ctrl_all(UsmEntity().get_input_textbox("description"))
            self.type(UsmEntity().get_input_textbox("description"), BasePage(self.driver).randomData("string", 6))
            permission_list = ["Read","Update","Create","Delete","MassUpdate"]
            capability_list = self.find_elements(UsmEntity.capabilitity_list)
            capability_item = None
            capability_index = []
            for i in capabilityNamelist:
                for j, item in enumerate(capability_list):
                    if i == item.text:
                        capability_item = j
                        capability_index.append(capability_item)
                if capability_item is None:
                    logger.info(msg="capabilityName %s not found!" % i)
            for a in capability_index:
                for b in permission_list:
                    self.click(UsmEntity().get_capability(b, a))
            if buttonName == "New":
                self.click(UsmEntity().get_button("Next"))
                self.type(UsmEntity.filter, self.find_element(UsmEntity().get_list_value("availableUsersSelected", "1")).text)
                Select(self.find_element(UsmEntity().get_two_list("availableUsersSelected"))).select_by_index(0)
                self.click(UsmEntity().get_button("Add"))
                self.click(UsmEntity().get_button("Finish"))
            elif buttonName == "Edit":
                self.click(UsmEntity().get_switch_tab("Users"))
                Select(self.find_element(UsmEntity().get_two_list("assignedUsersSelected"))).select_by_index(0)
                self.click(UsmEntity().get_button("Remove"))
                self.click(UsmEntity().get_button("Finish"))
        elif  buttonName == "Inactivate":
                self.click(UsmEntity.confirm_delete)
        elif section == "Users":
            self.ctrl_all(UsmEntity().get_input_textbox("userName"))
            self.type(UsmEntity().get_input_textbox("userName"),BasePage(self.driver).randomData("string", 6))
            self.ctrl_all(UsmEntity().get_input_textbox("firstName"))
            self.type(UsmEntity().get_input_textbox("firstName"), BasePage(self.driver).randomData("string", 6))
            self.ctrl_all(UsmEntity().get_input_textbox("lastName"))
            self.type(UsmEntity().get_input_textbox("lastName"), BasePage(self.driver).randomData("string", 6))
            self.type(UsmEntity.filter,
                      self.find_element(UsmEntity().get_list_value("availableRolesSelected", "1")).text)
            Select(self.find_element(UsmEntity().get_two_list("availableRolesSelected"))).select_by_index(0)
            self.click(UsmEntity().get_button("Add"))
            self.click(UsmEntity().get_button("Finish"))
        self.sleep(2)
        if "successfully" in CustomerRecordPage(self.driver).get_tips_msg():
            return True
        else:
            return False

    def get_capability(self,capabilityNamelist=[]):
        capability_list= self.find_elements(UsmEntity.capabilitity_list)
        capability_index = None
        for i in capabilityNamelist:
            for j, item in enumerate(capability_list):
                if i == item.text:
                    capability_index = (j, item)
                    break
            if capability_index is None:
                logger.info(msg="capabilityName %s not found!" % i)
















