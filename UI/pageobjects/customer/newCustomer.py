# -*- coding: utf-8 -*-

from  utils.base_page import  BasePage
from config.customer.new_customer_entity import  NewCustomerEntity
from config.customer.customer_record_entity import CustomerRecordEntity
from pageobjects.customer.customerRecord import CustomerRecordPage
from utils.logger import  logger

class NewCustomerPage(BasePage):

    def  business_entity(self,entityType,entityClass,salutation,firstName,lastName,suffix,fullName,default_sort,organizationName,typeOfBusiness,stateOfIncorporation):
        """
          #选择用户类型，输入Business Entity信息
          :param  type,className
          :param  salutation,firstName,lastName,suffix,fullName,default_sort,organizationName,typeOfBusiness,stateOfIncorporation
          :return:
        """
        self.drop_select(NewCustomerEntity().get_entity("entityType"), entityType)
        self.drop_select(NewCustomerEntity().get_entity("entityClass"), entityClass)
        if entityType == "Person":
            if entityClass == "Household":
                self.type(NewCustomerEntity().get_entity_input("fullName"), fullName)
                self.type(NewCustomerEntity().get_entity_input("defaultSort"), default_sort)
            else:
                self.drop_select(NewCustomerEntity().get_entity_select("salutation"), salutation)
                self.type(NewCustomerEntity().get_entity_input("firstName"), firstName)
                self.type(NewCustomerEntity().get_entity_input("lastName"), lastName)
                self.drop_select(NewCustomerEntity().get_entity_select("suffix"), suffix)
        else:
            self.type(NewCustomerEntity().get_entity_input("organizationName"), organizationName)
            if entityType == "Trust/Estate":
                self.drop_select(NewCustomerEntity().get_entity_select("stateOfIncorporation"), stateOfIncorporation)
            else:
                self.drop_select(NewCustomerEntity().get_entity_select("typeOfBusiness"), typeOfBusiness)
                self.drop_select(NewCustomerEntity().get_entity_select("stateOfIncorporation"), stateOfIncorporation)

    def add_remove(self,sectionName):
        self.click(NewCustomerEntity().get_add_remove(sectionName))

    def address(self,sectionName,addressType,address1,city,stateCode,postalCode):
        self.click(NewCustomerEntity().get_add_remove(sectionName))
        self.drop_select(CustomerRecordEntity.addressType,addressType)
        self.type(CustomerRecordEntity.address1,address1)
        self.type(CustomerRecordEntity.city,city)
        self.drop_select(CustomerRecordEntity.stateCode, stateCode)
        self.type(CustomerRecordEntity.postalCode, postalCode)

    def identifier(self,sectionName,type,identifierNo):
        self.click(NewCustomerEntity().get_add_remove(sectionName))
        self.drop_select(CustomerRecordEntity.identifierName,type)
        self.type(CustomerRecordEntity.identifier,identifierNo)


    def save(self):
        self.click(NewCustomerEntity.save)
        self.find_element_by_wait("xpath",CustomerRecordEntity.tips_msg)
        if "successfully" in CustomerRecordPage(self.driver).get_tips_msg():
            return True
        else:
            return False

    def contact(self,index,flag,firstName,lastName,role,emailType,email,areaCode,phone,type):
        if index == 3:
            self.click(NewCustomerEntity().get_add_remove("Contact 2"))
        self.type(NewCustomerEntity().get_contact_input(index,"firstName"),firstName)
        self.type(NewCustomerEntity().get_contact_input(index, "lastName"), lastName)
        self.drop_select(NewCustomerEntity().get_contact_role(index),role)
        self.drop_select(NewCustomerEntity().get_email_type(index), emailType)
        self.type(NewCustomerEntity().get_email(index), email)
        self.type(NewCustomerEntity().get_phone_input(index,flag,"areaCode"), areaCode)
        self.type(NewCustomerEntity().get_phone_input(index,flag, "phone"), phone)
        self.drop_select(NewCustomerEntity().get_phone_type(index,flag),type)

    def add_phone(self,sectionName,index,flag,areaCode,phone,type):
        self.click(NewCustomerEntity().get_add_phone(index,sectionName))
        self.type(NewCustomerEntity().get_phone_input(index, flag, "areaCode"), areaCode)
        self.type(NewCustomerEntity().get_phone_input(index, flag, "phone"), phone)
        self.drop_select(NewCustomerEntity().get_phone_type(index, flag), type)



















