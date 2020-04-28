# -*- coding: utf-8 -*-

class SearchCustomerEntity(object):
    #搜索页面
    assert_title = "xpath=>//div[@class='content-container']/h1"

    #top button
    top_button = "xpath=>//div[@class='col-md-12']/button[text()='%s']"
    def get_top_button(self,loc):
        return self.top_button %loc

    #save search
    #save search as
    #Show Saved Searches
    #left entity file
    entity_filter = "id=>filter"
