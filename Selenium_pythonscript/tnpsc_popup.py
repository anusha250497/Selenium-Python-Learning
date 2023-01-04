import time

from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.common.by import By

service_obj = Service(".\\chromedriver_win32\\chromedriver.exe")
driver = webdriver.Chrome(service= service_obj)
driver.implicitly_wait(5)

driver.get("https://www.tnpsc.gov.in/")
driver.maximize_window()
time.sleep(3)

driver.find_element(By.XPATH,"//h3[@class='home-title reg-user']").click()
myalert = driver.switch_to.alert
myalert.accept() # ok
time.sleep(3)
