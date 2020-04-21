# -*- coding: utf-8 -*-

from  utils.base_page import  BasePage
from config.common.homepage_entity import  homepageEntity

class homePage(BasePage):
    #校验进入首页
    def is_visibility_homepage(self):
        return bool(self.find_element(homepageEntity.default_text))