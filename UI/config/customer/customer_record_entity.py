# -*- coding: utf-8 -*-

class CustomerRecordEntity(object):
    #top button
    top_button = "xpath=>//div[@class='btn-toolbar show']/button[text()='%s']"
    def get_top_button(self,loc):
        return self.top_button %loc

    #Actions submenu
    action_submenu = "xpath=>//div[@class='btn-toolbar show']/ul//a[text()='%s']"
    def get_action_submenu(self,loc):
        return self.action_submenu %loc

    #record tab
    record_tab = "xpath=>//div[@class='card']//li/a[text()='%s']"
    def get_record_tab(self,loc):
        return self.record_tab %loc

    #Entity>>Customer Summary,Addresses,Websites,Doing Business As (DBA),Business Identifiers
    #Contacts>>Contacts,Email,Phone
    section_list = "xpath=>//div[@class='card']//div//h4"

    #Entity和Contacts下section的操作按钮
    section_operator = "xpath=>//div[@class='glo-row']/div[%s]//button[text()='%s']"
    def get_section_operator(self,loc1,loc2):
        return  self.section_operator %(loc1,loc2)

    #Related Leases/Lands>>Lands,Mineral Leases，Surface Leases，Surface Projects
    related_section_list = "xpath=>//div[@class='reactTable-full']/div//h3"

    #Related Leases/Lands下的操作按钮
    related_section_operator = "xpath=>//div[@class='reactTable-full']/div[%s]//a[text()='%s']"
    def get_related_operator(self,loc1,loc2):
        return  self.related_section_operator %(loc1,loc2)

