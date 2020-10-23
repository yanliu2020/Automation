# -*- coding: utf-8 -*-
class LandDetailsEntity(object):

    # top operate buttons
    land_operate = "xpath=>//div[@class='btn-toolbar']/button[text()='%s']"
    def get_land_operate(self, loc):
        return self.land_operate % loc

    # Actions下拉选项
    action = "xpath=>//div[@class='btn-toolbar show']/ul//a[text()='%s']"
    def get_action(self, loc):
        return self.action % loc

    #Sale tab>>reservations 复选框
    reservations = "xpath=>//div[@title='reservations']/label"
    reservation = "xpath=>//div[@title='reservations']/label[%s]"
    def get_reservation(self,loc):
        return self.reservation %loc

