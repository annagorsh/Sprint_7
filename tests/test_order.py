from selenium.webdriver.firefox import webdriver
import links
from pages.order_page import *
from pages.tracking_page import *
from pages.receiver_form_page import *
from pages.rent_details_page import *

class TestOrder:
    driver = None

    @allure.title("Проверка создания заказа и перехода на главную по клику на 'Самокат' в логотипе")
    def test_click_scooter(self):
        self.driver = webdriver.Firefox()
        main = OrderPage(self.driver)
        main.navigate(links.MAIN_URL)
        main.cookie_close()
        main.go_to_order_top()
        receiver = ReceiverFormPage(self.driver)
        receiver.fill_in_receiver_form()
        rent = RentDetailsFormPage(self.driver)
        rent.fill_in_rent_form()
        track_page = TrackingPage(self.driver)
        order_created = track_page.wait_for_element_visible(TrackingPageLocators.cancel_button)
        assert order_created.is_displayed()
        track_page.scooter_click()
        expected_url = links.MAIN_URL
        assert self.driver.current_url == expected_url
        self.driver.quit()

    @allure.title("Проверка создания заказа и перехода на 'Дзен' по клику на 'Яндекс' в логотипе")
    def test_click_yandex(self):
        self.driver = webdriver.Firefox()
        main = OrderPage(self.driver)
        main.navigate(links.MAIN_URL)
        main.cookie_close()
        main.scroll_to_bottom()
        main.wait_for_element_visible(LandingPageLocators.bottom_order_button)
        main.go_to_order_bottom()
        receiver = ReceiverFormPage(self.driver)
        receiver.fill_in_receiver_form()
        rent = RentDetailsFormPage(self.driver)
        rent.fill_in_rent_form()
        track_page = TrackingPage(self.driver)
        order_created = track_page.wait_for_element_visible(TrackingPageLocators.cancel_button)
        assert order_created.is_displayed()
        track_page.yandex_click()
        track_page.switch_tab()
        track_page.wait_for_element_visible(MiscLocators.yandex_search_logo)
        expected_url = links.DZEN_URL
        assert self.driver.current_url == expected_url
        self.driver.quit()