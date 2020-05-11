# -*- coding: utf-8 -*-

class CustomerRecordEntity(object):
    #Actions和History
    customer_operate = "xpath=>//div[@class='btn-toolbar show']/button[text()='%s']"
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
    close_window = "xpath=>//button[@class='close']"
    #弹窗标题
    window_title = "xpath=>//h4[@class='modal-title']"
    #确认删除
    delete_confirm = "xpath=>//button[text()='Yes, delete it!']"
    #提示消息
    tips_msg = "xpath=>//div[@role='alert']"

    #email
    emailAddress = "id=>CreateContactEmail"
    emailType = "id=>CreateEmailType"
    isPrimary = "id=>CreateIsPrimary"

    #identifier
    identifierName = "id=>detailsIdentifierName"
    identifier = "id=>CreateIdentifier"


