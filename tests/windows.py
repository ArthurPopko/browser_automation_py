from selenium import webdriver

browser1 = webdriver.Chrome()
# browser2 = webdriver.Chrome()

browser1.get('https://techstepacademy.com/training-ground')
# Tabs
browser1.execute_script('window.open("https://techstepacademy.com/training-ground", "_blank")')
browser1.execute_script('window.open("https://techstepacademy.com/training-ground", "_blank")')
browser1.execute_script('window.open("https://techstepacademy.com/training-ground", "_blank")')
# browser2.get('https://google.com')

# Get the all tabs
tabs = browser1.window_handles
print(len(browser1.window_handles))
# Switch to a specific tab by index
browser1.switch_to.window(tabs[2])
