# -*- coding: utf-8 -*-
from  utils.base_page import  BasePage
from config.customer.customer_record_entity import CustomerRecordEntity
from utils.logger import logger
from utils.connect_sql import dbConnect

class CustomerRecordPage(BasePage):
    def is_customer_record_page(self):
        if self.find_element(CustomerRecordEntity.default_text):
            return True
        else:
            return False

    def switch_tab(self,tabName):
        """
        #Customer Record Switch Tab
        :param  tabName : Summary，Entity，Contacts，Related Lease/Lands
        :return:
        """
        if self.is_customer_record_page() == True:
            self.find_element_by_wait("xpath", CustomerRecordEntity().get_record_tab(tabName))
            self.click(CustomerRecordEntity().get_record_tab(tabName))

    def entity_operator(self,sectionName,buttonName,row):
        """
        #Entity Tab
        :param sectionName,buttonName,row
        :return:
        """
        if self.is_customer_record_page() == True:
            section_list = self.find_elements(CustomerRecordEntity.section_list)
            # print(section_list)
            section_item = None
            for i, item in enumerate(section_list):
                if sectionName == item.text:
                    section_item = (i + 1, item)
                    break
            if section_item is None:
                logger.info(msg="sectionName %s not found!" % sectionName)
            else:
                self.scroll_into_view(CustomerRecordEntity().get_section_name(sectionName))
                if sectionName == "Customer Summary" or buttonName == "New":
                    self.click(CustomerRecordEntity().get_section_operator(section_item[0], buttonName))
                elif buttonName == "List":
                    self.drag_and_drop(CustomerRecordEntity().get_drag_column(section_item[0], "City"),
                                       CustomerRecordEntity().get_drag_column(section_item[0], "Attention To Line"))
                else:
                    if self.find_elements(CustomerRecordEntity().get_entity_records(section_item[0])):
                        if self.not_selected(section_item[0], row) == True:
                            self.click(CustomerRecordEntity().get_entity_record(section_item[0], row))
                        if sectionName == "Business Identifier" and self.find_element(
                                CustomerRecordEntity().get_identifier_name(1)).text == "BAN" and (
                                buttonName == "Edit" or buttonName == "Delete"):
                            pass
                        else:
                            self.click(CustomerRecordEntity().get_section_operator(section_item[0], buttonName))
                    else:
                        logger.info("sectionName %s have no record!" % sectionName)


    def contact_operator(self,sectionName,buttonName,row):
        """
        #Contacts Tab
        :param sectionName,buttonName,row
        :return:
        """
        if self.is_customer_record_page() == True:
            section_list = self.find_elements(CustomerRecordEntity.section_list)
            # print(section_list)
            section_item = None
            for i, item in enumerate(section_list):
                if sectionName == item.text:
                    section_item = (i + 1, item)
                    break
            if section_item is None:
                logger.info("sectionName %s not found!" % sectionName)
            else:
                self.scroll_into_view(CustomerRecordEntity().get_section_name(sectionName))
                if sectionName == "Contacts":
                    if buttonName != "New" and self.contact_list_page() == True:
                        if self.not_selected(section_item[0], row) == True:
                            self.click(CustomerRecordEntity().get_entity_record(section_item[0], row))
                    self.click(CustomerRecordEntity().get_section_operator(section_item[0], buttonName))
                elif self.contact_list_page() == True:
                    if self.not_selected(1, 1) == True:
                        self.click(CustomerRecordEntity().get_entity_record(1, 1))
                    if buttonName != "New" and self.find_elements(
                            CustomerRecordEntity().get_entity_records(section_item[0])):
                        if self.not_selected(section_item[0], row) == True:
                            self.click(CustomerRecordEntity().get_entity_record(section_item[0], row))
                    self.click(CustomerRecordEntity().get_section_operator(section_item[0], buttonName))

    def contact_list_page(self):
        """
         # contact list record
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
        # Not selected record
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
        # get the msg
        :return:
        """
        self.sleep(2)
        return  self.find_element(CustomerRecordEntity.tips_msg).text

    # def detail_history(self,title):
    #     """
    #     #History & Details
    #     :param : title
    #     :return:
    #     """
    #     title = self.find_element(CustomerRecordEntity.contact_title).text
    #     if title in title:
    #         self.execute_script_click(CustomerRecordEntity.contact_close)
    #         return True
    #     else:
    #         return False

    def delete(self):
        """
        # Execute delete
        :return:
        """
        # self.find_element_by_wait("xpath",CustomerRecordEntity.delete_confirm)
        self.sleep(1)
        self.click(CustomerRecordEntity.delete_confirm)
        # msg = self.get_tips_msg()
        if "successfully" in self.get_tips_msg():
            return True
        else:
            return False

    def operator_address(self,addressType,stateCode):
        """
        # Address
        :param : type,identifierNo
        :return:
        """
        self.drop_select(CustomerRecordEntity().get_address_select("addressType"),addressType)
        self.ctrl_all(CustomerRecordEntity().get_address_input("address1"))
        self.type(CustomerRecordEntity().get_address_input("address1"),BasePage(self.driver).randomData("string", 6))
        self.ctrl_all(CustomerRecordEntity().get_address_input("city"))
        self.type(CustomerRecordEntity().get_address_input("city"),BasePage(self.driver).randomData("string", 6))
        self.drop_select(CustomerRecordEntity().get_address_select("stateCode"), stateCode)
        self.click(CustomerRecordEntity.save)
        # msg = self.get_tips_msg()
        if "successfully" in self.get_tips_msg():
            return True
        else:
            return False

    def input_DBA_Website(self, name):
        """
        #DBA,Websites
        :param: name : alias, url
        :return:
        """
        self.ctrl_all(CustomerRecordEntity().get_input_info(name))
        if name == "url":
            self.type(CustomerRecordEntity().get_input_info(name), "http://www."+ BasePage(self.driver).randomData("string", 10)+ ".com")
        elif name == "alias":
            self.type(CustomerRecordEntity().get_input_info(name), BasePage(self.driver).randomData("string", 20))
        self.click(CustomerRecordEntity.save)
        # msg = self.get_tips_msg()
        if "successfully" in self.get_tips_msg():
            return True
        else:
            return False

    def operator_identifier(self,flag,type):
        """
        # Identifier
        :param : flag,type
        :return:
        """
        if flag == "edit":
            if self.find_element(CustomerRecordEntity().get_identifier_name(1)).text == "BAN":
                return True
            elif self.find_element(CustomerRecordEntity().get_identifier_name(1)).text == "State Tax ID":
                self.ctrl_all(CustomerRecordEntity.identifier)
                self.type(CustomerRecordEntity.identifier, BasePage(self.driver).randomData("number", 11))
                self.click(CustomerRecordEntity.save)
                if "successfully" in self.get_tips_msg():
                    return True
                else:
                    return False
            else:
                self.drop_select(CustomerRecordEntity.identifierName, type)
                self.ctrl_all(CustomerRecordEntity.identifier)
                self.identifier_not_BAN_input(type)
                self.click(CustomerRecordEntity.save)
                if "successfully" in self.get_tips_msg():
                    return True
                else:
                    return False
        elif flag == "new":
            if type == "BAN":
                if self.without_BAN() == True:
                    type = dbConnect().getdata('MCDH', 'identifierNameWithoutBan')
                    self.drop_select(CustomerRecordEntity.identifierName,type)
                    self.identifier_not_BAN_input(type)
                else:
                    self.drop_select(CustomerRecordEntity.identifierName, "State Tax ID")
                    self.type(CustomerRecordEntity.identifier, BasePage(self.driver).randomData("number", 11))
                    self.click(CustomerRecordEntity.save)
                    self.find_elements_by_wait("xpath", CustomerRecordEntity().get_section_operator(5, "New"))
                    self.click(CustomerRecordEntity().get_section_operator(5, "New"))
                    self.drop_select(CustomerRecordEntity.identifierName, type)
                    self.drop_select_index(CustomerRecordEntity.select_tax, 1)
            else:
                self.drop_select(CustomerRecordEntity.identifierName, type)
                self.identifier_not_BAN_input(type)
            self.click(CustomerRecordEntity.save)
            if "successfully" in self.get_tips_msg():
                return True
            else:
                return False
        elif flag == "Delete":
            if self.find_element(CustomerRecordEntity().get_identifier_name(1)).text == "BAN":
                return  True
            else:
                self.click(CustomerRecordEntity.delete_confirm)
                if "successfully" in self.get_tips_msg():
                    return True
                else:
                    return False

    def operator_contact(self,salutation,suffix,contactRole):
        """
        # Contact
        :param : salutation,firstName,middleName,lastName,suffix,contactRole
        :return:
        """
        self.drop_select(CustomerRecordEntity().get_contact_select("salutation"),salutation)
        self.ctrl_all(CustomerRecordEntity().get_contact_input("firstName"))
        self.type(CustomerRecordEntity().get_contact_input("firstName"),BasePage(self.driver).randomData("string", 6))
        self.ctrl_all(CustomerRecordEntity().get_contact_input("middleName"))
        self.type(CustomerRecordEntity().get_contact_input("middleName"),BasePage(self.driver).randomData("string", 6))
        self.ctrl_all(CustomerRecordEntity().get_contact_input("lastName"))
        self.type(CustomerRecordEntity().get_contact_input("lastName"),BasePage(self.driver).randomData("string", 6))
        self.drop_select(CustomerRecordEntity().get_contact_select("suffix"), suffix)
        self.drop_select(CustomerRecordEntity().get_contact_select("contactRole"), contactRole)
        self.click(CustomerRecordEntity.save)
        # msg = self.get_tips_msg()
        if "successfully" in self.get_tips_msg():
            return True
        else:
            return False

    def operator_email(self,type,isPrimary):
        """
        # Contact Email
        :param : email,type,isPrimary
        :return:
        """
        self.ctrl_all(CustomerRecordEntity().get_email_input("emailAddress"))
        self.type(CustomerRecordEntity().get_email_input("emailAddress"), BasePage(self.driver).randomData("string", 6)+"@"+
                  BasePage(self.driver).randomData("string", 4)+".com")
        self.drop_select(CustomerRecordEntity().get_email_select("emailType"), type)
        self.drop_select(CustomerRecordEntity().get_email_select("isPrimary"), isPrimary)
        self.click(CustomerRecordEntity.save)
        # msg = self.get_tips_msg()
        if 'successfully' in self.get_tips_msg():
            return True
        else:
            return False

    def operator_phone(self,type):
        """
        # Contact Phone
        :param : countryCode,type,areaCode,phone,exetension
        :return:
        """
        # self.ctrl_all(CustomerRecordEntity().phone_input("countryCode"))
        # self.type(CustomerRecordEntity().phone_input("countryCode"), countryCode)
        self.drop_select(CustomerRecordEntity().get_phone_select("phoneType"), type)
        self.ctrl_all(CustomerRecordEntity().get_phone_input("areaCode"))
        self.type(CustomerRecordEntity().get_phone_input("areaCode"), BasePage(self.driver).randomData("number", 3))
        self.ctrl_all(CustomerRecordEntity().get_phone_input("phone"))
        self.type(CustomerRecordEntity().get_phone_input("phone"), BasePage(self.driver).randomData("number", 7))
        self.ctrl_all(CustomerRecordEntity().get_phone_input("extension"))
        self.type(CustomerRecordEntity().get_phone_input("extension"), BasePage(self.driver).randomData("string", 6))
        self.click(CustomerRecordEntity.save)
        # msg = self.get_tips_msg()
        if 'successfully' in self.get_tips_msg():
            return True
        else:
            return False

    def top_operate(self,buttonName,acitonName):
        """
        # Action Drop List
        :param : buttonName，acitonName
        :return:
        """
        #self.scroll_into_view(CustomerRecordEntity().get_customer_operate(buttonName))
        if self.is_customer_record_page() == True:
            self.click(CustomerRecordEntity().get_customer_operate(buttonName))
            if buttonName == "History":
                self.sleep(1)
                title = self.find_element(CustomerRecordEntity.contact_title).text
                if buttonName in title:
                    self.execute_script_click(CustomerRecordEntity.contact_close)
                    return True
                else:
                    return False
            else:
                self.click(CustomerRecordEntity().get_action(acitonName))



    def edit_entity(self,entityType,entityClass,salutation,suffix,typeOfBusiness,stateOfIncorporation):
        """
        #Edit multiple type customer
        :param  type,className
        :param  salutation,firstName,lastName,suffix,fullName,default_sort,organizationName,typeOfBusiness,stateOfIncorporation
        :return:
        """
        if self.is_customer_record_page() == True:
            self.drop_select(CustomerRecordEntity().get_entity("typeName"), entityType)
            self.drop_select(CustomerRecordEntity().get_entity("entityClass"), entityClass)
            if entityType == "Person":
                if entityClass == "Household":
                    self.ctrl_all(CustomerRecordEntity().get_edit_input("fullName"))
                    self.type(CustomerRecordEntity().get_edit_input("fullName"),
                              BasePage(self.driver).randomData("string", 6))
                    self.ctrl_all(CustomerRecordEntity().get_edit_input("soundEx"))
                    self.type(CustomerRecordEntity().get_edit_input("soundEx"),
                              BasePage(self.driver).randomData("string", 6))
                else:
                    self.drop_select(CustomerRecordEntity().get_edit_select("salutation"), salutation)
                    self.ctrl_all(CustomerRecordEntity().get_edit_input("firstName"))
                    self.type(CustomerRecordEntity().get_edit_input("firstName"),
                              BasePage(self.driver).randomData("string", 6))
                    self.ctrl_all(CustomerRecordEntity().get_edit_input("lastName"))
                    self.type(CustomerRecordEntity().get_edit_input("lastName"),
                              BasePage(self.driver).randomData("string", 6))
                    self.drop_select(CustomerRecordEntity().get_edit_select("suffix"), suffix)
            else:
                self.ctrl_all(CustomerRecordEntity().get_edit_input("organizationName"))
                self.type(CustomerRecordEntity().get_edit_input("organizationName"),
                          BasePage(self.driver).randomData("string", 6))
                if entityClass == "Company" or entityClass == "Government":
                    self.drop_select(CustomerRecordEntity().get_edit_select("subClassName"), typeOfBusiness)
                self.drop_select(CustomerRecordEntity().get_edit_select("stateOfIncorporation"), stateOfIncorporation)


    def validate_records_rows(self):
        record = self.find_element(CustomerRecordEntity.entity_history).text
        if "total records: 1" in record:
            return True
        else:
            return False

    def without_BAN(self):
        """
        # Identifier Name Without BAN
        :param :
        :return:
        """
        identifierNameList = self.find_elements(CustomerRecordEntity.identifierNameList)
        name_item = None
        for i, item in enumerate(identifierNameList):
            if "BAN" == item.get_attribute("value"):
                name_item = (i + 1, item)
                break
        if name_item is None:
            logger.info("Without BAN type!")
            return True
        else:
            return  False

    def identifier_not_BAN_input(self,type):
        """
        # Identifier Name Without BAN input
        :param : type
        :return:
        """
        if type == "SSN" or type == "Federal EIN":
            self.type(CustomerRecordEntity.identifier, BasePage(self.driver).randomData("number", 9))
        elif type == "State Tax ID":
            self.type(CustomerRecordEntity.identifier, BasePage(self.driver).randomData("number", 11))
        elif type == "Agency ID":
            self.type(CustomerRecordEntity.identifier, BasePage(self.driver).randomData("number", 4))
        elif type == "Internal GLO ID" or type == "Unknown":
            self.type(CustomerRecordEntity.identifier, BasePage(self.driver).randomData("number", 6))

    def delete_related(self,section):
        """
        #Execute Delete for Related module
         :return:
        """
        self.sleep(2)
        self.click(CustomerRecordEntity.delete_confirm)
        if section == "Customer" and "Reassign links before C000048473 can be deleted" in self.get_tips_msg():
            return True
        if section == "Address" and "Reassign links before this site can be deleted" in self.get_tips_msg():
            return True
        if section == "Contact" and "Reassign links before this contact can be deleted" in self.get_tips_msg():
            return True
        if section == "Email" and "Reassign links before this contact email can be deleted" in self.get_tips_msg():
            return  True
        if section == "Phone" and "Reassign links before this contact phone can be deleted" in self.get_tips_msg():
             return  True
        else :
             return  False

    def validate_permission(self):
        """
        #Validation Permission
         :return:
        """
        if 'Access not Granted' in self.get_tips_msg():
            return True
        else:
            return False



















