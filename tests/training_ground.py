from selenium import webdriver
from page_objects.training_ground_page import TrainingGroundPage

# Test Setup
browser = webdriver.Chrome()
test_value = 'it worked'

# Test
training_page = TrainingGroundPage(driver=browser)
training_page.go()
training_page.type_into_input(test_value)
txt_from_input = training_page.get_input_text()
assert txt_from_input == test_value, f"Test Failed: Input did not match expected {test_value}."
print("Test Passed.")
