# -*- coding: utf-8 -*-

class HomePageEntity(object):
    # 欢迎语
    default_text = "xpath=>//div[@id='root']//div[@class='content-heading']"

    #module_list
    module_list="xpath=>//div[@class='card']/form//div[@id='homeGrid']/div//h2"

    #module_operator
    module_operator="xpath=>//div[@class='card']/form//div[@id='homeGrid']/div[%s]/div[2]//a[text()=' %s']"
    def get_module_operator(self,loc,name):
        return self.module_operator %(loc,name)

    #quick search
    quick_search = "xpath=>//div[@class='card']/form//div[@id='homeGrid']/div[%s]//input"
    def get_quick_search(self,loc):
        return self.quick_search %loc

    #quick_select
    quick_select = "xpath=>//div[@class='card']/form//div[@id='homeGrid']/div[%s]//select"
    def get_quick_select(self,loc):
        return self.quick_select %loc
    #quick_select_go
    quick_select_go = "xpath=>//div[@class='card']/form//div[@id='homeGrid']/div[%s]/div/div/button"
    def get_quick_select_go(self,loc):
        return self.quick_select_go %loc

    #quick_search_go
    quick_go = "xpath=>//div[@class='card']/form//div[@id='homeGrid']/div[%s]/div/button"
    def get_quick_search_go(self,loc):
        return self.quick_go %(loc)
