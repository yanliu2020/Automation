# -*- coding: utf-8 -*-

class NewCustomerEntity(object):
    #搜索页面
    assert_title = "xpath=>//div[@class='content-container']/h1"

    #click entity type
    entity_type = "xpath=>//select[@name='entityType']"
    #Entity class
    entity_class = "xpath=>//select[@name='entityClass']"

    #section列表
    section_list = "xpath=>//div[@class='card']//div//h4"
    #section名称
    section_name = "xpath=>//div[@class='card']//div//h4[text()='%s']"
    def get_section_name(self,loc):
        return self.section_name %loc

    #Salutation
    salutation = "xpath=>//form[@class='ie-fix-flex']/div[%s]//select[@name='salutation']"
    def get_salutation(self,loc):
        return self.salutation %loc
    #FirstName
    firstName = "xpath=>//form[@class='ie-fix-flex']/div[%s]//input[@name='firstName']"
    def get_firstName(self,loc):
        return self.firstName %loc
    #MiddleName
    middleName = "xpath=>//form[@class='ie-fix-flex']/div[%s]//input[@name='middleName']"
    def get_middleName(self,loc):
        return self.middleName %loc
    #LastName
    lastName = "xpath=>//form[@class='ie-fix-flex']/div[%s]//input[@name='lastName']"
    def get_lastName(self,loc):
        return self.lastName %loc
    #Suffix
    suffix = "xpath=>//form[@class='ie-fix-flex']/div[%s]//select[@name='suffix']"
    def get_suffix(self, loc):
        return self.suffix %loc

    # FullName
    fullName = "xpath=>//form[@class='ie-fix-flex']/div[1]//input[@name='fullName']"
    #Default Sort
    default_sort = "xpath=>//form[@class='ie-fix-flex']/div[1]//input[@name='defaultSort']"
    #organizationName
    organizationName = "xpath=>//form[@class='ie-fix-flex']/div[1]//input[@name='organizationName']"
    #type of business
    typeOfBusiness = "xpath=>//form[@class='ie-fix-flex']/div[1]//select[@name='typeOfBusiness']"
    #stateOfIncorporation
    stateOfIncorporation = "xpath=>//form[@class='ie-fix-flex']/div[1]//select[@name='stateOfIncorporation']"

    #Address & Identifier 按钮
    add_remove = "xpath=>//p[text()='%s']"
    def get_add_remove(self,loc):
        return self.add_remove %loc

    #save
    save = "xpath=>//button[text()='Save']"



