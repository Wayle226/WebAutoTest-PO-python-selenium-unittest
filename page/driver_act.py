from selenium import webdriver

import settings


class Driver:
    driver = None

    @classmethod
    def get_page_driver_obj_and_maximize_window(cls):
        if not cls.driver:
            cls.driver = webdriver.Firefox()
            # cls.driver = webdriver.Chrome()
            cls.driver.maximize_window()
            cls.driver.get(settings.Setting.url)
        return cls.driver

    @classmethod
    def quit(cls):
        if cls.driver:
            cls.driver.quit()
            # 需要给self.driver赋值为None，因为quit操作后 driver值还存在
            cls.driver = None



