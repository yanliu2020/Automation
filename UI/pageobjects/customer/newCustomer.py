# -*- coding: utf-8 -*-

from  utils.base_page import  BasePage
from config.customer.new_customer_entity import  NewCustomerEntity
from config.customer.customer_record_entity import CustomerRecordEntity
from pageobjects.customer.customerRecord import CustomerRecordPage
from utils.logger import  logger

class NewCustomerPage(BasePage):

    def  Business_Entity(self,type,className,salutation,firstName,lastName,suffix,fullName,default_sort,organizationName,typeOfBusiness,stateOfIncorporation):
        """
          #选择用户类型，输入Business Entity信息
          :param  type,className
          :param  salutation,firstName,lastName,suffix,fullName,default_sort,organizationName,typeOfBusiness,stateOfIncorporation
          :return:
        """
        self.drop_select(NewCustomerEntity.entity_type,type)
        self.drop_select(NewCustomerEntity.entity_class,className)
        if type == "Person":
            if className == "Household":
                self.type(NewCustomerEntity.fullName, fullName)
                self.type(NewCustomerEntity.default_sort, default_sort)
            else:
                self.drop_select(NewCustomerEntity().get_salutation(1), salutation)
                self.type(NewCustomerEntity().get_firstName(1), firstName)
                self.type(NewCustomerEntity().get_lastName(1), lastName)
                self.drop_select(NewCustomerEntity().get_suffix(1), suffix)
        else:
            if className == "Trust/Estate":
                self.type(NewCustomerEntity.organizationName, organizationName)
                self.drop_select(NewCustomerEntity.stateOfIncorporation, stateOfIncorporation)
            else:
                self.type(NewCustomerEntity.organizationName, organizationName)
                self.drop_select(NewCustomerEntity.typeOfBusiness, typeOfBusiness)
                self.drop_select(NewCustomerEntity.stateOfIncorporation, stateOfIncorporation)

    def add_remove(self,sectionName):
        self.click(NewCustomerEntity().get_add_remove(sectionName))

    def Address(self,sectionName,addressType,address1,city,stateCode):
        self.click(NewCustomerEntity().get_add_remove(sectionName))
        self.drop_select(CustomerRecordEntity.addressType,addressType)
        self.type(CustomerRecordEntity.address1,address1)
        self.type(CustomerRecordEntity.city,city)
        self.drop_select(CustomerRecordEntity.stateCode, stateCode)

    def Identifier(self,sectionName,type,identifierNo):
        self.click(NewCustomerEntity().get_add_remove(sectionName))
        self.drop_select(CustomerRecordEntity.identifierName,type)
        self.type(CustomerRecordEntity.identifier,identifierNo)


    def save(self):
        self.click(NewCustomerEntity.save)
        if "successfully" in CustomerRecordPage(self.driver).get_tips_msg():
            return True
        else:
            return False












