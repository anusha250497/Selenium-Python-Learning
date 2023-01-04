import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj = Service(".\\chromedriver_win32\\chromedriver.exe");
driver = webdriver.Chrome(service= service_obj)

driver.get("https://www.google.com")
driver.maximize_window()
driver.get("https://www.amazon.com")
driver.find_element(By.ID,"searchDropdownBox").send_keys("Books")
time.sleep(3)
driver.find_element(By.ID,"nav-search-submit-button").click()
time.sleep(3)
driver.find_element(By.ID,"twotabsearchtextbox").send_keys("twostates")
time.sleep(3)
driver.find_element(By.ID,"nav-search-submit-button").click()
driver.close()