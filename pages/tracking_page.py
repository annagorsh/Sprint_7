from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import *
import allure

class TrackingPage:
    def __init__(self, driver):
        self.driver = driver

    def find_element(self, locator):
        self.driver.find_element(locator)

    @allure.step("Проверяем, что мы на странице с трекингом заказа")
    def wait_for_tracking_page(self):
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(TrackingPageLocators.cancel_button))

    @allure.step("Кликаем по слову 'Яндекс' в логотипе")
    def yandex_click(self):
        self.driver.find_element(*TrackingPageLocators.ya_logo).click()

    @allure.step("Кликаем по слову 'Самокат' в логотипе")
    def scooter_click(self):
        self.driver.find_element(*TrackingPageLocators.scooter_logo).click()

