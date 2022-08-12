from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

from page_objects import list
from page_objects.trail_of_stones_page import TrailOfStones

# Expected variables
R1_LABEL = 'Another word for stone (4 letters)?'
success_msg = 'Success!'
complete_msg = 'Trial Complete'

# def test_trail_of_stones():
browser = webdriver.Chrome(ChromeDriverManager().install())
trail_of_stones_page = TrailOfStones(driver=browser)
trail_of_stones_page.go()
# Riddle of Stones actions
trail_of_stones_page.stone_input.input_text('rock')
trail_of_stones_page.stone_answer_button.click()
password = trail_of_stones_page.stone_result.text

# Riddle of Secrets actions
trail_of_stones_page.secrets_input.input_text(password)
trail_of_stones_page.secrets_answer_btn.click()
trail_of_stones_page.secrets_success_msg = trail_of_stones_page.secrets_result.text
assert trail_of_stones_page.secrets_success_msg == success_msg

# Two Merchants actions
richest_merchant = list.PageWithListings(browser.page_source).highest_wealth.name

# tree = etree.HTML(browser.page_source)
# merchant_divs = tree.findall(".//div/span/..")
# merchant1 = merchant_divs[0]
# merchant2 = merchant_divs[1]
#
# merchant1_name = merchant1.find("./span/b").text
# merchant2_name = merchant2.find("./span/b").text
#
# merchant1_wealth = merchant1.find("./p").text
# merchant2_wealth = merchant2.find("./p").text
# print(merchant1_name, merchant1_wealth, merchant2_name, merchant2_wealth)

# richest_merchant_name = trail_of_stones_page.get_richest_merchant_name
trail_of_stones_page.merchant_input.input_text(richest_merchant)
trail_of_stones_page.merchant_answer_btn.click()
trail_of_stones_page.merchant_success = trail_of_stones_page.merchant_result.text
assert trail_of_stones_page.merchant_success == success_msg

# Final check
trail_of_stones_page.check_btn.click()
# browser.save_screenshot('../screenshots/scr.png')
assert trail_of_stones_page.final_msg == complete_msg

browser.quit()
