# -*- coding: utf-8 -*-


class TopMenuEntity(object):
    #logo
    logo = "id=>logo"
    #用户头像
    #user_log = "xpath=>//div[@class='header-badge']"
    user_log = "xpath=>//div[@class='header-badge-glo']"
    #退出登录
    logout_user = "xpath=>//a[text()='Logout']"

    #first_menu
    first_menu = "id=>%s"
    def get_first_menu(self,loc):
        return self.first_menu %loc

    #second_menu_list
    second_menu_list = "xpath=>//ul[@class='dropdown-menu multi-level show']/li/a"
    #second_menu
    second_menu = "xpath=>//ul[@class='dropdown-menu multi-level show']/li[%s]/a"
    def get_second_menu(self,loc):
        return self.second_menu %loc

    #third_menu_list
    third_menu_list = "xpath=>//ul[@class='dropdown-menu multi-level show']/li[%s]/ul/li/a"
    def get_third_menu_list(self,loc):
        return self.third_menu_list %loc
    #third_menu
    third_menu = "xpath=>//ul[@class='dropdown-menu multi-level show']/li[%s]/ul/li[%s]/a"
    def get_third_menu(self,loc1,loc2):
        return self.third_menu %(loc1,loc2)

    #four_menu
    four_menu = "xpath=>//ul[@class='dropdown-menu multi-level show']/li[%s]/ul/li[%s]/ul/li/a[text()='%s']"
    def get_four_menu(self,loc1,loc2,loc3):
        return self.four_menu %(loc1,loc2,loc3)







