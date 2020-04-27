# -*- coding: utf-8 -*-
from configparser import ConfigParser

from selenium.common.exceptions import NoSuchElementException
from config.common.topmenu_entity import TopMenuEntity
from utils.base_page import BasePage
from utils.basepath_helper import config_path
from utils.logger import logger
from config.homepage.homepage_entity import HomepageEntity
from pageobjects.login.login import SystemLogin
from config.customer.search_customer_entity import  SearchCustomerEntity


class TopMenuPage(BasePage):

    def get_url(self):
        """
        # 重新访问服务器，页面重定向到默认看板
        :return:
        """
        config = ConfigParser()
        file_path = config_path + 'config.ini'
        config.read(file_path)
        base_url = config.get("testServer", "URL")
        self.driver.get(base_url)
        # 记录 executor_url 和 session_id 以便复用session
        executor_url = self.driver.command_executor._url
        session_id = self.driver.session_id

        # try:
        #     self.sleep(5)
        #     self.find_element_by_wait('xpath',HomepageEntity.default_text)
        #     #self.find_element(HomepageEntity.default_text)
        # except NoSuchElementException:
        #     pass
        # else:
        #     logger.info('页面加载完成')

    def logout(self):
        """
        # 退出账号
        :return:
        """
        self.find_element_by_wait('xpath',TopMenuEntity.user_log)
        self.click(TopMenuEntity.user_log)
        self.click(TopMenuEntity.logout_user)
        if SystemLogin(self.driver).is_login_page():
            logger.info('logout success')
            return True
        else:
            logger.error('logout fail')
            return False


    def choose_top_menu(self,level,first_menu,second_menu,third_menu,four_menu):
        """
        #choose first and second menu
        :param first_menu,second_menu:third_menu
        :param level
        :return:
        """
        self.click(TopMenuEntity().get_first_menu(first_menu))
        #return second_menu
        second_menu_list = self.find_elements(TopMenuEntity.second_menu_list)
        print(second_menu_list)
        second_item = None
        for i, item2 in enumerate(second_menu_list):
            if second_menu == item2.text:
                second_item = (i + 1, item2)
                break

        if level == 2:
            if second_item is None:
                raise NoSuchElementException(msg="second_menu %s not found!" % second_menu)
            else:
                self.click(TopMenuEntity().get_second_menu(second_item[0]))
                logger.info('second_menu: %s' % second_menu)
                return True

        elif level == 3:
            # return third_menu
            third_menu_list = self.find_elements(TopMenuEntity().get_third_menu_list(second_item[0]))
            self.move_to_element(TopMenuEntity().get_second_menu(second_item[0]))
            third_item = None
            for i, item3 in enumerate(third_menu_list):
                if third_menu == item3.text:
                    third_item = (i + 1, item3)
                    break
            if third_item is None:
                raise NoSuchElementException(msg="second_menu %s not found!" % third_menu)
            else:
                self.click(TopMenuEntity().get_third_menu(second_item[0], third_item[0]))
                logger.info('third_menu: %s' % third_menu)
                return True

        elif level ==4:
            # return third_menu
            third_menu_list = self.find_elements(TopMenuEntity().get_third_menu_list(second_item[0]))
            self.move_to_element(TopMenuEntity().get_second_menu(second_item[0]))
            third_item = None
            for i, item3 in enumerate(third_menu_list):
                if third_menu == item3.text:
                    third_item = (i + 1, item3)
                    break
            #choose four menu
            self.move_to_element(TopMenuEntity().get_third_menu(second_item[0],third_item[0]))
            self.click(TopMenuEntity().get_four_menu(second_item[0],third_item[0],four_menu))
            logger.info('four_menu: %s' % four_menu)
            return True







