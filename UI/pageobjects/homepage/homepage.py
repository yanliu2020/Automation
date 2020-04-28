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
    def search_or_add(self,module_name,operator_name):
        """
        #click search or add new
        :param  module_name : Land,Surface Leasing,Mineral Leasing,Customers
        :param  operator_name : Search, Add New(注意前面加空格)
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
        else:
            self.click(HomePageEntity().get_module_operator(module_item[0],operator_name))
            logger.info('module_name: %s' % module_name)
            return True
