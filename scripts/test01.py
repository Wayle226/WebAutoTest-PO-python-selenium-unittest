import unittest
import settings
from page.driver_act import Driver


class TestLogin(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = Driver.get_page_driver_obj_and_maximize_window()

    @classmethod
    def tearDownClass(cls) -> None:
        Driver.quit()

    def test01(self):
        pass