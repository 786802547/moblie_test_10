import page
from base.base_page import BasePage


class IndexPage(BasePage):
    mine = page.mine
    def clicl_mine(self):
        self.click_func(self.mine)