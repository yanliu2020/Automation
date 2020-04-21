# coding = utf-8


class AnalysysCommonEntity(object):

    """分析图表切换日期"""
    # 点击展开日期控件
    cal = "xpath=>//div[1][@class='v-input v-input--prefix']/input[@class='v-input__inner v-input-default']"

    # 切换riq
    latest_7 = "xpath=>//div[@class='date-packer-daterange-body']/div/div/div[text()='近7日']"
    # 确认按钮
    confirm = "xpath=>//div[@class='date-packer-daterange-body']/div[2]/div[2]/button"

    """保存图表"""
    # 保存按钮
    saveBtn = "xpath=>//span[@class='save-text']"

    # 分析图表名称
    graph_name = "xpath=>//div[@class='addChartName ans-input ans-input--default']/input"

    # 添加到看板
    board_list = "xpath=>//div[@class='from-panels']/div[@class='list']/label/span" \
                 "/div[@class='reference v-poptip__reference']"

    # 添加到第1个看板
    board_list_name = "xpath=>//ul[@class='panel-ul scrollbar']/li/label[@class='text-overflow v-checkbox-wrapper']"

    # 确认按钮
    analysys_save_confirm = "xpath=>//div[@class='operation']/button[@class='ans-btn ans-btn-primary ans-btn-circle ans-btn-default']"

    # 保存断言
    save_assert = "xpath=>//div[@class='mod-name oper-name']/div[@action-type='titleRename']"

    """删除图表"""
    # 搜索图表
    search_chart = "xpath=>//div[@class='vi-category-search']/div[@class='box']/div[@class='ans-input ans-input--default']/input"

    analysys_list = "xpath=>//div[@class='list-table']/table/tbody/tr/td/div/a"

    analysys_del = "xpath=>//div[@class='list-table']/table/tbody/tr[%s]//i[@class='fz fz-lajitong']"

    def get_analysys_del(self, loc):
        return self.analysys_del % loc

    analysys_del_confirm = "xpath=>//body[@class='f-commom-body']/div[@class='ans-poptip panel-dog-modal panel-dog-modal-8 light'][1]/"\
                           "/div/button[@class='ans-btn ans-btn-primary ans-btn-circle ans-btn-default']/span"

    """添加对比人群"""

    # 对比分群-下拉菜单-可选分群列表
    contrast_cohorts_list = "xpath=>//div[@aria-hidden = 'false']/div[@class='v-select__inner']" \
                            "/ul[@class='v-select__scrollbar']/li[@class ='v-select__item']/a"

    # 对比分群-总数
    count_cohorts = "xpath=>//div[@class='item crowd-item']//span[@class='reference-btn']"

    # 增加对比分群
    contrast_cohorts = "xpath=>//div[@class='v-select__ref']/span[@class='reference-btn add-btn']"

    # 第n个对比分群（如果存在）
    user_cohorts = "xpath=>//div[@class='item crowd-item'][%s]/div/div[@class='v-select__ref']" \
                   "/span[@class='reference-btn']"

    def get_user_cohorts(self, loc):
        return self.user_cohorts % loc

    # 第n个分群-关闭按钮
    user_cohorts_delete = "xpath=>//div[@class='item crowd-item'][%s]" \
                          "/div[@class='v-select']//span[@class='reference-del fz fz-cha']"

    def get_user_cohorts_delete(self, loc):
        return self.user_cohorts_delete % loc

    """下载"""
    # 下载按钮
    down_btn = "xpath=>//div[@class='oper-box']/a/span[@class='down-text']"

    """详情页分享"""
    share_btn = "xpath=>//div[@class='oper-box']/a/span[@class='share-text']"
    # 确认分享
    confirm_share = "xpath=>//div[@class='v-share-modal']/div[@class='vsm-ft']/button/span[text()='确定']"

    """数据刷新按钮"""
    refresh_btn = "xpath=>//div[@class='sample clearfix']/a[@class='sample-refresh']"

    # 小舟正在拼命计算中
    loading = "xpath=>//div[@class='m-spin-box']//div[@class='v-spin-bd']/div[2]"

    """抽样"""
    # 全量按钮
    sample_btn = "xpath=>//div[@class='sample clearfix']//span[@class='sample-title']"

    # 抽样计算-减号
    sample_pre_btn = "xpath=>//div[@class='sample-slider']/button[@class='pre-btn']"

    # 抽样计算-加号
    sample_next_btn = "xpath=>//div[@class='sample-slider']/button[@class='next-btn']"

    """另存为"""
    # 另存为按钮
    saveAs_btn = "xpath=>//div[@class='oper-box']/a[2]/span[@class='saveAs-text']"
    confirm_saveAs = "xpath=>//div[@class='operation']/button[@class='ans-btn ans-btn-primary ans-btn-circle ans-btn-default']"

    # 提示消息
    tips_msg = "xpath=>//div[@class='ans-message-box-content-text']/span"

    # 实时分析、留存分析、智能路径 日期入口
    date_input = "xpath=>//span[@class='v-datepicker']/div/div/input"

    # 日期选择面板
    picker_date_panel = "xpath=>//div[@class='date-packer-opt']/div[%s]"

    def choice_date(self, index):
        return self.picker_date_panel % index

    # 分群下钻_目标人数
    retention_value = "xpath=>//div[@class='dirr-poptop']/div/span[@class='dirr-count']"

    # 查看分群概览
    seeUserList = "xpath=>//div[@class='dirr-poptop']/div[3]"

    # 保存用户分群
    saveUserList = "xpath=>//div[@class='dirr-poptop']/div[4]"

    # 保存名称输入
    save_input_name = "xpath=>//div[@class='v-modal-content-body']/ul[@class='dirll-save-crowd']/li/input"

    # 保存确认按钮
    save_confirm = "xpath=>//div[@class='modal-box-save-crowd']/div/button[2]"

    # 分群页面 用户数
    User_number = "xpath=>//div[@class='m-cohorts-user']/div[@class='th']/div[@class='number']/b"

    # 分群页面 返回分析
    cohort_to_analysys = "xpath=>//body[@id='app-body']//div[@class='title']/span/a"
