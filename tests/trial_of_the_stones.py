from selenium import webdriver
from selenium.webdriver.common.by import By

# No page object, no optimization
URL = 'https://techstepacademy.com/trial-of-the-stones'
R1_LABEL = 'Another word for stone (4 letters)?'
success_msg = 'Success!'
complete_msg = 'Trial Complete'


# def test_trail_of_stones():
browser = webdriver.Chrome()
browser.get(URL)

# Riddle of Stones
stone_input = browser.find_element(By.ID, 'r1Input')
stone_answer_button = browser.find_element(By.CSS_SELECTOR, 'button#r1Btn')
stone_result = browser.find_element(By.CSS_SELECTOR, 'div#passwordBanner > h4')

# Riddle of Secrets
secrets_input = browser.find_element(By.ID, 'r2Input')
secrets_answer_btn = browser.find_element(By.ID, 'r2Butn')
secrets_result = browser.find_element(By.CSS_SELECTOR, 'div#successBanner1 > h4')

# Two Merchants
richest_merchant = browser.find_element(By.XPATH, '//p[text()="3000"]/.. /span/b')
richest_merchant_name = richest_merchant.text
merchant_input = browser.find_element(By.ID, 'r3Input')
merchant_answer_btn = browser.find_element(By.CSS_SELECTOR, 'button#r3Butn')
merchant_result = browser.find_element(By.CSS_SELECTOR, 'div#successBanner2 > h4')

# Final check
check_btn = browser.find_element(By.CSS_SELECTOR, 'button[name="checkButn"]')
final_msg = browser.find_element(By.CSS_SELECTOR, 'div#trialCompleteBanner > h4')

# Riddle of Stones actions
stone_input.send_keys('rock')
stone_answer_button.click()
password = stone_result.text

# Riddle of Secrets actions
secrets_input.send_keys(password)
secrets_answer_btn.click()
secrets_success_msg = secrets_result.text
assert secrets_success_msg == success_msg

# Two Merchants actions
merchant_input.send_keys(richest_merchant_name)
merchant_answer_btn.click()
merchant_success = merchant_result.text
assert merchant_success == success_msg

# Final check
check_btn.click()
# browser.save_screenshot('../screenshots/scr.png')
assert final_msg == final_msg

# browser.close()
