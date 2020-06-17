# -*- coding: utf-8 -*-

from  utils.base_page import  BasePage
from config.customer.customer_record_entity import CustomerRecordEntity
from selenium.common.exceptions import  NoSuchElementException
from utils.logger import logger
class CustomerRecordPage(BasePage):

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
        :param sectionName,buttonName,row
        :return:
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
        :param sectionName,buttonName,row
        :return:
        """
        section_list = self.find_elements(CustomerRecordEntity.section_list)
        # print(section_list)
        section_item = None
        #根据传入的section名获取section_item
        for i, item in enumerate(section_list):
            if sectionName == item.text:
                section_item = (i+1,item)
                break
        if section_item is None:
            logger.info("sectionName %s not found!" % sectionName)
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

    # def related_leases_operator(self,sectionName,buttonName,row):
    #     """
    #     #Related Lease/Lands 查询和删除
    #     :param  sectionName,buttonName,row
    #     :return:
    #     """
    #     section_list = self.find_elements(CustomerRecordEntity.related_section_list)
    #     # print(section_list)
    #     section_item = None
    #     for i, item in enumerate(section_list):
    #         if sectionName == item.text:
    #             section_item = (i + 1, item)
    #             break
    #     if section_item is None:
    #         raise NoSuchElementException(msg="sectionName %s not found!" % sectionName)
    #     else:
    #         self.scroll_into_view(CustomerRecordEntity().get_section_name(sectionName))
    #         if buttonName == "Delete Relationship":
    #             self.click(CustomerRecordEntity().get_related_operator(section_item[0],buttonName))
    #         else:
    #             if self.find_elements(CustomerRecordEntity().get_related_records(section_item[0])):
    #                 self.click(CustomerRecordEntity().get_related_record(section_item[0], row))
    #                 self.click(CustomerRecordEntity().get_related_operator(section_item[0],buttonName))
    #             else:
    #                 logger.info("sectionName %s have no record!"% sectionName)

    def contact_list_page(self):
        """
         # contact list是否有记录
         :return:
        """
        record = self.find_element(CustomerRecordEntity.contact_list_page).text
        if "total records: 0" in record:
            logger.info("have no contact record")
            return False
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
        if "background" in  selected:
            pass
        else:
            return True

    def get_tips_msg(self):
        """
        # 获取页面提示消息
        :return:
        """
        self.sleep(2)
        return  self.find_element(CustomerRecordEntity.tips_msg).text

    def detail_history(self,title):
        """
        #详情页,历史页
        :param : title
        :return:
        """
        title = self.find_element(CustomerRecordEntity.contact_title).text
        if title in title:
            self.execute_script_click(CustomerRecordEntity.contact_close)
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
        self.drop_select(CustomerRecordEntity().get_address_select("addressType"),addressType)
        self.ctrl_all(CustomerRecordEntity().get_address_input("address1"))
        self.type(CustomerRecordEntity().get_address_input("address1"),address1)
        self.ctrl_all(CustomerRecordEntity().get_address_input("city"))
        self.type(CustomerRecordEntity().get_address_input("city"),city)
        self.drop_select(CustomerRecordEntity().get_address_select("stateCode"), stateCode)
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
        self.drop_select(CustomerRecordEntity().get_contact_select("salutation"),salutation)
        self.ctrl_all(CustomerRecordEntity().get_contact_input("firstName"))
        self.type(CustomerRecordEntity().get_contact_input("firstName"),firstName)
        self.ctrl_all(CustomerRecordEntity().get_contact_input("middleName"))
        self.type(CustomerRecordEntity().get_contact_input("middleName"),middleName)
        self.ctrl_all(CustomerRecordEntity().get_contact_input("lastName"))
        self.type(CustomerRecordEntity().get_contact_input("lastName"),lastName)
        self.drop_select(CustomerRecordEntity().get_contact_select("suffix"), suffix)
        self.drop_select(CustomerRecordEntity().get_contact_select("contactRole"), contactRole)
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
        self.ctrl_all(CustomerRecordEntity().get_email_input("emailAddress"))
        self.type(CustomerRecordEntity().get_email_input("emailAddress"), email)
        self.drop_select(CustomerRecordEntity().get_email_select("emailType"), type)
        self.drop_select(CustomerRecordEntity().get_email_select("isPrimary"), isPrimary)
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
        # self.ctrl_all(CustomerRecordEntity().phone_input("countryCode"))
        # self.type(CustomerRecordEntity().phone_input("countryCode"), countryCode)
        self.drop_select(CustomerRecordEntity().get_phone_select("phoneType"), type)
        self.ctrl_all(CustomerRecordEntity().get_phone_input("areaCode"))
        self.type(CustomerRecordEntity().get_phone_input("areaCode"), areaCode)
        self.ctrl_all(CustomerRecordEntity().get_phone_input("phone"))
        self.type(CustomerRecordEntity().get_phone_input("phone"), phone)
        self.ctrl_all(CustomerRecordEntity().get_phone_input("extension"))
        self.type(CustomerRecordEntity().get_phone_input("extension"), exetension)
        self.click(CustomerRecordEntity.save)
        # msg = self.get_tips_msg()
        if 'successfully' in self.get_tips_msg():
            return True
        else:
            return False

    def top_operate(self,buttonName,acitonName):
        """
        # Action区域快捷操作
        :param : buttonName，acitonName
        :return:
        """
        #self.scroll_into_view(CustomerRecordEntity().get_customer_operate(buttonName))
        self.click(CustomerRecordEntity().get_customer_operate(buttonName))
        if buttonName == "History":
            self.sleep(1)
            title = self.find_element(CustomerRecordEntity.contact_title).text
            if buttonName in title:
                self.execute_script_click(CustomerRecordEntity.contact_close)
                return True
            else:
                return False
        elif buttonName == "Delete":
            self.click(CustomerRecordEntity.delete_confirm)
            if 'successfully' in self.get_tips_msg():
                return True
            else:
                return False
        else:
            self.click(CustomerRecordEntity().get_action(acitonName))

    def edit_entity(self,entityType,entityClass,salutation,firstName,lastName,suffix,fullName,default_sort,organizationName,typeOfBusiness,stateOfIncorporation):
        """
        #Edit multiple type customer
        :param  type,className
        :param  salutation,firstName,lastName,suffix,fullName,default_sort,organizationName,typeOfBusiness,stateOfIncorporation
        :return:
        """
        self.drop_select(CustomerRecordEntity().get_entity("typeName"), entityType)
        self.drop_select(CustomerRecordEntity().get_entity("entityClass"), entityClass)
        if entityType == "Person":
            if entityClass == "Household":
                self.ctrl_all(CustomerRecordEntity().get_edit_input("fullName"))
                self.type(CustomerRecordEntity().get_edit_input("fullName"), fullName)
                self.ctrl_all(CustomerRecordEntity().get_edit_input("soundEx"))
                self.type(CustomerRecordEntity().get_edit_input("soundEx"), default_sort)
            else:
                self.drop_select(CustomerRecordEntity().get_edit_select("salutation"), salutation)
                self.ctrl_all(CustomerRecordEntity().get_edit_input("firstName"))
                self.type(CustomerRecordEntity().get_edit_input("firstName"), firstName)
                self.ctrl_all(CustomerRecordEntity().get_edit_input("lastName"))
                self.type(CustomerRecordEntity().get_edit_input("lastName"), lastName)
                self.drop_select(CustomerRecordEntity().get_edit_select("suffix"), suffix)
        else:
            self.ctrl_all(CustomerRecordEntity().get_edit_input("organizationName"))
            self.type(CustomerRecordEntity().get_edit_input("organizationName"), organizationName)
            if entityClass == "Company" or entityClass == "Government":
                self.drop_select(CustomerRecordEntity().get_edit_select("subClassName"), typeOfBusiness)
            self.drop_select(CustomerRecordEntity().get_edit_select("stateOfIncorporation"), stateOfIncorporation)

    def validate_records_rows(self):
        record = self.find_element(CustomerRecordEntity.entity_history).text
        if "total records: 1" in record:
            return True
        else:
            return False














