from selenium.webdriver.firefox import webdriver
import links
from pages.order_page import *
import pytest


class TestLandingAccordeon:
    driver = None

    @classmethod
    def setup_class(cls):
        cls.driver = webdriver.Firefox()

    @allure.title("Проверяем, что раскрываются все пункты в блоке вопросов и ответов")
    @pytest.mark.parametrize("question, answer",
                             [
                                 [LandingPageLocators.accordeon_1, LandingPageLocators.accordeon_text_1],
                                 [LandingPageLocators.accordeon_2, LandingPageLocators.accordeon_text_2],
                                 [LandingPageLocators.accordeon_3, LandingPageLocators.accordeon_text_3],
                                 [LandingPageLocators.accordeon_4, LandingPageLocators.accordeon_text_4],
                                 [LandingPageLocators.accordeon_5, LandingPageLocators.accordeon_text_5],
                                 [LandingPageLocators.accordeon_6, LandingPageLocators.accordeon_text_6],
                                 [LandingPageLocators.accordeon_7, LandingPageLocators.accordeon_text_7],
                                 [LandingPageLocators.accordeon_8, LandingPageLocators.accordeon_text_8]
                             ])
    def test_questions_and_answers_block(self, question, answer):
        main = OrderPage(self.driver)
        main.navigate(links.MAIN_URL)
        main.scroll_to_accordeon()
        main.wait_for_accordeon_in_view()
        main.click_element(question)
        result = main.wait_for_element_visible(answer)
        assert result.is_displayed()

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()