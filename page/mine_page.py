import page
from base.base_page import BasePage


class MinePage(BasePage):
    login_reg = page.login_reg
    def click_login_reg(self):
        self.click_func(self.login_reg)
        # 点击登录注册方法