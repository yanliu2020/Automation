# -*- coding: utf-8 -*-

from  utils.base_page import  BasePage
from config.customer.new_customer_entity import  NewCustomerEntity
from utils.logger import  logger

class NewCustomerPage(BasePage):
    #选择用户类型
    def  choose_cust_type(self,type,className):
        self.click(NewCustomerEntity.entity_type)
        self.drop_select(NewCustomerEntity.entity_type,type)
        self.click(NewCustomerEntity.entity_class)
        self.drop_select(NewCustomerEntity.entity_class,className)



