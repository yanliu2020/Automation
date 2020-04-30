# -*- coding: utf-8 -*-

from  utils.base_page import  BasePage
from config.customer.customer_record_entity import CustomerRecordEntity
from selenium.common.exceptions import  NoSuchElementException
class CustomerRecordPage(BasePage):

    #选择顶部快捷操作按钮
    def top_quick_operator(self,firstMenu,SubMenu):
        """
        #click Actions or History
        :param  action : Actions,History
        :param  select_option : New, Edit, Delete
        :return:
        """
        #点击操作按钮
        self.click(CustomerRecordEntity().get_top_button(firstMenu))
        #点击Actions 选择二级按钮
        if SubMenu != "":
            self.click(CustomerRecordEntity().get_action_submenu(SubMenu))

    def switch_tab(self,tabName):
        """
        :param  tabName : Summary，Entity，Contacts，Related Lease/Lands
        :return:
        """
        self.find_element_by_wait("xpath",CustomerRecordEntity().get_record_tab(tabName))
        self.click(CustomerRecordEntity().get_record_tab(tabName))

    #Entity和Contact页签点击每个section的Detail，Edit，History,New,Delete按钮
    def entity_contacts_operator(self,sectionName,buttonName):
        """
        #click Detail，Edit，History,New,Delete
        :param  sectionName : Customer Summary,Addresses,Websites,Doing Business As (DBA),Business Identifiers
        :param  buttonName : Detail，Edit，History,New,Delete
        :return:
        """
        section_list = self.find_elements(CustomerRecordEntity.section_list)
        print(section_list)
        section_item = None
        for i, item in enumerate(section_list):
            if sectionName == item.text:
                section_item = (i+1,item)
                break
        if section_item is None:
            raise NoSuchElementException(msg="sectionName %s not found!" % sectionName)
        else:
            self.click(CustomerRecordEntity().get_section_operator(section_item[0],buttonName))

    # Related Leases/Lands页签点击每个section的[Link Details], [Delete Relationship]按钮
    def related_leases_operator(self,sectionName,buttonName):
        """
        #click  Link Details，Delete Relationship
        :param  sectionName : Lands，Mineral Leases，Surface Leases，Surface Projects
        :param  buttonName : Link Details，Delete Relationship
        :return:
        """
        section_list = self.find_elements(CustomerRecordEntity.related_section_list)
        print(section_list)
        section_item = None
        for i, item in enumerate(section_list):
            if sectionName == item.text:
                section_item = (i + 1, item)
                break
        if section_item is None:
            raise NoSuchElementException(msg="sectionName %s not found!" % sectionName)
        else:
            self.click(CustomerRecordEntity().get_related_operator(section_item[0], buttonName))

