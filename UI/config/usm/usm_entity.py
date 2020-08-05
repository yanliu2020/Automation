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

    #roleName, roleDescription
    input_textbox = "xpath=>//input[@name='%s']"
    def get_input_textbox(self,loc):
        return self.input_textbox %loc

    #Capabilities/Users
    switch_tab = "xpath=>//div[@class='mb-0 card']//li/a[text()='%s']"
    def get_switch_tab(self,loc):
        return self.switch_tab %loc

    #Filter
    filter = "xpath=>//input[@class='form-control']"

    # availableUsersSelected/assignedUsers/availableRolesSelected/assignedRolesSelected
    two_list = "xpath=>//select[@name='%s']"
    def get_two_list(self,loc):
        return self.two_list %loc

    list_value = "xpath=>//select[@name='%s']/option[%s]"
    def get_list_value(self,loc1,loc2):
        return  self.list_value %(loc1,loc2)

    #Add.Remove,Previous,Next,Finish,Cancel
    button = "xpath=>//button[contains(text(),'%s')]"
    def get_button(self,loc):
        return self.button %loc

    #confirm delete
    confirm_delete = "xpath=>//button[text()='Yes, Inactivate it!]"

    #Capabilities
    # capability = "xpath=>//div[@class='modal fade show']//div[@class='card']//div[@class='rt-tr-group']//div[text()='%s']"
    # def get_capability(self,loc):
    #     return self.capability %loc

    capability= "xpath=>//div[@class='modal fade show']//div[@class='glo-row']//input[@id='can%s_%s']"
    #canRead_0,canUpdate_0,canCreate_0,canDelete_0,canMassUpdate_0
    def get_capability(self,loc1,loc2):
        return self.capability %(loc1,loc2)

    capabilitity_list = "xpath=>//div[@class='mb-0 card']//div[@class='rt-table']/div[@class='rt-tbody']//div[@class='rt-td']"



