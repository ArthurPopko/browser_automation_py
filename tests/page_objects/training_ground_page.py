from selenium.webdriver.common.by import By
from .base_page import BasePage


class TrainingGroundPage(BasePage):

    url = 'https://techstepacademy.com/training-ground/'

    def type_into_input(self, text):
        inpt = self.driver.find_element(By.ID, 'ipt1')
        inpt.clear()
        inpt.send_keys(text)
        return None

    def get_input_text(self):
        inpt = self.driver.find_element(By.ID, 'ipt1')
        elem_text = inpt.get_attribute('value')
        return elem_text

    def click_button_1(self):
        button = self.driver.find_element(By.ID, 'b1')
        button.click()
        return None
