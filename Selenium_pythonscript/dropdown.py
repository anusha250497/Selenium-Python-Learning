import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

service_obj = Service(".\\chromedriver_win32\\chromedriver.exe");
driver = webdriver.Chrome(service= service_obj)

driver.get("https://www.google.com")
driver.maximize_window()
driver.get("https://rahulshettyacademy.com/dropdownsPractise/")
time.sleep(3)
#dynamic dropdown
driver.find_element(By.ID,"autosuggest").send_keys("ind")
time.sleep(3)
countries = driver.find_elements(By.CSS_SELECTOR,"li[class = 'ui-menu-item'] a")
print(len(countries))

for country in countries:
    if country.text == "India":
        country.click()
        break
#print(driver.find_element(By.ID,"autosuggest").get_attribute("value")) --> india
assert driver.find_element(By.ID,"autosuggest").get_attribute("value")=="India"
