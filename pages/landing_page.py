from selenium import webdriver
from locators import LandingPageLocators
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure

driver = webdriver.Firefox()

class LandingPageScooter():

    def __init__(self, driver):
        self.driver = driver

    def find_element(self, locator):
        self.driver.find_element(locator)

    #Скролл до аккордеона
    @allure.step("Скроллим до нужного элемента")
    def scroll_to_accordeon(self):
        element = self.driver.find_element(*LandingPageLocators.accordeon_1)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    @allure.step("Кликаем на нужный элемент")
    def click_accordeon_1(self):
        self.driver.find_element(*LandingPageLocators.accordeon_1).click()

    @allure.step("Кликаем на нужный элемент")
    def click_accordeon_2(self):
        self.driver.find_element(*LandingPageLocators.accordeon_2).click()

    @allure.step("Кликаем на нужный элемент")
    def click_accordeon_3(self):
        self.driver.find_element(*LandingPageLocators.accordeon_3).click()

    @allure.step("Кликаем на нужный элемент")
    def click_accordeon_4(self):
        self.driver.find_element(*LandingPageLocators.accordeon_4).click()

    @allure.step("Кликаем на нужный элемент")
    def click_accordeon_5(self):
        self.driver.find_element(*LandingPageLocators.accordeon_5).click()

    @allure.step("Кликаем на нужный элемент")
    def click_accordeon_6(self):
        self.driver.find_element(*LandingPageLocators.accordeon_6).click()

    @allure.step("Кликаем на нужный элемент")
    def click_accordeon_7(self):
        self.driver.find_element(*LandingPageLocators.accordeon_7).click()

    @allure.step("Кликаем на нужный элемент")
    def click_accordeon_8(self):
        self.driver.find_element(*LandingPageLocators.accordeon_8).click()


    #Ожидание видимости элементов
    @allure.step("Ждём, пока элемент станет видимым")
    def wait_until_answer_visible_1(self):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(LandingPageLocators.accordeon_text_1))

    @allure.step("Ждём, пока элемент станет видимым")
    def wait_until_answer_visible_2(self):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(LandingPageLocators.accordeon_text_2))

    @allure.step("Ждём, пока элемент станет видимым")
    def wait_until_answer_visible_3(self):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(LandingPageLocators.accordeon_text_3))

    @allure.step("Ждём, пока элемент станет видимым")
    def wait_until_answer_visible_4(self):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(LandingPageLocators.accordeon_text_4))

    @allure.step("Ждём, пока элемент станет видимым")
    def wait_until_answer_visible_5(self):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(LandingPageLocators.accordeon_text_5))

    @allure.step("Ждём, пока элемент станет видимым")
    def wait_until_answer_visible_6(self):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(LandingPageLocators.accordeon_text_6))

    @allure.step("Ждём, пока элемент станет видимым")
    def wait_until_answer_visible_7(self):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(LandingPageLocators.accordeon_text_7))

    @allure.step("Ждём, пока элемент станет видимым")
    def wait_until_answer_visible_8(self):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(LandingPageLocators.accordeon_text_8))