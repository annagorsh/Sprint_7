from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import *
import allure
from selenium.webdriver.common.keys import Keys
from random import randint

driver = webdriver.Firefox()

#элементы страницы
class OrderPage:
    #Форма "Для кого самокат"
    def __init__(self, driver):
        self.driver = driver

    def find_element(self, locator):
        self.driver.find_element(locator)

    @allure.step("Нажимаем на 'Заказать' на главной вверху страницы")
    def go_to_order_top(self):
        self.driver.find_element(*LandingPageLocators.top_order_button).click()

    @allure.step("Прокручиваем до кнопки 'Заказать' внизу страницы")
    def scroll_to_bottom(self):
        element = self.driver.find_element(*LandingPageLocators.bottom_order_button)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    @allure.step("Нажимаем на 'Заказать' на главной вверху страницы")
    def go_to_order_bottom(self):
        self.driver.find_element(*LandingPageLocators.bottom_order_button).click()

    @allure.step("Ждём, пока нужный заголовок станет видимым")
    def wait_until_receiver_form_visible(self):
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(ReceiverFormLocators.receiver_header))

    @allure.step("Заполняем поле 'Имя'")
    def fill_in_name(self):
        self.driver.find_element(*ReceiverFormLocators.name_field).send_keys("Юнги")

    @allure.step("Заполняем поле 'Фамилия'")
    def fill_in_surname(self):
        self.driver.find_element(*ReceiverFormLocators.surname_field).send_keys("Мин")

    @allure.step("Заполняем поле 'Адрес'")
    def fill_in_address(self):
        self.driver.find_element(*ReceiverFormLocators.address_field).send_keys("Бойцовая улица, 24с1")

    @allure.step("Выбираем станцию метро")
    def click_metro_station(self):
        self.driver.find_element(*ReceiverFormLocators.metro_station_field).click()
        self.driver.find_element(*ReceiverFormLocators.metro_station_button).click()

    @allure.step("Вводим номер телефона")
    def fill_in_phone_number(self):
        self.driver.find_element(*ReceiverFormLocators.phone_field).send_keys("+79999999999")

    @allure.step("Кликаем на 'Далее'")
    def click_continue(self):
        self.driver.find_element(*ReceiverFormLocators.continue_button).click()

    #Форма "Про аренду"
    @allure.step("Ждём, пока нужный заголовок станет видимым")
    def wait_until_rent_form_visible(self):
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(RentDetailsLocators.rent_header))

    @allure.step("Заполняем дату")
    def fill_in_date(self):
        self.driver.find_element(*RentDetailsLocators.date_field).send_keys("31.12.2024")

    def press_enter_date(self):
        self.driver.find_element(*RentDetailsLocators.date_field).send_keys(Keys.ENTER)

    @allure.step("Выбираем длительность аренды")
    def pick_duration(self):
        self.driver.find_element(*RentDetailsLocators.rent_time_field).click()
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(RentDetailsLocators.rent_picker))
        self.driver.find_element(*RentDetailsLocators.rent_picker).click()

    @allure.step("Выбираем чёрный цвет самоката")
    def pick_colour_black(self):
        self.driver.find_element(*RentDetailsLocators.scooter_colour_black).click()

    @allure.step("Выбираем серый цвет самоката")
    def pick_colour_grey(self):
        self.driver.find_element(*RentDetailsLocators.scooter_colour_grey).click()

    @allure.step("Нажимаем 'Заказать'")
    def click_order_at_rent_details(self):
        self.driver.find_element(*RentDetailsLocators.order_button).click()

    @allure.step("Ждём появления всплывающего окна 'Хотите оформить заказ?'")
    def wait_for_popup1(self):
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(OrderPopupLocators.order_confirm_header))

    @allure.step("Нажимаем 'Да' во всплывающем окне")
    def click_yes(self):
        self.driver.find_element(*OrderPopupLocators.order_confirm_yes_button).click()

    @allure.step("Ждём появления всплывающего окна с номером заказа")
    def wait_for_popup2(self):
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(OrderPopupLocators.order_created_header))

    @allure.step("Кликаем на 'Посмотреть статус' для перехода к странице статуса заказа")
    def click_to_see_order_page(self):
        self.driver.find_element(*OrderPopupLocators.go_to_order_button).click()

    @allure.step("Соглашаемся с куками, чтобы они не перекрывали элемент")
    def cookie_close(self):
        self.driver.find_element(*ReceiverFormLocators.cookie_button).click()

    @allure.step("Оформление заказа и переход на страницу трекинга")
    def order_flow(self):
        self.wait_until_receiver_form_visible()
        self.fill_in_name()
        self.fill_in_surname()
        self.fill_in_address()
        self.click_metro_station()
        self.fill_in_phone_number()
        self.click_continue()
        self.wait_until_rent_form_visible()
        self.fill_in_date()
        self.press_enter_date()
        self.pick_duration()
        self.pick_colour_black()
        self.click_order_at_rent_details()
        self.wait_for_popup1()
        self.click_yes()
        self.wait_for_popup2()
        self.click_to_see_order_page()

    @allure.step("Кликаем по слову 'Самокат' в лого в шапке сайта")
    def click_scooter(self):
        self.driver.find_element(*TrackingPageLocators.scooter_logo).click()

    @allure.step("Кликаем по слову 'Яндекс' в логотипе")
    def click_yandex(self):
        self.driver.find_element(*TrackingPageLocators.ya_logo).click()

