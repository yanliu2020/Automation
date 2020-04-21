# -*- coding: utf-8 -*-

from  utils.base_page import  BasePage
from config.homepage.homepage_entity import  HomepageEntity

class HomePage(BasePage):
    #校验进入首页
    def is_visibility_homepage(self):
        self.find_element_by_wait("xpath",HomepageEntity.default_text)
        return bool(self.find_element(HomepageEntity.default_text))
        print("++++进入首页")