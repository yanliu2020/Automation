# -*- coding: utf-8 -*-

class DownLoadEntity(object):
    # third_menu
    third_menu = "xpath=>//ul[@class='dropdown-menu multi-level show']//a[contains(text(),'%s')]"

    def get_third_menu(self, loc):
        return self.third_menu %loc

    # four_menu
    four_menu = "xpath=>//ul[@class='dropdown-menu multi-level show']/li[%s]/ul/li[%s]/ul/li/a[text()='%s']"

    def get_four_menu(self, loc1, loc2, loc3):
        return self.four_menu % (loc1, loc2, loc3)