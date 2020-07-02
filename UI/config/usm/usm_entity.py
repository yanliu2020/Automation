# -*- coding: utf-8 -*-

class UsmEntity(object):
    #tab页签
    record_tab = "xpath=>//div[@class='card']//li/a[text()='%s']"
    def get_record_tab(self, loc):
        return self.record_tab %loc

    #操作按钮
    operator = "xpath=>//div[@class='card']//button[text()=' %s']"
    def get_operator(self,loc):
        return  self.operator %loc

    #选中N行记录
    select_record = "xpath=>//div[@class='card']//div[@class='glo-row']//div[@class='rt-tr-group'][%s]/div"
    def get_select_record(self,loc):
        return  self.select_record %loc