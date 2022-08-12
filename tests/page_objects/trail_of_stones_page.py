from selenium.webdriver.common.by import By
from .base_element import BaseElement
from .base_page import BasePage


class TrailOfStones(BasePage):
    url = 'https://techstepacademy.com/trial-of-the-stones'

    # Riddle of Stones
    @property
    def stone_input(self):
        locator = (By.ID, 'r1Input')
        return BaseElement(self.driver, by=locator[0], value=locator[1])

    @property
    def stone_answer_button(self):
        locator = (By.CSS_SELECTOR, 'button#r1Btn')
        return BaseElement(self.driver, by=locator[0], value=locator[1])

    @property
    def stone_result(self):
        locator = (By.CSS_SELECTOR, 'div#passwordBanner > h4')
        return BaseElement(self.driver, by=locator[0], value=locator[1])

    # Riddle of Secrets
    @property
    def secrets_input(self):
        locator = (By.ID, 'r2Input')
        return BaseElement(self.driver, by=locator[0], value=locator[1])

    @property
    def secrets_answer_btn(self):
        locator = (By.ID, 'r2Butn')
        return BaseElement(self.driver, by=locator[0], value=locator[1])

    @property
    def secrets_result(self):
        locator = (By.CSS_SELECTOR, 'div#successBanner1 > h4')
        return BaseElement(self.driver, by=locator[0], value=locator[1])

    # Two Merchants
    @property
    def get_richest_merchant_name(self):
        richest_merchant = self.driver.find_element(By.XPATH, '//p[text()="3000"]/.. /span/b')
        return richest_merchant.text

    @property
    def merchant_input(self):
        locator = (By.ID, 'r3Input')
        return BaseElement(self.driver, by=locator[0], value=locator[1])

    @property
    def merchant_answer_btn(self):
        locator = (By.CSS_SELECTOR, 'button#r3Butn')
        return BaseElement(self.driver, by=locator[0], value=locator[1])

    @property
    def merchant_result(self):
        locator = (By.CSS_SELECTOR, 'div#successBanner2 > h4')
        return BaseElement(self.driver, by=locator[0], value=locator[1])

    # Final check
    @property
    def check_btn(self):
        locator = (By.CSS_SELECTOR, 'button[name="checkButn"]')
        return BaseElement(self.driver, by=locator[0], value=locator[1])

    @property
    def final_msg(self):
        final_msg_field = self.driver.find_element(By.CSS_SELECTOR, 'div#trialCompleteBanner > h4')
        return final_msg_field.text
