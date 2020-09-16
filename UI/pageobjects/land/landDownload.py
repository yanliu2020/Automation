# -*- coding: utf-8 -*-
from  utils.base_page import  BasePage
from config.land.land_download_entity import DownLoadEntity
from config.common.topmenu_entity import TopMenuEntity
from utils.basepath_helper import config_path
from utils.logger import logger
from pageobjects.login.login import SystemLogin

class LandDownLoad(BasePage):
    def download(self,level,first_menu,second_menu,third_menu,four_menu,url):
        """
        #导航多级菜单选择
        :param first_menu,second_menu,third_menu,four_menu
        :param level
        :return:
        """
        self.sleep(2)
        self.click(TopMenuEntity().get_first_menu(first_menu))
        #return second_menu
        second_menu_list = self.find_elements(TopMenuEntity.second_menu_list)
        # print(second_menu_list)
        second_item = None
        for i, item2 in enumerate(second_menu_list):
            if second_menu == item2.text:
                second_item = (i + 1, item2)
                break

        if level == 2:
            if second_item is None:
                logger.info(msg="second_menu %s not found!" % second_menu)
            else:
                self.click(TopMenuEntity().get_second_menu(second_item[0]))
                logger.info('second_menu: %s' % second_menu)
                return True

        elif level == 3:
            # return third_menu
            third_menu_list = self.find_elements(TopMenuEntity().get_third_menu_list(second_item[0]))
            self.click(TopMenuEntity().get_second_menu(second_item[0]))
            third_item = None
            for i, item3 in enumerate(third_menu_list):
                if third_menu == item3.text:
                    third_item = (i + 1, item3)
                    break
            if third_item is None:
                logger.info(msg="third_menu %s not found!" % third_menu)
            else:
                if self.find_element(TopMenuEntity().get_third_menu(second_item[0], third_item[0])).get_attribute('href')== url:
                    self.click(TopMenuEntity().get_third_menu(second_item[0], third_item[0]))
                    return True
                else:
                    return False

        elif level ==4:
            # return third_menu
            self.click(TopMenuEntity().get_second_menu(second_item[0]))
            third_menu_list = self.find_elements(TopMenuEntity().get_third_menu_list(second_item[0]))
            third_item = None
            for i, item3 in enumerate(third_menu_list):
                if third_menu == item3.text:
                    third_item = (i + 1, item3)
                    break
            if third_item is None:
                logger.info(msg="third_menu %s not found!" % third_menu)
            else:
                self.click(TopMenuEntity().get_third_menu(second_item[0], third_item[0]))
                if self.find_element(TopMenuEntity().get_four_menu(second_item[0],third_item[0],four_menu)).get_attribute(
                    'href') == url:
                    # choose four menu
                    self.click(TopMenuEntity().get_four_menu(second_item[0], third_item[0], four_menu))
                    return True
                else:
                    return False
        self.sleep(2)