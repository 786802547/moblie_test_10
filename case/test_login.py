import time

import pytest

from page.page_factory import PageFactory
from utils import init_driver


class TestLogin(object):
    @pytest.fixture(autouse=True)
    def before_func(self):
        self.driver = init_driver()
        self.page_factory = PageFactory(self.driver)
        yield
        time.sleep(1)
        self.driver.quit()
    def test_login(self):
        self.page_factory.index_page().clicl_mine()
        self.page_factory.mine_page().click_login_reg()
        self.page_factory.login_page().input_phone_num(12345678901)
        self.page_factory.login_page().input_pwd(123456)
        self.page_factory.login_page().click_login_btn()
        # self.page_factory.login_page().click_alect_btn()