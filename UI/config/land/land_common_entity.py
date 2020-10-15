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

    #input_special
    field_special ="xpath=>//div[@class='modal-body']//input[@name='%s']"
    def get_field_special_input(self,loc):
        return self.field_special %loc

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
    field_name = "xpath=>//div[@class='modal-body']//div//label"
    required_field_name = "xpath=>//div[@class='modal-body']//div[%s]//label"
    def get_field_name(self,loc):
        return self.required_field_name %loc

    #required field message
    required_field_message ="xpath=>//div[contains(text(),'is required')]"

    #fields_name
    fields_name ="xpath=>//div[@class='row form-group']/div[%s]//div[%s]/div/label"
    def get_fields_name(self,loc1,loc2):
        return self.fields_name %(loc1,loc2)

    #required_field_name
    required_name = "xpath=>//div[@class='row form-group']/div[%s]//div[%s]/div/label/span"
    def get_required_name(self,loc1,loc2):
        return self.required_name %(loc1,loc2)

    #fields_section
    field_section = "xpath=>//div[@class='row form-group']/div"

    #fields of section
    field_of_section ="xpath=>//div[@class='row form-group']/div[%s]//div/div/label"
    def get_fields_of_section(self,loc):
        return self.field_of_section %loc

