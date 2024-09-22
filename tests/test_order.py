import links
from pages.order_page import *
from pages.tracking_page import *
import time

class TestOrder:
    driver = None

    @classmethod
    def setup_class(cls):
        cls.driver = webdriver.Firefox()

    @allure.title("Проверка создания заказа и перехода на главную по клику на 'Самокат' в логотипе")
    def test_click_scooter(self):
        self.driver.get(links.MAIN_URL)
        main = OrderPage(self.driver)
        main.cookie_close()
        main.go_to_order_top()
        main.order_flow()
        main.click_scooter()
        expected_url = links.MAIN_URL
        assert self.driver.current_url == expected_url

    @allure.title("Проверка создания заказа и перехода на 'Дзен' по клику на 'Яндекс' в логотипе")
    def test_click_yandex(self):
        self.driver.get(links.MAIN_URL)
        main = OrderPage(self.driver)
        main.scroll_to_bottom()
        time.sleep(3)
        main.go_to_order_bottom()
        main.order_flow()
        time.sleep(3)
        main.click_yandex()
        tabs = main.driver.window_handles
        main.driver.switch_to.window(tabs[1])
        time.sleep(5)
        expected_url = links.DZEN_URL
        assert self.driver.current_url == expected_url

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()