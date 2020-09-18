# -*- coding: utf-8 -*-

class NewCustomerEntity(object):
    #搜索页面
    assert_title = "xpath=>//div[@class='content-container']/h1"

    #判断new customer页面
    default_text = "xpath=>//div[@id='root']//div[contains(text(),'New Business Entity')]"

    # input fields
    field_input = "xpath=>//input[@name='%s']"
    def get_field_input(self, loc):
        return self.field_input % loc

    # select fields
    field_select = "xpath=>//select[@name='%s']"
    def get_field_select(self, loc):
        return self.field_select % loc

    #section列表
    section_list = "xpath=>//div[@class='card']//div//h4"
    #section名称
    section_name = "xpath=>//div[@class='card']//div//h4[text()='%s']"
    def get_section_name(self,loc):
        return self.section_name %loc

    # 增加移除按钮
    add_remove = "xpath=>//p[text()='%s']"
    def get_add_remove(self, loc1):
        return self.add_remove % (loc1)

    #增加删除phone
    add_phone = "xpath=>//div[@class='col-md-8']/div[%s]//p[text()='%s']"
    def get_add_phone(self,loc1,loc2):
        return self.add_phone %(loc1,loc2)

    #save
    save = "xpath=>//button[text()='Save']"

    #Contact：1和3 ，name：salutation和suffix
    contact_select = "xpath=>//form[@class='ie-fix-flex']/div[2]//div[@class='col-md-8']/div[%s]//select[@name='%s']"
    def get_contact_select(self,loc1,loc2):
        return self.contact_select %(loc1,loc2)

    # Contact：1和3 ，name：firstName,middleName,lastName
    contact_input = "xpath=>//form[@class='ie-fix-flex']/div[2]//div[@class='col-md-8']/div[%s]//input[@name='%s']"
    def get_contact_input(self,loc1,loc2):
        return self.contact_input %(loc1,loc2)

    #Contact role:1和3
    role = "xpath=>//div[@class='col-md-8']/div[%s]//select[@name='contactRole']"
    def get_contact_role(self,loc):
        return self.role %loc

    #email type 1,3
    email_type = "xpath=>//div[@class='col-md-8']/div[%s]//select[@name='emailType']"
    def get_email_type(self,loc):
        return self.email_type %loc
    #email 1,3
    email = "xpath=>//div[@class='col-md-8']/div[%s]//input[@name='emailAddress']"
    def get_email(self,loc):
        return self.email %loc

    #contact 1,3和 phone 1,3,5 和 countryCode，areaCode，phone，ext
    phone_input = "xpath=>//div[@class='col-md-8']/div[%s]//div[@class='card-body bg-light']/div[%s]//input[@name='%s']"
    def get_phone_input(self,loc1,loc2,loc3):
        return self.phone_input %(loc1,loc2,loc3)

    #contact 1,3和 phone 1,3,5
    phone_type = "xpath=>//div[@class='col-md-8']/div[%s]//div[@class='card-body bg-light']/div[%s]//select[@name='phoneType']"
    def get_phone_type(self,loc1,loc2):
        return self.phone_type %(loc1,loc2)

    #Contact 1 Same as Above
    same_as = "id=>sameAs"

    #提示消息
    msg_list = "xpath=>//div[@role='alert']/div[@class='summaryMessage']"






