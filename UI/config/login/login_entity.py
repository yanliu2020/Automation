#-*- coding: UTF-8 -*-


class LoginEntity(object):
    # 用户名
    username = "id=>logonIdentifier"
    # 密码
    password = "id=>password"
    # 登录按钮
    login_btn = "xpath=>//div[@class='buttons']/button[text()='Sign in']"
    # 登录标题
    login_title = "xpath=>//div[@class='localAccount']//div[@class='intro']/h2"

    # 用户头像
    user_logo = "xpath=>//div[@class='header-badge-glo']"

    # 退出登录
    logout_user = "xpath=>//a[text()='Logout']"
