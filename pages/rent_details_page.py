from pages.base_page import *
from selenium.webdriver.common.keys import Keys

class RentDetailsFormPage(BasePage):

    @allure.step("Инициализируем браузер")
    def __init__(self, driver):
        super().__init__(driver)

    @allure.step("Ждём, пока нужный заголовок станет видимым")
    def wait_until_rent_form_visible(self):
        self.wait_for_element_visible(RentDetailsLocators.rent_header)

    @allure.step("Заполняем дату")
    def fill_in_date(self):
        self.enter_text(RentDetailsLocators.date_field, "31.12.2024")


    @allure.step("Прожимаем Enter после ввода даты")
    def press_enter_date(self):
        self.enter_text(RentDetailsLocators.date_field, Keys.ENTER)

    @allure.step("Выбираем длительность аренды")
    def pick_duration(self):
        self.click_element(RentDetailsLocators.rent_time_field)
        self.wait_for_element_visible(RentDetailsLocators.rent_picker)
        self.click_element(RentDetailsLocators.rent_picker)

    @allure.step("Выбираем чёрный цвет самоката")
    def pick_colour_black(self):
        self.click_element(RentDetailsLocators.scooter_colour_black)

    @allure.step("Выбираем серый цвет самоката")
    def pick_colour_grey(self):
        self.click_element(RentDetailsLocators.scooter_colour_grey)

    @allure.step("Нажимаем 'Заказать'")
    def click_order_at_rent_details(self):
        self.click_element(RentDetailsLocators.order_button)

    @allure.step("Ждём появления всплывающего окна 'Хотите оформить заказ?'")
    def wait_for_popup1(self):
        self.wait_for_element_visible(OrderPopupLocators.order_confirm_header)

    @allure.step("Нажимаем 'Да' во всплывающем окне")
    def click_yes(self):
        self.click_element(OrderPopupLocators.order_confirm_yes_button)

    @allure.step("Ждём появления всплывающего окна с номером заказа")
    def wait_for_popup2(self):
        self.wait_for_element_visible(OrderPopupLocators.order_created_header)

    @allure.step("Кликаем на 'Посмотреть статус' для перехода к странице статуса заказа")
    def click_to_see_order_page(self):
        self.click_element(OrderPopupLocators.go_to_order_button)

    @allure.step("Заполняем форму 'Про аренду'")
    def fill_in_rent_form(self):
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