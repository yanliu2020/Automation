# -*- coding: utf-8 -*-
class LandDetailsEntity(object):
    # land detail page
    default_text = "xpath=>//div[@id='root']//div[contains(text(),'Land Details ')]"

    # Actions栏buttons
    land_operate = "xpath=>//div[@class='btn-toolbar']/button[text()='%s']"
    def get_land_operate(self, loc):
        return self.land_operate % loc

    # Actions下拉点击
    action = "xpath=>//div[@class='btn-toolbar show']/ul//a[text()='%s']"
    def get_action(self, loc):
        return self.action % loc

    # details page各页签
    record_tab = "xpath=>//div[@class='card']//li/a[text()='%s']"
    def get_record_tab(self, loc):
        return self.record_tab % loc

    # 各页签下section
    section_list = "xpath=>//div[@class='card']//div//h4"

    # section名称
    section_name = "xpath=>//div[@class='card']//div//h4[text()='%s']"
    def get_section_name(self, loc):
        return self.section_name % loc

    # Summay/Utilization/Comment/Related Leases/Related Land/Appraisal/Sale/Acquisition/Cutomers的操作按钮
    section_operator = "xpath=>//div[@class='glo-row']/div[%s]//button[text()=' %s']"
    def get_section_operator(self, loc1, loc2):
        return self.section_operator % (loc1, loc2)

     # Location的操作按钮
    location_operator = "xpath=>//div[@role='tabpanel']/div/div[%s]//button[text()=' %s']"
    def get_location_operator(self, loc1, loc2):
        return self.location_operator % (loc1, loc2)

    # 每个section下的记录数
    section_records = "xpath=>//div[@role='tabpanel']/div[%s]//div[@class='glo-row']//div[@class='rt-tr-group']"
    def get_section_records(self, loc):
        return self.section_records % loc

    # section下选中N行记录
    select_record = "xpath=>//div[@role='tabpanel']/div[%s]//div[@class='glo-row']//div[@class='rt-tr-group'][%s]/div"
    def get_select_record(self, loc1, loc2):
        return self.select_record % (loc1, loc2)

    #提示消息
    tips_msg = "xpath=>//div[@role='alert']"
    # 确认删除
    delete_confirm = "xpath=>//button[text()='Yes, delete it!']"