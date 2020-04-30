# -*- coding: utf-8 -*-

from  utils.base_page import  BasePage
from config.homepage.homepage_entity import  HomePageEntity
from selenium.common.exceptions import NoSuchElementException
from utils.logger import logger

class HomePage(BasePage):
    #校验进入首页
    def is_visibility_homepage(self):
        return bool(self.find_element(HomePageEntity.default_text))

    #首页点击Search && Add New
    def quick_operator(self,module_name,Name,flag):
        """
        #click search or add new
        :param  module_name : Land,Surface Leasing,Mineral Leasing,Customers
        :param  Name : Search, Add New(注意前面加空格),select_value,input_value
        :param  flag : 1,2
        :return:
        """
        module_list = self.find_elements(HomePageEntity.module_list)
        print(module_list)
        module_item = None
        for i, item in enumerate(module_list):
            if module_name == item.text:
                module_item = (i + 1, item)
                break
        if module_item is None:
            raise NoSuchElementException(msg="module_name %s not found!" % module_name)
        #下拉框选择
        elif flag ==1:
            self.find_element(HomePageEntity().get_quick_select(module_item[0]))
            self.click(HomePageEntity().get_quick_select(module_item[0]))
            self.drop_select(HomePageEntity().get_quick_select(module_item[0]), Name)
            self.click(HomePageEntity().get_quick_select_go(module_item[0]))
            logger.info('module_name: %s' % module_name)
            return True
        #输入文本
        elif flag ==2:
            self.type(HomePageEntity().get_quick_search(module_item[0]), Name)
            self.click(HomePageEntity().get_quick_search_go(module_item[0]))
            logger.info('module_name: %s' % module_name)
            return True
        #点击按钮
        else:
            self.click(HomePageEntity().get_module_operator(module_item[0],Name))
            logger.info('module_name: %s' % module_name)
            return True








