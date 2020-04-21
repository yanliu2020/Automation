# -*- coding: utf-8 -*-

from  utils.base_page import  BasePage
from config.customer.search_customer_entity import  SearchCustomerEntity
from utils.logger import  logger

class SearchCustomerPage(BasePage):
    #assert into search page
    def  searchPage_visible(self):
        text = self.find_element(SearchCustomerEntity.assert_title)

    #click top button
    def  click_top_button(self,name):
        self.find_element(SearchCustomerEntity().get_top_button(name))

