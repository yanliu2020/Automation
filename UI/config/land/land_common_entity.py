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

    #save/cancel
    button = "xpath=>//button[text()='%s']"
    def get_land_button(self,loc):
        return self.button %loc

    #Date Picker
    Date_list = "xpath=>//div[@class='react-datepicker__month']/div/div"
    Selected_Date = "xpath=>//div[@class='react-datepicker__month']/div/div[@tabindex='0']"