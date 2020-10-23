# -*- coding: utf-8 -*-
class LandCommonEntity(object):
    # detail page
    default_text = "xpath=>//div[@id='root']//div[contains(text(),'%s')]"
    def get_default_text(self,loc):
        return self.default_text %loc

    #top operate buttons
    top_operate = "xpath=>//div[@role='toolbar']/button[text()='%s']"
    def get_top_operate(self,loc):
        return self.top_operate %loc

    #Actions dropdown items
    actions = "xpath=>//div[@role='toolbar']/ul//a[text()='%s']"
    def get_actions(self,loc):
        return self.actions %loc

    # details page>>Tabs
    record_tab = "xpath=>//div[@class='card']//li/a[text()='%s']"
    def get_record_tab(self, loc):
        return self.record_tab % loc

    # details page>>Tabs>>Section items
    section_list = "xpath=>//div[@class='card']//div//h4"

    # details page>>Tabs>>Specific Section Name
    section_name = "xpath=>//div[@class='card']//div//h4[text()='%s']"
    def get_section_name(self, loc):
        return self.section_name % loc

    # details page>>Tabs>>Section>>list buttons
    section_operator = "xpath=>//div[@role='tabpanel']/div[%s]//button[text()=' %s']"
    def get_section_operator(self, loc1, loc2):
        return self.section_operator % (loc1, loc2)

     # details page>>Tabs>>Section>> special list buttons
    specail_operator = "xpath=>//div[@role='tabpanel']/div/div[%s]//button[text()=' %s']"
    def get_specail_operator(self, loc1, loc2):
        return self.specail_operator % (loc1, loc2)

    # get_section_rows
    section_records = "xpath=>//div[@role='tabpanel']/div[%s]//div[@class='glo-row']//div[@class='rt-tr-group']"
    def get_section_records(self, loc):
        return self.section_records % loc

    # get_select_row
    select_record = "xpath=>//div[@role='tabpanel']/div[%s]//div[@class='glo-row']//div[@class='rt-tr-group'][%s]/div"
    def get_select_record(self, loc1, loc2):
        return self.select_record % (loc1, loc2)

    #detail dialog>> fields value
    input_value = "xpath=>//div[@class='row form-group']//input"
    textarea_value = "xpath=>//div[@class='row form-group']//textarea"

    #table>>fields
    select_column_value = "xpath=>//div[@role='tabpanel']/div[%s]//div[@class='glo-row']//div[@class='rt-tr-group'][%s]/div/div"
    def get_column_value(self, loc1, loc2):
        return self.select_column_value % (loc1, loc2)

    #history dialog>>fields value
    select_history_value= "xpath=>//div[@class='modal-body']//div[@class='rt-tr-group'][%s]/div/div"
    def get_history_value(self,loc):
        return self.select_history_value %loc

    # special_section_list
    special_section_list = "xpath=>//div[@role='tabpanel']/div[@class='glo-row']//span"

    # fields value on section
    section_values = "xpath=>//div[@role='tabpanel']/div/div[%s]//div[@class='glo-field row']//input"
    def get_section_value(self, loc):
        return self.section_values % loc

    # input fields
    field_input = "xpath=>//div[@class='row form-group']//input[@name='%s']"
    def get_field_input(self,loc):
        return self.field_input %loc

    #textarea fields
    field_textarea = "xpath=>//div[@class='row form-group']//textarea[@name='%s']"
    def get_field_textarea(self,loc):
        return self.field_textarea %loc

    # select fields
    field_select = "xpath=>//select[@name='%s']"
    def get_field_select(self,loc):
        return self.field_select %loc

    #input_special
    input_special ="xpath=>//div[@class='modal-body']//input[@name='%s']"
    def get_input_special(self,loc):
        return self.input_special %loc

    #textarea specail
    textarea_specail = "xpath=>//div[@class='modal-body']//textarea[@name='%s']"
    def get_textarea_specail(self,loc):
        return self.textarea_specail %loc

    #Date Picker
    Date_list = "xpath=>//div[@class='react-datepicker__month']/div/div"
    Selected_Date = "xpath=>//div[@class='react-datepicker__month']/div/div[@tabindex='0']"

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

    #提示消息
    tips_msg = "xpath=>//div[@role='alert']"
    # 确认删除
    delete_confirm = "xpath=>//button[text()='Yes, delete it!']"
    # 关闭弹窗
    close = "xpath=>//button[@class='close']"
    #save/cancel
    button = "xpath=>//button[text()='%s']"
    def get_land_button(self,loc):
        return self.button %loc

