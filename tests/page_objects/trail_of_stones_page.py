from selenium.webdriver.common.by import By
from .base_page import BasePage


class TrailOfStones(BasePage):
    url = 'https://techstepacademy.com/trial-of-the-stones'

    # Riddle of Stones
    def stone_input(self):
        return self.driver.find_element(By.ID, 'r1Input')

    def stone_answer_button(self):
        return self.driver.find_element(By.CSS_SELECTOR, 'button#r1Btn')

    def stone_result(self):
        return self.driver.find_element(By.CSS_SELECTOR, 'div#passwordBanner > h4')

    # Riddle of Secrets
    def secrets_input(self):
        return self.driver.find_element(By.ID, 'r2Input')

    def secrets_answer_btn(self):
        return self.driver.find_element(By.ID, 'r2Butn')

    def secrets_result(self):
        return self.driver.find_element(By.CSS_SELECTOR, 'div#successBanner1 > h4')

    # Two Merchants
    def get_richest_merchant_name(self):
        richest_merchant = self.driver.find_element(By.XPATH, '//p[text()="3000"]/.. /span/b')
        return richest_merchant.text

    def merchant_input(self):
        return self.driver.find_element(By.ID, 'r3Input')

    def merchant_answer_btn(self):
        return self.driver.find_element(By.CSS_SELECTOR, 'button#r3Butn')

    def merchant_result(self):
        return self.driver.find_element(By.CSS_SELECTOR, 'div#successBanner2 > h4')

    # Final check
    def check_btn(self):
        return self.driver.find_element(By.CSS_SELECTOR, 'button[name="checkButn"]')

    def final_msg(self):
        final_msg_field = self.driver.find_element(By.CSS_SELECTOR, 'div#trialCompleteBanner > h4')
        return final_msg_field.text
