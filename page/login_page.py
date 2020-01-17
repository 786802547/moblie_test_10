import page
from base.base_page import BasePage


class LoginPage(BasePage):
    phone_num = page.phone_num
    pwd = page.pwd
    login_btn = page.login_btn
    alect_btn = page.alect_btn

    def input_phone_num(self, num):
        self.input_func(self.phone_num, num)
        # 输入手机号方法

    def input_pwd(self, pwd):
        self.input_func(self.pwd, pwd)
        # 输入密码方法

    def click_login_btn(self):
        self.click_func(self.login_btn)
        # 点击登录方法

    def click_alect_btn(self):
        self.click_func(self.alect_btn)
        # 点击确认按钮方法
