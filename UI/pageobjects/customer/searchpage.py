# -*- coding: utf-8 -*-

from  utils.base_page import  BasePage
from config.customer.search_customer_entity import  SearchCustomerEntity
from utils.logger import  logger

class SearchCustomerPage(BasePage):
    #assert into search page
    def  searchPage_visible(self):
        """
        # 进入Search 页面
        :return:
        """
        text = self.find_element(SearchCustomerEntity.assert_title)

    #click top button
    def  click_top_button(self,name):
        """
        # 顶部按钮操作
        :return:
        """
        self.find_element(SearchCustomerEntity().get_top_button(name))

