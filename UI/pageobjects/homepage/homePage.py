# -*- coding: utf-8 -*-

from  utils.base_page import  BasePage
from config.homepage.homepage_entity import  HomePageEntity
from config.common.topmenu_entity import TopMenuEntity
from selenium.common.exceptions import NoSuchElementException
from utils.logger import logger

class HomePage(BasePage):
    #校验进入首页
    def is_visibility_homepage(self):
        # self.find_element_by_wait("xpath",HomePageEntity.default_text)
        if self.find_element(HomePageEntity.default_text):
            return True
        else:
            return False




    #点击login
    def click_logo(self):
        self.click(TopMenuEntity.logo)

    #首页快捷入口
    def quick_entrance(self,module_name,Name,flag):
        """
        #default page quickly entrance
        :param  module_name : Land,Surface Leasing,Mineral Leasing,Customers
        :param  Name :Search,Add New,select_value,input_value
        :param  flag : 1,2
        :return:
        """
        self.find_element_by_wait("xpath",HomePageEntity.module_list)
        module_list = self.find_elements(HomePageEntity.module_list)
        # print(module_list)
        module_item = None
        for i, item in enumerate(module_list):
            if module_name == item.text:
                module_item = (i + 1, item)
                break
        if module_item is None:
            logger.info("module_name %s not found!" % module_name)
        #下拉框选择
        elif flag == 1:
            self.find_element(HomePageEntity().get_quick_select(module_item[0]))
            self.click(HomePageEntity().get_quick_select(module_item[0]))
            self.drop_select(HomePageEntity().get_quick_select(module_item[0]),Name)
            self.click(HomePageEntity().get_quick_select_go(module_item[0]))
            logger.info('module_name: %s' % module_name)
        #输入文本
        elif flag == 2:
            self.type(HomePageEntity().get_quick_search(module_item[0]),Name)
            self.click(HomePageEntity().get_quick_search_go(module_item[0]))
            logger.info('module_name: %s' % module_name)
        #点击按钮
        else:
            self.click(HomePageEntity().get_module_operator(module_item[0],Name))
            logger.info('module_name: %s' % module_name)










