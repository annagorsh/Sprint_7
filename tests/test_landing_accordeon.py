import allure
import links
from pages.landing_page import *
import time

class TestLandingAccordeon:
    driver = None

    @classmethod
    def setup_class(cls):
        cls.driver = webdriver.Firefox()

    @allure.title("Проверяем 1 раскрывашку в аккордеоне на главной странице Яндекс Самоката")
    def test_1(self):
        self.driver.get(links.MAIN_URL)
        main_page = LandingPageScooter(self.driver)
        main_page.scroll_to_accordeon()
        time.sleep(2)
        main_page.click_accordeon_1()
        main_page.wait_until_answer_visible_1()
        result = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(LandingPageLocators.accordeon_text_1))
        assert result.is_displayed()

    @allure.title("Проверяем 2 раскрывашку в аккордеоне на главной странице Яндекс Самоката")
    def test_2(self):
        self.driver.get(links.MAIN_URL)
        main_page = LandingPageScooter(self.driver)
        main_page.scroll_to_accordeon()
        time.sleep(2)
        main_page.click_accordeon_2()
        main_page.wait_until_answer_visible_2()
        result = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(LandingPageLocators.accordeon_text_2))
        assert result.is_displayed()

    @allure.title("Проверяем 3 раскрывашку в аккордеоне на главной странице Яндекс Самоката")
    def test_3(self):
        self.driver.get(links.MAIN_URL)
        main_page = LandingPageScooter(self.driver)
        main_page.scroll_to_accordeon()
        time.sleep(2)
        main_page.click_accordeon_3()
        main_page.wait_until_answer_visible_3()
        result = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(LandingPageLocators.accordeon_text_3))
        assert result.is_displayed()

    @allure.title("Проверяем 4 раскрывашку в аккордеоне на главной странице Яндекс Самоката")
    def test_4(self):
        self.driver.get(links.MAIN_URL)
        main_page = LandingPageScooter(self.driver)
        main_page.scroll_to_accordeon()
        time.sleep(2)
        main_page.click_accordeon_4()
        main_page.wait_until_answer_visible_4()
        result = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(LandingPageLocators.accordeon_text_4))
        assert result.is_displayed()

    @allure.title("Проверяем 5 раскрывашку в аккордеоне на главной странице Яндекс Самоката")
    def test_5(self):
        self.driver.get(links.MAIN_URL)
        main_page = LandingPageScooter(self.driver)
        main_page.scroll_to_accordeon()
        time.sleep(2)
        main_page.click_accordeon_5()
        main_page.wait_until_answer_visible_5()
        result = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(LandingPageLocators.accordeon_text_5))
        assert result.is_displayed()

    @allure.title("Проверяем 6 раскрывашку в аккордеоне на главной странице Яндекс Самоката")
    def test_6(self):
        self.driver.get(links.MAIN_URL)
        main_page = LandingPageScooter(self.driver)
        main_page.scroll_to_accordeon()
        time.sleep(2)
        main_page.click_accordeon_6()
        main_page.wait_until_answer_visible_6()
        result = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(LandingPageLocators.accordeon_text_6))
        assert result.is_displayed()

    @allure.title("Проверяем 7 раскрывашку в аккордеоне на главной странице Яндекс Самоката")
    def test_7(self):
        self.driver.get(links.MAIN_URL)
        main_page = LandingPageScooter(self.driver)
        main_page.scroll_to_accordeon()
        time.sleep(2)
        main_page.click_accordeon_7()
        main_page.wait_until_answer_visible_7()
        result = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(LandingPageLocators.accordeon_text_7))
        assert result.is_displayed()

    @allure.title("Проверяем 8 раскрывашку в аккордеоне на главной странице Яндекс Самоката")
    def test_8(self):
        self.driver.get(links.MAIN_URL)
        main_page = LandingPageScooter(self.driver)
        main_page.scroll_to_accordeon()
        time.sleep(2)
        main_page.click_accordeon_8()
        main_page.wait_until_answer_visible_8()
        result = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(LandingPageLocators.accordeon_text_8))
        assert result.is_displayed()

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()