# -*- coding: utf-8 -*-
from  utils.base_page import  BasePage
from config.usm.usm_entity import  UsmEntity

class UsmPage(BasePage):
    def switch_tab(self,tabName):
        """
        #切换tab页
        :param  tabName : Roles，Users
        :return:
        """
        self.find_element_by_wait("xpath",UsmEntity().get_record_tab(tabName))
        self.click(UsmEntity().get_record_tab(tabName))

    def operator(self,tabName,buttonName,row):
        """
        #增删改查
        :param tabName,buttonName,row
        :return:
        """
        if (tabName == "Roles" and buttonName != "New") or tabName == "Users":
            if "background" not in self.find_element(
            UsmEntity().get_select_record(row)).get_attribute('style'):
                self.click(UsmEntity().get_select_record(row))
        self.click(UsmEntity().get_operator(buttonName))


