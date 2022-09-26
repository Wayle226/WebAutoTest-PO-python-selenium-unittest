# from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
import settings
import time


class Base:
    def __init__(self, driver):
        # self.driver = webdriver.Firefox()  # 方便后面的方法编写
        self.driver = driver

    # 查找元素
    def base_find_element(self, loc, timeout=settings.Setting.timeout, poll_frequency=settings.Setting.poll_frequency):
        # 显示等待的获取元素
        return WebDriverWait(self.driver, timeout=timeout, poll_frequency=poll_frequency).until(
            lambda x: x.find_element(*loc)
        )

    # 点击操作
    def base_click(self, loc):
        self.base_find_element(loc).click()

    # 输入操作
    def base_input(self, loc, input_content=None, keys=None):
        if None:
            el = self.base_find_element(loc)
            # 先清除内容
            el.clear()
            el.send_keys(input_content)
        # keys传列表或者元组：(Keys.A)或者[Keys.CONTROL, "v"]
        if keys:
            el.send_keys(*keys)

    # 截屏操作
    def base_screen_shorts(self):
        self.driver.get_screenshot_as_file(f"../screenshorts/{time.time()}.png")

    # 获取文本
    def base_get_text(self, loc):
        return self.base_find_element(loc).text

    # 鼠标双击
    def base_double_click(self, loc):
        ActionChains(self.driver).double_click(self.base_find_element(loc)).perform()

    # 鼠标右键
    def base_context_click(self, loc):
        ActionChains(self.driver).context_click(self.base_find_element(loc)).perform()

    # 鼠标拖动
    def base_drag_and_drop(self, source_loc, target_loc):
        ActionChains(self.driver).drag_and_drop(
            self.base_find_element(source_loc), self.base_find_element(target_loc)).perform()

    # 鼠标悬停
    def base_move_to_element(self, loc):
        ActionChains(self.driver).move_to_element(self.base_find_element(loc)).perform()

    # 判断页面是否存在元素
    def base_if_exist(self, loc):
        try:
            self.driver.find_element(loc, timeout=2)
            return True

        except:
            return False
