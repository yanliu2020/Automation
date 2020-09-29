# -*- coding: utf-8 -*-
class LandCommonEntity(object):
    # input fields
    field_input = "xpath=>//input[@name='%s']"
    def get_field_input(self,loc):
        return self.field_input %loc

    # select fields
    field_select = "xpath=>//select[@name='%s']"
    def get_field_select(self,loc):
        return self.field_select %loc

    #textarea fields
    field_textarea = "xpath=>//textarea[@name='%s']"
    def get_field_textarea(self,loc):
        return self.field_textarea %loc

    #save/cancel
    button = "xpath=>//button[text()='%s']"
    def get_land_button(self,loc):
        return self.button %loc

    #Date Picker
    Date_list = "xpath=>//div[@class='react-datepicker__month']/div/div"
    Selected_Date = "xpath=>//div[@class='react-datepicker__month']/div/div[@tabindex='0']"

    # 关闭弹窗
    close = "xpath=>//button[@class='close']"

    #*
    required_field = "xpath=>//span[@class='required']"

    #required_field_name
    required_field_name = "xpath=>//div[@class='modal-body']//div[@class='glo-field row'][%s]//label"
    def get_field_name(self,loc):
        return self.required_field_name %loc

    #required field message
    required_field_message ="xpath=>//div[contains(text(),'is required')]"


