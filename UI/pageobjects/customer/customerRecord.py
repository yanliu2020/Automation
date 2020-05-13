# -*- coding: utf-8 -*-

from  utils.base_page import  BasePage
from config.customer.customer_record_entity import CustomerRecordEntity
from selenium.common.exceptions import  NoSuchElementException
from utils.logger import Logger
class CustomerRecordPage(BasePage):

    def customer_operator(self,action,select_option):
        """
        #Customer增删改查
        :param  action : Actions,History
        :param  select_option : New, Edit, Delete
        :return:
        """
        #点击操作按钮
        self.click(CustomerRecordEntity().get_top_button(action))
        #点击Actions 选择二级按钮
        if select_option != "":
            self.click(CustomerRecordEntity().get_action_submenu(select_option))

    def switch_tab(self,tabName):
        """
        #Customer Record 切换tab页
        :param  tabName : Summary，Entity，Contacts，Related Lease/Lands
        :return:
        """
        self.find_element_by_wait("xpath",CustomerRecordEntity().get_record_tab(tabName))
        self.click(CustomerRecordEntity().get_record_tab(tabName))


    def entity_operator(self,sectionName,buttonName,row):
        """
        #Entity页签增删改查
        :param sectionName :
             Entity页签:Customer Summary,Addresses,Websites,Doing Business As (DBA),Business Identifiers
             Contacts页签:Contacts,Email,Phone
        :param row:选择记录行
        :param buttonName:Detail，Edit，New,Delete,History
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
            self.scroll_into_view(CustomerRecordEntity().get_section_name(sectionName))
            if sectionName == "Customer Summary" or buttonName == "New" or buttonName == "History":
                self.click(CustomerRecordEntity().get_section_operator(section_item[0], buttonName))
            else:
                if self.find_elements(CustomerRecordEntity().get_entity_records(section_item[0])):
                    if self.not_selected(section_item[0], row) == True:
                        self.click(CustomerRecordEntity().get_entity_record(section_item[0], row))
                    self.click(CustomerRecordEntity().get_section_operator(section_item[0],buttonName))
                else:
                    Logger.info("sectionName %s have no record!"% sectionName)


    def contact_operator(self,sectionName,buttonName,row):
        """
        #Contacts页签下增删改查
        :param sectionName:
             Contacts页签:Contacts,Email,Phone
        :param row:选择记录行
        :param buttonName:Detail，Edit，New,Delete,History
        :return:
        """
        if self.find_elements(CustomerRecordEntity().get_entity_records(1)):
            #判断是否选中contact记录,确定选中
            if self.not_selected(1, 1) == True:
                self.click(CustomerRecordEntity().get_entity_record(1, 1))
        section_list = self.find_elements(CustomerRecordEntity.section_list)
        print(section_list)
        section_item = None
        #根据传入的section名获取section_item
        for i, item in enumerate(section_list):
            if sectionName == item.text:
                section_item = (i+1,item)
                break
        if section_item is None:
            raise NoSuchElementException(msg="sectionName %s not found!" % sectionName)
        else:
            self.scroll_into_view(CustomerRecordEntity().get_section_name(sectionName))
            if  buttonName == "New" or buttonName == "History":
                self.click(CustomerRecordEntity().get_section_operator(section_item[0], buttonName))
            elif sectionName == "Contacts":
                if self.find_elements(CustomerRecordEntity().get_entity_records(section_item[0])):
                    if self.not_selected(section_item[0],row) == True:
                        self.click(CustomerRecordEntity().get_entity_record(section_item[0], row))
                    self.click(CustomerRecordEntity().get_section_operator(section_item[0], buttonName))
                else:
                    Logger.info("sectionName %s have no record!" % sectionName)
            elif self.find_elements(CustomerRecordEntity().get_entity_records(1)):
                if self.not_selected(1, 1) == True:
                    self.click(CustomerRecordEntity().get_entity_record(1, 1))
                if self.find_elements(CustomerRecordEntity().get_entity_records(section_item[0])):
                    if self.not_selected(section_item[0],row) == True:
                        self.click(CustomerRecordEntity().get_entity_record(section_item[0], row))
                    self.click(CustomerRecordEntity().get_section_operator(section_item[0], buttonName))
                else:
                    Logger.info("sectionName %s have no record!" % sectionName)
            else:
                Logger.info("sectionName %s have no record!" % sectionName)
            # elif self.find_elements(CustomerRecordEntity().get_entity_records(section_item[0])):
            #     if self.not_selected(section_item[0], row) == True:
            #         self.click(CustomerRecordEntity().get_entity_record(section_item[0], row))
            #     self.click(CustomerRecordEntity().get_section_operator(section_item[0], buttonName))
            # else:
            #     Logger.info("sectionName %s have no record!" % sectionName)


    def related_leases_operator(self,sectionName,buttonName,row):
        """
        #Related Lease/Lands 查询和删除
        :param  sectionName:Lands，Mineral Leases,Surface Leases，Surface Projects
        :param  buttonName:Link Details,Delete Relationship
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
            self.scroll_into_view(CustomerRecordEntity().get_section_name(sectionName))
            if buttonName == "Delete Relationship":
                self.click(CustomerRecordEntity().get_related_operator(section_item[0],buttonName))
            else:
                if self.find_elements(CustomerRecordEntity().get_related_records(section_item[0])):
                    self.click(CustomerRecordEntity().get_related_record(section_item[0], row))
                    self.click(CustomerRecordEntity().get_related_operator(section_item[0],buttonName))
                else:
                    Logger.info("sectionName %s have no record!"% sectionName)

    def get_tips_msg(self):
        """
        # 获取页面提示消息
        :return:
        """
        #self.find_element_by_wait("xpath",CustomerRecordEntity.tips_msg)
        msg = self.find_element(CustomerRecordEntity.tips_msg).text.lower()
        print(msg)
        return msg

    def input_DBA_Website(self, name, txt):
        """
        #输入DBA,Websites
        :param: name : alias, url
        :return:
        """
        self.ctrl_all(CustomerRecordEntity().get_input_info(name))
        self.type(CustomerRecordEntity().get_input_info(name), txt)
        self.click(CustomerRecordEntity.save)
        msg = self.get_tips_msg()
        if 'successfully' in msg:
            return True
        else:
            return False

    def detail_history(self,title):
        """
        #详情页,历史页
        :param : title
        :return:
        """
        title = self.find_element(CustomerRecordEntity.window_title).text
        if title in title:
            self.click(CustomerRecordEntity.close_window)
            return True
        else:
            return False

    def delete(self):
        """
        # 执行删除操作
        :return:
        """
        self.click(CustomerRecordEntity.delete_confirm)
        msg = self.get_tips_msg()
        if 'successfully' in msg:
            return True
        else:
            return False

    def not_selected(self,section,row):
        """
        # 未选中状态
        :param : section
        :param : row
        :return:
        """
        selected = self.find_element(
            CustomerRecordEntity().get_entity_record(section, row)).get_attribute('style')
        print("+++++" + selected)
        if "background" in  selected:
            pass
        else:
            return True

    def operator_email(self,index,email,type,isPrimary):
        """
        # 新增/修改 contact email
        :param : email
        :param : type
        :param : isPrimary
        :return:
        """
        if index == "New":
            self.ctrl_all(CustomerRecordEntity.emailAddress)
            self.type(CustomerRecordEntity.emailAddress, email)
            self.drop_select(CustomerRecordEntity.emailType, type)
            self.drop_select(CustomerRecordEntity.isPrimary, isPrimary)
            self.click(CustomerRecordEntity.save)
        elif index == "Edit":
            self.ctrl_all(CustomerRecordEntity.editEmailAddress)
            self.type(CustomerRecordEntity.editEmailAddress, email)
            self.drop_select(CustomerRecordEntity.editEmailType, type)
            self.drop_select(CustomerRecordEntity.editEmailPrimary, isPrimary)
            self.click(CustomerRecordEntity.save)
        msg = self.get_tips_msg()
        if 'successfully' in msg:
            return True
        else:
            return False

    def operator_phone(self,index,countryCode,type,areaCode,phone,exetension):
        """
        # 新增/修改 contact phone
        :param : index
        :param : countryCode
        :param : type
        :param : areaCode
        :param : phone
        :param : exetension
        :return:
        """
        if index == 'New':
            self.type(CustomerRecordEntity.countryCode,countryCode)
            self.drop_select(CustomerRecordEntity.phoneType, type)
            self.type(CustomerRecordEntity.phoneNumber,phone)
            self.type(CustomerRecordEntity.phoneExtension, exetension)
        elif index == "Edit":
            self.ctrl_all(CustomerRecordEntity.countryCode)
            self.type(CustomerRecordEntity.countryCode, countryCode)
            self.drop_select(CustomerRecordEntity.phoneType, type)
            self.ctrl_all(CustomerRecordEntity.areaCode)
            self.type(CustomerRecordEntity.areaCode, areaCode)
            self.ctrl_all(CustomerRecordEntity.phoneNumber)
            self.type(CustomerRecordEntity.phoneNumber, phone)
            self.ctrl_all(CustomerRecordEntity.phoneExtension)
            self.type(CustomerRecordEntity.phoneExtension, exetension)
        msg = self.get_tips_msg()
        if 'successfully' in msg:
            return True
        else:
            return False

    def operator_identifier(self,type,identifierNo):
        """
        # 新增/修改 identifier
        :param : type
        :param : identifierNo
        :return:
        """
        self.drop_select(CustomerRecordEntity.identifierName,type)
        self.ctrl_all(CustomerRecordEntity.identifier)
        self.type(CustomerRecordEntity.identifier,identifierNo)
        self.click(CustomerRecordEntity.save)
        msg = self.get_tips_msg()
        if 'successfully' in msg:
            return True
        else:
            return False





