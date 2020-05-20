# -*- coding: utf-8 -*-

from  utils.base_page import  BasePage
from config.customer.customer_record_entity import CustomerRecordEntity
from selenium.common.exceptions import  NoSuchElementException
from utils.logger import logger
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
        # print(section_list)
        section_item = None
        for i, item in enumerate(section_list):
            if sectionName == item.text:
                section_item = (i+1,item)
                break
        if section_item is None:
            logger.info(msg="sectionName %s not found!" % sectionName)
        else:
            self.scroll_into_view(CustomerRecordEntity().get_section_name(sectionName))
            if sectionName == "Customer Summary" or buttonName == "New":
                self.click(CustomerRecordEntity().get_section_operator(section_item[0], buttonName))
            else:
                if self.find_elements(CustomerRecordEntity().get_entity_records(section_item[0])):
                    if self.not_selected(section_item[0], row) == True:
                        self.click(CustomerRecordEntity().get_entity_record(section_item[0], row))
                    self.click(CustomerRecordEntity().get_section_operator(section_item[0],buttonName))
                else:
                    logger.info("sectionName %s have no record!"% sectionName)

    def contact_operator(self,sectionName,buttonName,row):
        """
        #Contacts页签下增删改查
        :param sectionName:
             Contacts页签:Contacts,Email,Phone
        :param row:选择记录行
        :param buttonName:Detail，Edit，New,Delete,History
        :return:
        """
        # if self.contact_list_page() == True:
        #     if self.find_elements(CustomerRecordEntity().get_entity_records(1)):
        #         # 判断是否选中contact记录,确定选中
        #         if self.not_selected(1, 1) == True:
        #             self.click(CustomerRecordEntity().get_entity_record(1, 1))
        section_list = self.find_elements(CustomerRecordEntity.section_list)
        # print(section_list)
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
            if sectionName == "Contacts":
                if buttonName != "New" and self.contact_list_page() == True:
                    if self.not_selected(section_item[0],row) == True:
                        self.click(CustomerRecordEntity().get_entity_record(section_item[0], row))
                self.click(CustomerRecordEntity().get_section_operator(section_item[0], buttonName))
            elif self.contact_list_page() == True:
                if self.not_selected(1, 1) == True:
                    self.click(CustomerRecordEntity().get_entity_record(1, 1))
                if buttonName != "New" and self.find_elements(CustomerRecordEntity().get_entity_records(section_item[0])):
                    if self.not_selected(section_item[0],row) == True:
                        self.click(CustomerRecordEntity().get_entity_record(section_item[0], row))
                self.click(CustomerRecordEntity().get_section_operator(section_item[0], buttonName))

            # if  buttonName == "New":
            #     self.click(CustomerRecordEntity().get_section_operator(section_item[0], buttonName))
            # elif sectionName == "Contacts":
            #     if self.find_elements(CustomerRecordEntity().get_entity_records(section_item[0])):
            #         if self.not_selected(section_item[0],row) == True:
            #             self.click(CustomerRecordEntity().get_entity_record(section_item[0], row))
            #         self.click(CustomerRecordEntity().get_section_operator(section_item[0], buttonName))
            #     else:
            #         logger.info("sectionName %s have no record!" % sectionName)
            # elif self.find_elements(CustomerRecordEntity().get_entity_records(1)):
            #     if self.not_selected(1, 1) == True:
            #         self.click(CustomerRecordEntity().get_entity_record(1, 1))
            #     if self.find_elements(CustomerRecordEntity().get_entity_records(section_item[0])):
            #         if self.not_selected(section_item[0],row) == True:
            #             self.click(CustomerRecordEntity().get_entity_record(section_item[0], row))
            #         self.click(CustomerRecordEntity().get_section_operator(section_item[0], buttonName))
            #     else:
            #         logger.info("sectionName %s have no record!" % sectionName)
            # else:
            #     logger.info("sectionName %s have no record!" % sectionName)

            # elif self.find_elements(CustomerRecordEntity().get_entity_records(section_item[0])):
            #     if self.not_selected(section_item[0], row) == True:
            #         self.click(CustomerRecordEntity().get_entity_record(section_item[0], row))
            #     self.click(CustomerRecordEntity().get_section_operator(section_item[0], buttonName))
            # else:
            #     logger.info("sectionName %s have no record!" % sectionName)


    def related_leases_operator(self,sectionName,buttonName,row):
        """
        #Related Lease/Lands 查询和删除
        :param  sectionName:Lands，Mineral Leases,Surface Leases，Surface Projects
        :param  buttonName:Link Details,Delete Relationship
        :return:
        """
        section_list = self.find_elements(CustomerRecordEntity.related_section_list)
        # print(section_list)
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
                    logger.info("sectionName %s have no record!"% sectionName)

    def contact_list_page(self):
        record = self.find_element(CustomerRecordEntity.contact_list_page).text
        if "0" in record:
            return False
            logger.info("have no contact record")
        else:
            return True

    def not_selected(self,section,row):
        """
        # 未选中状态
        :param : section
        :param : row
        :return:
        """
        selected = self.find_element(
            CustomerRecordEntity().get_entity_record(section, row)).get_attribute('style')
        # print("+++++" + selected)
        if "background" in  selected:
            pass
        else:
            return True

    def get_tips_msg(self):
        """
        # 获取页面提示消息
        :return:
        """
        #self.find_element_by_wait("xpath",CustomerRecordEntity.tips_msg)
        self.sleep(1)
        return  self.find_element(CustomerRecordEntity.tips_msg).text
        #print(msg)
        #return msg

    def detail_history(self,title):
        """
        #详情页,历史页
        :param : title
        :return:
        """
        title = self.find_element(CustomerRecordEntity.window_title).text
        if title in title:
            self.execute_script_click(CustomerRecordEntity.close_window)
            return True
        else:
            return False

    def delete(self):
        """
        # 执行删除操作
        :return:
        """
        self.click(CustomerRecordEntity.delete_confirm)
        # msg = self.get_tips_msg()
        if "successfully" in self.get_tips_msg():
            return True
        else:
            return False

    def operator_address(self,addressType,address1,city,stateCode):
        """
        # 新增/修改 address
        :param : type,identifierNo
        :return:
        """
        self.drop_select(CustomerRecordEntity.addressType,addressType)
        self.ctrl_all(CustomerRecordEntity.address1)
        self.type(CustomerRecordEntity.address1,address1)
        self.ctrl_all(CustomerRecordEntity.city)
        self.type(CustomerRecordEntity.city,city)
        self.drop_select(CustomerRecordEntity.stateCode, stateCode)
        self.click(CustomerRecordEntity.save)
        # msg = self.get_tips_msg()
        if "successfully" in self.get_tips_msg():
            return True
        else:
            return False

    def input_DBA_Website(self, name, txt):
        """
        #输入DBA,Websites
        :param: name : alias, url
        :return:
        """
        self.ctrl_all(CustomerRecordEntity().get_input_info(name))
        self.type(CustomerRecordEntity().get_input_info(name), txt)
        self.click(CustomerRecordEntity.save)
        # msg = self.get_tips_msg()
        if "successfully" in self.get_tips_msg():
            return True
        else:
            return False

    def operator_identifier(self,type,identifierNo):
        """
        # 新增/修改 identifier
        :param : type,identifierNo
        :return:
        """
        self.drop_select(CustomerRecordEntity.identifierName,type)
        self.ctrl_all(CustomerRecordEntity.identifier)
        self.type(CustomerRecordEntity.identifier,identifierNo)
        self.click(CustomerRecordEntity.save)
        # msg = self.get_tips_msg()
        if "successfully" in self.get_tips_msg():
            return True
        else:
            return False



    def operator_contact(self,salutation,firstName,middleName,lastName,suffix,contactRole):
        """
        # 新增/修改 contact
        :param : salutation,firstName,middleName,lastName,suffix,contactRole
        :return:
        """
        self.drop_select(CustomerRecordEntity.salutation,salutation)
        self.ctrl_all(CustomerRecordEntity.firstName)
        self.type(CustomerRecordEntity.firstName,firstName)
        self.ctrl_all(CustomerRecordEntity.middleName)
        self.type(CustomerRecordEntity.middleName,middleName)
        self.ctrl_all(CustomerRecordEntity.lastName)
        self.type(CustomerRecordEntity.lastName,lastName)
        self.drop_select(CustomerRecordEntity.suffix, suffix)
        self.drop_select(CustomerRecordEntity.contactRole, contactRole)
        self.click(CustomerRecordEntity.save)
        # msg = self.get_tips_msg()
        if "successfully" in self.get_tips_msg():
            return True
        else:
            return False

    def operator_email(self,email,type,isPrimary):
        """
        # 新增/修改 contact email
        :param : email,type,isPrimary
        :return:
        """
        self.ctrl_all(CustomerRecordEntity.emailAddress)
        self.type(CustomerRecordEntity.emailAddress, email)
        self.drop_select(CustomerRecordEntity.emailType, type)
        self.drop_select(CustomerRecordEntity.isPrimary, isPrimary)
        self.click(CustomerRecordEntity.save)
        # msg = self.get_tips_msg()
        if 'successfully' in self.get_tips_msg():
            return True
        else:
            return False

    def operator_phone(self,type,areaCode,phone,exetension):
        """
        # 新增/修改 contact phone
        :param : countryCode,type,areaCode,phone,exetension
        :return:
        """
        # self.ctrl_all(CustomerRecordEntity.countryCode)
        # self.type(CustomerRecordEntity.countryCode, countryCode)
        self.drop_select(CustomerRecordEntity.phoneType, type)
        self.ctrl_all(CustomerRecordEntity.areaCode)
        self.type(CustomerRecordEntity.areaCode, areaCode)
        self.ctrl_all(CustomerRecordEntity.phoneNumber)
        self.type(CustomerRecordEntity.phoneNumber, phone)
        self.ctrl_all(CustomerRecordEntity.phoneExtension)
        self.type(CustomerRecordEntity.phoneExtension, exetension)
        self.click(CustomerRecordEntity.save)
        # msg = self.get_tips_msg()
        if 'successfully' in self.get_tips_msg():
            return True
        else:
            return False






