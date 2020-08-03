# -*- coding: utf-8 -*-
from  utils.base_page import  BasePage
from config.customer.new_customer_entity import  NewCustomerEntity
from config.customer.customer_record_entity import CustomerRecordEntity
from pageobjects.customer.customerRecord import CustomerRecordPage
from utils.connect_sql import dbConnect
from utils.logger import logger

class NewCustomerPage(BasePage):

    def  business_entity(self,entityType,entityClass,salutation,suffix,typeOfBusiness,stateOfIncorporation):
        """
          #new multiple type customer
          :param  type,className
          :param  salutation,firstName,lastName,suffix,fullName,default_sort,organizationName,typeOfBusiness,stateOfIncorporation
          :return:
        """
        self.drop_select(NewCustomerEntity().get_entity("typeName"), entityType)
        self.drop_select(NewCustomerEntity().get_entity("entityClass"), entityClass)
        if entityType == "Person":
            if entityClass == "Household":
                self.type(NewCustomerEntity().get_entity_input("fullName"), BasePage(self.driver).randomData("string",6))
                self.type(NewCustomerEntity().get_entity_input("soundEx"), BasePage(self.driver).randomData("string",6))
            else:
                self.drop_select(NewCustomerEntity().get_entity_select("salutation"), salutation)
                self.type(NewCustomerEntity().get_entity_input("firstName"), BasePage(self.driver).randomData("string",6))
                self.type(NewCustomerEntity().get_entity_input("middleName"),BasePage(self.driver).randomData("string", 6))
                self.type(NewCustomerEntity().get_entity_input("lastName"), BasePage(self.driver).randomData("string",6))
                self.drop_select(NewCustomerEntity().get_entity_select("suffix"), suffix)
        else:
            self.type(NewCustomerEntity().get_entity_input("organizationName"), BasePage(self.driver).randomData("string",6))
            if entityClass == "Company" or entityClass == "Government":
                self.drop_select(NewCustomerEntity().get_entity_select("subClassName"), typeOfBusiness)
            self.drop_select(NewCustomerEntity().get_entity_select("stateOfIncorporation"), stateOfIncorporation)

    def add_remove(self,sectionName):
        """
        #Add and Remove
        :param sectionName
        :return:
        """
        self.click(NewCustomerEntity().get_add_remove(sectionName))

    def address(self,sectionName,addressType,stateCode):
        """
        #Address Information
        :param sectionName,addressType,address1,city,stateCode,postalCode
        :return:
        """
        self.click(NewCustomerEntity().get_add_remove(sectionName))
        self.type(CustomerRecordEntity().get_address_input("address1"), BasePage(self.driver).randomData("string", 6))
        self.drop_select(CustomerRecordEntity().get_address_select("addressType"),addressType)
        self.type(CustomerRecordEntity().get_address_input("city"),BasePage(self.driver).randomData("string", 6))
        self.drop_select(CustomerRecordEntity().get_address_select("stateCode"), stateCode)
        self.type(CustomerRecordEntity().get_address_input("postalCode"), BasePage(self.driver).randomData("number", 5))

    def identifier(self,sectionName,type):
        """
        #Identifier
        :param sectionName,type,identifierNo
        :return:
        """
        self.click(NewCustomerEntity().get_add_remove(sectionName))
        self.drop_select(CustomerRecordEntity.identifierName,type)
        if type == "SSN" or type == "Federal EIN":
            self.type(CustomerRecordEntity.identifier,BasePage(self.driver).randomData("number", 9))
        elif type == "State Tax ID":
            self.type(CustomerRecordEntity.identifier, BasePage(self.driver).randomData("number", 11))
        elif type == "Agency ID":
            self.type(CustomerRecordEntity.identifier, BasePage(self.driver).randomData("number", 4))
        else :
            self.type(CustomerRecordEntity.identifier, BasePage(self.driver).randomData("number", 6))

    def save(self):
        """
        #Save validation
        :param
        :return:
        """
        self.click(NewCustomerEntity.save)
        self.sleep(1)
        if "successfully" in CustomerRecordPage(self.driver).get_tips_msg():
            return True
        else:
            return False


    def contact(self,same,index,flag,role,emailType,phoneType):
        """
        #Multiple Contact Information
        :param  index,flag,firstName,lastName,role,emailType,email,areaCode,phone,type
        :return:
        """
        if index == 3:
            self.click(NewCustomerEntity().get_add_remove("Contact 2"))
        if same is False:
            self.type(NewCustomerEntity().get_contact_input(index, "firstName"), BasePage(self.driver).randomData("string", 6))
            self.type(NewCustomerEntity().get_contact_input(index, "lastName"), BasePage(self.driver).randomData("string", 6))
            self.drop_select(NewCustomerEntity().get_contact_role(index), role)
        else:
            self.click(NewCustomerEntity.same_as)
        self.drop_select(NewCustomerEntity().get_email_type(index), emailType)
        self.type(NewCustomerEntity().get_email(index), BasePage(self.driver).randomData("string", 6)+"@"+
                  BasePage(self.driver).randomData("string", 4)+".com")
        self.type(NewCustomerEntity().get_phone_input(index, flag, "areaCode"), BasePage(self.driver).randomData("number", 3))
        self.type(NewCustomerEntity().get_phone_input(index, flag, "phone"), BasePage(self.driver).randomData("number", 7))
        self.drop_select(NewCustomerEntity().get_phone_type(index, flag), phoneType)

    def add_phone(self,sectionName,index,flag,type):
        """
        #Multiple Phone Information
        :param  sectionName,index,flag,areaCode,phone,type
        :return:
        """
        self.click(NewCustomerEntity().get_add_phone(index,sectionName))
        self.type(NewCustomerEntity().get_phone_input(index, flag, "areaCode"), BasePage(self.driver).randomData("number", 3))
        self.type(NewCustomerEntity().get_phone_input(index, flag, "phone"), BasePage(self.driver).randomData("number", 7))
        self.drop_select(NewCustomerEntity().get_phone_type(index, flag), type)

    def validation_data(self):
        """
        #validate the data accuracy
        :param
        :return:
        """
        customerId = self.find_element(NewCustomerEntity().get_value("customer-id")).get_attribute('value')
        organizationName = self.find_element(NewCustomerEntity().get_value("organization-name")).get_attribute('value')
        entityType = self.find_element(NewCustomerEntity().get_value("entity-type")).get_attribute('value')
        if entityType == "Person":
            CustomerId = dbConnect().getdata('MCDH', 'CustomerId_Person', organizationName)
        elif entityType == "Organization":
            CustomerId = dbConnect().getdata('MCDH', 'CustomerId_Organization', organizationName)
        if customerId == CustomerId:
            return True
        else:
            logger.info("customerId %s new customer failed!"% customerId)
            return False

























