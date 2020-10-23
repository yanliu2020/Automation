#-*- coding: UTF-8 -*-

from pageobjects.homepage.homePage import HomePage
from utils.logger import logger
from utils.base_page import BasePage
from config.login.login_entity import LoginEntity

class SystemLogin(BasePage):
    #判断登录页面
    def is_login_page(self):
        text = self.find_element(LoginEntity.login_title).text
        if text == 'Sign in with your existing account':
            return True
        return False

     #登录操作
    def user_login(self, username, password):
        if not self.is_login_page():
            logger.error('not in login page')
        self.ctrl_all(LoginEntity.username)
        self.type(LoginEntity.username, username)
        self.ctrl_all(LoginEntity.password)
        self.type(LoginEntity.password, password)
        self.find_element(LoginEntity.login_btn).click()
        if HomePage(self.driver).is_visibility_homepage() == True:
            logger.info('login success')
        else:
            logger.error('login fail')

    def logout(self):
        """
        # 退出账号
        :return:
        """
        self.find_element_by_wait('xpath',LoginEntity.user_logo)
        self.click(LoginEntity.user_logo)
        self.click(LoginEntity.logout_user)
        if SystemLogin(self.driver).is_login_page():
            logger.info('logout success')
            return True
        else:
            logger.error('logout fail')
            return False

    def switch_account(self,username,password):
        self.logout()
        self.find_element_by_wait('xpath', LoginEntity.login_title)
        self.user_login(username, password)



