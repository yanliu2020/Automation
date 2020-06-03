# -*- coding: utf-8 -*-

from  utils.base_page import  BasePage
from config.customer.new_customer_entity import  NewCustomerEntity
from config.customer.customer_record_entity import CustomerRecordEntity
from pageobjects.customer.customerRecord import CustomerRecordPage
from utils.logger import  logger

class NewCustomerPage(BasePage):

    def  business_entity(self,entityType,entityClass,salutation,firstName,lastName,suffix,fullName,default_sort,organizationName,typeOfBusiness,stateOfIncorporation):
        """
          #new multiple type customer
          :param  type,className
          :param  salutation,firstName,lastName,suffix,fullName,default_sort,organizationName,typeOfBusiness,stateOfIncorporation
          :return:
        """
        self.drop_select(NewCustomerEntity().get_entity("entityType"), entityType)
        self.drop_select(NewCustomerEntity().get_entity("entityClass"), entityClass)
        if entityType == "Person":
            if entityClass == "Household":
                self.ctrl_all(NewCustomerEntity().get_entity_input("fullName"))
                self.type(NewCustomerEntity().get_entity_input("fullName"), fullName)
                self.ctrl_all(NewCustomerEntity().get_entity_input("defaultSort"))
                self.type(NewCustomerEntity().get_entity_input("defaultSort"), default_sort)
            else:
                self.drop_select(NewCustomerEntity().get_entity_select("salutation"), salutation)
                self.ctrl_all(NewCustomerEntity().get_entity_input("firstName"))
                self.type(NewCustomerEntity().get_entity_input("firstName"), firstName)
                self.ctrl_all(NewCustomerEntity().get_entity_input("lastName"))
                self.type(NewCustomerEntity().get_entity_input("lastName"), lastName)
                self.drop_select(NewCustomerEntity().get_entity_select("suffix"), suffix)
        else:
            self.ctrl_all(NewCustomerEntity().get_entity_input("organizationName"))
            self.type(NewCustomerEntity().get_entity_input("organizationName"), organizationName)
            if entityClass == "Trust/Estate":
                self.drop_select(NewCustomerEntity().get_entity_select("stateOfIncorporation"), stateOfIncorporation)
            else:
                self.drop_select(NewCustomerEntity().get_entity_select("typeOfBusiness"), typeOfBusiness)
                self.drop_select(NewCustomerEntity().get_entity_select("stateOfIncorporation"), stateOfIncorporation)

    def add_remove(self,sectionName):
        """
        #Add and Remove
        :param sectionName
        :return:
        """
        self.click(NewCustomerEntity().get_add_remove(sectionName))

    def address(self,sectionName,addressType,address1,city,stateCode,postalCode):
        """
        #Address Information
        :param sectionName,addressType,address1,city,stateCode,postalCode
        :return:
        """
        self.click(NewCustomerEntity().get_add_remove(sectionName))
        self.drop_select(CustomerRecordEntity.addressType,addressType)
        self.type(CustomerRecordEntity.address1,address1)
        self.type(CustomerRecordEntity.city,city)
        self.drop_select(CustomerRecordEntity.stateCode, stateCode)
        self.type(CustomerRecordEntity.postalCode, postalCode)

    def identifier(self,sectionName,type,identifierNo):
        """
        #Identifier
        :param sectionName,type,identifierNo
        :return:
        """
        self.click(NewCustomerEntity().get_add_remove(sectionName))
        self.drop_select(CustomerRecordEntity.identifierName,type)
        self.type(CustomerRecordEntity.identifier,identifierNo)


    def save(self):
        """
        #保存校验
        :param
        :return:
        """
        self.click(NewCustomerEntity.save)
        if "successfully" in CustomerRecordPage(self.driver).get_tips_msg():
            return True
        else:
            return False

    def contact(self,index,flag,firstName,lastName,role,emailType,email,areaCode,phone,type):
        """
        #Multiple Contact Information
        :param  index,flag,firstName,lastName,role,emailType,email,areaCode,phone,type
        :return:
        """
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
        """
        #Multiple Phone Information
        :param  sectionName,index,flag,areaCode,phone,type
        :return:
        """
        self.click(NewCustomerEntity().get_add_phone(index,sectionName))
        self.type(NewCustomerEntity().get_phone_input(index, flag, "areaCode"), areaCode)
        self.type(NewCustomerEntity().get_phone_input(index, flag, "phone"), phone)
        self.drop_select(NewCustomerEntity().get_phone_type(index, flag), type)



















