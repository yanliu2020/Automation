# -*- coding: utf-8 -*-

class HomePageEntity(object):

    # 欢迎语
    default_text = "xpath=>//div[@id='root']//div[@class='content-heading']"

    #module_list
    module_list="xpath=>//div[@class='card']/form//div[@id='homeGrid']/div//h2"

    #module_operator
    module_operator="xpath=>//div[@class='card']/form//div[@id='homeGrid']/div[%s]/div[2]//a[text()='%s']"
    def get_module_operator(self,loc,name):
        return self.module_operator %(loc,name)


