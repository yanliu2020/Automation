# -*- coding: utf-8 -*-
from  utils.base_page import  BasePage
from config.customer.new_customer_entity import  NewCustomerEntity
from config.customer.customer_record_entity import CustomerRecordEntity
from pageobjects.customer.customerRecord import CustomerRecordPage
from utils.connect_sql import dbConnect
from utils.logger import logger

class NewCustomerPage(BasePage):
    def is_newCustomer_page(self):
        if self.find_element(NewCustomerEntity.default_text):
            return True
        else:
            return False

    def  business_entity(self,entityType,entityClass,salutation,suffix,typeOfBusiness,stateOfIncorporation):
        """
          #new multiple type customer
          :param  type,className
          :param  salutation,firstName,lastName,suffix,fullName,default_sort,organizationName,typeOfBusiness,stateOfIncorporation
          :return:
        """
        if self.is_newCustomer_page()== True:
            self.drop_select(NewCustomerEntity().get_field_select("typeName"), entityType)
            self.drop_select(NewCustomerEntity().get_field_select("entityClass"), entityClass)
            randomData = BasePage(self.driver).randomData("string", 6)
            if entityType == "Person":
                if entityClass == "Household":
                    self.type(NewCustomerEntity().get_field_input("fullName"), randomData)
                    self.type(NewCustomerEntity().get_field_input("soundEx"), randomData)
                else:
                    self.drop_select(NewCustomerEntity().get_field_select("salutation"), salutation)
                    self.type(NewCustomerEntity().get_field_input("firstName"), randomData)
                    self.type(NewCustomerEntity().get_field_input("middleName"), randomData)
                    self.type(NewCustomerEntity().get_field_input("lastName"), randomData)
                    self.drop_select(NewCustomerEntity().get_field_select("suffix"), suffix)
            else:
                self.type(NewCustomerEntity().get_field_input("organizationName"), randomData)
                if entityClass == "Company" or entityClass == "Government":
                    self.drop_select(NewCustomerEntity().get_field_select("subClassName"), typeOfBusiness)
                self.drop_select(NewCustomerEntity().get_field_select("stateOfIncorporation"), stateOfIncorporation)


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
        self.type(CustomerRecordEntity().get_field_input("address1"), BasePage(self.driver).randomData("string", 6))
        self.drop_select(CustomerRecordEntity().get_field_select("addressType"),addressType)
        self.type(CustomerRecordEntity().get_field_input("city"),BasePage(self.driver).randomData("string", 6))
        self.drop_select(CustomerRecordEntity().get_field_select("stateCode"), stateCode)
        self.type(CustomerRecordEntity().get_field_input("postalCode"), BasePage(self.driver).randomData("number", 5))

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

    def saveClick(self):
        """
        #Save validation
        :param
        :return:
        """
        self.click(NewCustomerEntity.save)
        self.sleep(3)


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
        if CustomerRecordPage(self.driver).is_customer_record_page():
            customerId = self.find_element(NewCustomerEntity().get_field_input("customer-id")).get_attribute('value')
            organizationName = self.find_element(NewCustomerEntity().get_field_input("organization-name")).get_attribute(
                'value')
            entityType = self.find_element(NewCustomerEntity().get_field_input("entity-type")).get_attribute('value')
            if entityType == "Person":
                CustomerId = dbConnect().getdata('MCDH', 'CustomerId_Person', organizationName)
            elif entityType == "Organization":
                CustomerId = dbConnect().getdata('MCDH', 'CustomerId_Organization', organizationName)
            if customerId == CustomerId:
                return True
            else:
                logger.info("customerId %s new customer failed!" % customerId)
                return False


    def get_required_msg(self):
        """
        # get the required msg
        :return:
        """
        msg_list = self.find_elements(NewCustomerEntity.msg_list)
        string_list = []
        msg = ''
        for i, item in enumerate(msg_list):
            msg= msg + item.text
            # string_list.append(item.text)
        # msg = "".join(string_list)
        message = msg.replace('\n', '').replace('\r', '')
        return message

    def validate_required(self,entityType,entityClass,flag):
        if self.is_newCustomer_page():
            self.drop_select(NewCustomerEntity().get_field_select("typeName"), entityType)
            self.drop_select(NewCustomerEntity().get_field_select("entityClass"), entityClass)
            if flag == "Business Entity":
                self.click(NewCustomerEntity.save)
                self.sleep(1)
                if entityType == "Person":
                    if entityClass == "Household":
                        if "Required but Missing Fields:Business Entity:Full Name, Default Sort" in self.get_required_msg():
                            return True
                        else:
                            return False
                    else:
                        if "Required but Missing Fields:Business Entity:First Name, Last Name" in self.get_required_msg():
                            return True
                        else:
                            return False
                else:
                    if "Required but Missing Fields:Business Entity:Organization Name" in self.get_required_msg():
                        return True
                    else:
                        return False
            else:
                self.type(NewCustomerEntity().get_field_input("firstName"),
                          BasePage(self.driver).randomData("string", 6))
                self.type(NewCustomerEntity().get_field_input("lastName"),
                          BasePage(self.driver).randomData("string", 6))
                if flag == "Contact":
                    self.drop_select(NewCustomerEntity().get_contact_select(1, "salutation"), "Ms.")
                    self.drop_select(NewCustomerEntity().get_email_type(1), "Personal")
                    self.type(NewCustomerEntity().get_phone_input(1, 1, "ext"),
                              BasePage(self.driver).randomData("string", 6))
                    self.click(NewCustomerEntity.save)
                    self.sleep(1)
                    if "Required but Missing Fields:Contact 1:First Name, Last Name, Contact RoleContact 1 Email:Email AddressContact 1 Phone 1:Area Code, Phone, Phone Type" \
                            in self.get_required_msg():
                        return True
                    else:
                        return False
                elif flag == "Address&Identifier":
                    self.click(NewCustomerEntity().get_add_remove("Address"))
                    self.drop_select(CustomerRecordEntity().get_field_select("country"), "USA")
                    self.click(NewCustomerEntity().get_add_remove("Identifier"))
                    self.drop_select(CustomerRecordEntity.identifierName, "SSN")
                    self.click(NewCustomerEntity.save)
                    self.sleep(1)
                    if "Required but Missing Fields:Address:Address1, Address Type, CityIdentifier:Identifier" in self.get_required_msg():
                        return True
                    else:
                        return False






































