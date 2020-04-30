#-*- coding: UTF-8 -*-

from pageobjects.homepage.homePage import HomePage
from utils.logger import logger
from utils.base_page import BasePage
from config.login.login_entity import LoginEntity

class SystemLogin(BasePage):

    # 输入用户名
    def input_username(self, text):
        self.clear(LoginEntity.username)
        self.type(LoginEntity.username, text)

    # 输入用户密码
    def input_password(self, text):
        self.clear(LoginEntity.password)
        self.type(LoginEntity.password, text)

    # 点击登录按钮
    def click_login(self):
        self.find_element(LoginEntity.login_btn).click()

    #判断登录页面
    def is_login_page(self):
        text = self.find_element(LoginEntity.login_title).text
        if text == 'Sign in with your existing account':
            return True
            print("return true")
        return False

     #登录操作
    def user_login(self, username, password):
        if not self.is_login_page():
            logger.error('not in login page')
            raise NameError('not in login page')
        self.input_username(username)
        self.input_password(password)
        self.click_login()
        if HomePage(self.driver).is_visibility_homepage():
            logger.info('login success')
            return True
        else:
            logger.error('login fail')
            return False


