# -*- coding: utf-8 -*-

class CustomerRecordEntity(object):
    #Actions和History
    customer_operate = "xpath=>//div[@class='btn-toolbar']/button[text()='%s']"
    def get_customer_operate(self,loc):
        return self.customer_operate %loc
    #Actions下拉点击
    action = "xpath=>//div[@class='btn-toolbar show']/ul//a[text()='%s']"
    def get_action(self,loc):
        return self.action %loc

    #record各页签
    record_tab = "xpath=>//div[@class='card']//li/a[text()='%s']"
    def get_record_tab(self,loc):
        return self.record_tab %loc

    #各页签下section
    section_list = "xpath=>//div[@class='card']//div//h4"
    #section名称
    section_name = "xpath=>//div[@class='card']//div//h4[text()='%s']"
    def get_section_name(self,loc):
        return self.section_name %loc

    #Entity和Contacts下section的操作按钮
    section_operator = "xpath=>//div[@class='glo-row']/div[%s]//button[text()=' %s']"
    def get_section_operator(self,loc1,loc2):
        return  self.section_operator %(loc1,loc2)

    #每个section下的记录数
    entity_records = "xpath=>//div[@class='glo-row']/div[%s]//div[@class='glo-row']//div[@class='rt-tr-group']"
    def get_entity_records(self,loc):
        return self.entity_records %loc

    #Entity和contacts下选中N行记录
    entity_record = "xpath=>//div[@class='glo-row']/div[%s]//div[@class='glo-row']//div[@class='rt-tr-group'][%s]/div"
    def get_entity_record(self,loc1,loc2):
        return  self.entity_record %(loc1,loc2)


    #Related Leases/Lands>>Lands,Mineral Leases，Surface Leases，Surface Projects
    related_section_list = "xpath=>//div[@class='reactTable-full']/div//h3"
    #Related Leases/Lands下的操作按钮
    related_section_operator = "xpath=>//div[@class='reactTable-full']/div[%s]//a[text()=' %s']"
    def get_related_operator(self,loc1,loc2):
        return  self.related_section_operator %(loc1,loc2)

    #每个section下的记录数
    related_records = "xpath=>//div[@class='reactTable-full']/div[%s]//div[@class='rt-tr-group']"
    def get_related_records(self,loc):
        return self.related_records %loc

    #Related Lease/Lands下选中N行记录
    related_record = "xpath=>//div[@class='reactTable-full']/div[%s]//div[@class='rt-tr-group'][%s]/div"
    def get_related_record(self,loc):
        return self.related_record %loc

    #DBA和Websites输入框
    input_info = "xpath=>//input[@name='%s']"
    def get_input_info(self,loc):
        return self.input_info %loc

    #点击保存
    save = "xpath=>//button[text()='Save']"
    #关闭弹窗
    contact_close = "xpath=>//button[@class='close']"
    #弹窗标题
    contact_title = "xpath=>//h4[@class='modal-title']"
    #确认删除
    delete_confirm = "xpath=>//button[text()='Yes, delete it!']"

    entity_title = "xpath=>//div[3]//h4[@class='modal-title']"
    entity_close = "xpath=>//div[3]//button[@class='close']"

    #提示消息
    tips_msg = "xpath=>//div[@role='alert']"
    required_msg = "xpath=>//div[@role='alert']/div[@class='summaryMessage']"
    #contact记录数
    contact_list_page = "xpath=>//span[@class='glo-table-pagination']"

    #contacts:salutation,firstName，middleName，lastName，
    contact_input = "xpath=>//input[@name='%s']"
    def get_contact_input(self,loc):
        return self.contact_input %loc
    #suffix, contactRole
    contact_select = "xpath=>//select[@name='%s']"
    def get_contact_select(self,loc):
        return self.contact_select %loc

    #email:emailAddress
    email_input = "xpath=>//input[@name='%s']"
    def get_email_input(self,loc):
        return self.email_input %loc
    #emailType, isPrimary
    email_select = "xpath=>//select[@name='%s']"
    def get_email_select(self,loc):
        return  self.email_select %loc

    #phone:countryCode,areaCode,phone,extension
    phone_input = "xpath=>//input[@name='%s']"
    def get_phone_input(self,loc):
        return self.phone_input %loc
    #phoneType
    phone_select = "xpath=>//select[@name='%s']"
    def get_phone_select(self,loc):
        return  self.phone_select %loc

    #identifier
    identifierName = "xpath=>//select[@name='name']"
    identifier = "xpath=>//input[@name='identifier']"
    select_tax = "xpath=>//select[@name='stateTaxID']"
    identifierNameList = "xpath=>//select[@name='name']/option"

    #address:attentionLine,address1,address2,city,postalCode
    address_input = "xpath=>//input[@name='%s']"
    def get_address_input(self,loc):
        return self.address_input %loc
    #addressType，stateCode，country
    address_select = "xpath=>//select[@name='%s']"
    def get_address_select(self,loc):
        return  self.address_select %loc

    #entityType, entityClass
    entity = "xpath=>//select[@name='%s']"
    def get_entity(self,loc):
        return self.entity %loc

    #firstName lastName fullName  defaultSort  organizationName,
    entity_edit_input = "xpath=>//input[@name='%s']"
    def get_edit_input(self,loc):
        return self.entity_edit_input %loc
    entity_edit_select = "xpath=>//select[@name='%s']"
    #salutation suffix subClassName stateOfIncorporation
    def get_edit_select(self,loc):
        return self.entity_edit_select %loc

    #history
    entity_history = "xpath=>//div[@class='modal-content']//span[@class='glo-table-pagination']"

    #判断已选择identifierName的类型
    identifierName_row = "xpath=>//div[@class='glo-row']/div[5]//div[@class='glo-row']//div[@class='rt-tr-group'][%s]/div/div"
    def get_identifier_name(self,loc):
        return self.identifierName_row %loc



