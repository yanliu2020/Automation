#-*- coding: UTF-8 -*-


class Event(object):
    # 事件分析按钮
    eventBtn = "xpath=>//div[@class='analysis-list']/div[1]/div[@class='bd']/a/span[text()='事件分析']"

    # 生成图表
    result_graph = "xpath=>//*[@id='Echarts']/div[1]/canvas"

    # 暂无数据
    null_graph = "xpath=>//div[@class='echartBody']//p[@class='tips']/span/span[text()='暂无数据']"

    # 校验
    asserted = "xpath=>//div[@id='eventSetTable']//div[@class='m-table-common table-fix-sticky']" \
               "/table[@class='m-table']/thead/tr[@class='m-thead']/th[@class='fix-col'][1]"

    # 表格第1行第1列合计
    total = "xpath=>//*[@id='eventSetTable']/div/div[2]/table/tbody/tr/td[3]"

    # 折线图按钮
    view_line = "xpath=>//div[@class='v-btn-group']/button[4]"

    # 柱状图按钮
    view_histogram = "xpath=>//div[@class='v-btn-group']/button[5]"

    # 面积按钮
    view_area = "xpath=>//div[@class='v-btn-group']/button[6]"

    # 表格按钮
    view_table = "xpath=>//div[@class='button-disabled v-btn-group']/button[@title='表格']"

    # 表格
    retention_table = "xpath=>//div[@class='m-table-common table-common-sticky']/table/thead/tr/th[1]"

    # 事件分析表格 合计
    table_lists = "xpath=>//div[@class='m-table-wrapper events-table']/" \
                  "div[@class='m-table-common table-common scrollbar scrollbar-show']/" \
                  "table[@class='m-table']/tbody[@class='m-tbody']/tr/td[3]"

    # 图表显示按钮列表
    graph_list = "xpath=>//div[contains(@class, 'v-btn-group')]/button[@class='v-btn']"

    # 勾选按钮
    selected = "xpath=>//span[@class='event-date-confirm']/label[@class='confirm-left ans-checkbox-wrapper']"

    # 切换至同比
    type_list = "xpath=>//span[@class='v-datepicker']//span[@class='event-date-confirm']" \
                "//button[@class='reference v-btn v-btn-text v-btn-small']"

    # 对比类型
    compare_type = "xpath=>//body/div[@class='v-popper v-select__menu']/div[@class='v-select__inner']" \
                   "/ul[@class='v-select__scrollbar']/li[@class='v-select__item'][%s]/a"

    def get_compare_type(self, loc):
        return self.compare_type % loc

    # 确认按钮
    confirm = "xpath=>//div[@class='date-packer-daterange-body']/div[@class='x-date-packer-confirm']/" \
              "div[@class='confirm-btn']/button"

    # 分析粒度下拉框
    analysys_type = "xpath=>//div[@class='box-title']/div/span[@class='tag-down-events analysys-type']/span"
    session_select = "xpath=>//a[@href='/analytics/event-segmentation/session']"

    # 切换至Session总用户数
    SessionPV = "xpath=>//div[@class='measure-line'][1]//span[@class='tag-down-events']" \
                "/span[@class='vi-btn-reference v-poptip__reference']"
    PV = "xpath=>//div[@x-placement='bottom-start']/div/ul/li/a[text()='Session总次数']"

    # 日期入口
    date_input = "xpath=>//div[@class='v-input v-input--prefix'][1]/"\
            "input[@class='v-input__inner v-input-default']"

