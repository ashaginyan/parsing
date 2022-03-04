from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# https://chromedriver.storage.googleapis.com/index.html

options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")
options.add_argument('--log-level=3')

driver = webdriver.Chrome(executable_path="chromedriver", options=options)
# driver.set_window_size(1920, 1080)

driver.get('https://www.rzd.ru/')
from_input = driver.find_element(by=By.ID, value='direction-from')
from_input.send_keys('Москва')
from_input.send_keys(Keys.ENTER)

to_input = driver.find_element(by=By.ID, value='direction-to')
to_input.send_keys('Санкт-Петербург')
to_input.send_keys(Keys.ENTER)

to_date = driver.find_element(by=By.ID, value='datepicker-from')
to_date.send_keys('04.03.2022')
to_date.send_keys(Keys.ENTER)

button = driver.find_element(by=By.CSS_SELECTOR, value='#rzd-search-widget > div > div.rzd-button-wrapper.rzd-cell.rzd-cell-15 > a')
button.click()

time.sleep(5)

driver.quit()
