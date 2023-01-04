import time

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium import webdriver

service_obj = Service(".\\chromedriver_win32\\chromedriver.exe")
driver = webdriver.Chrome(service= service_obj)
driver.implicitly_wait(5)
driver.maximize_window()


driver.get("https://sqa.stackexchange.com/questions/15527/handling-the-unexpected-popup-ads-in-website")

driver.find_element(By.XPATH, "//button[normalize-space()='Accept all cookies']").click()
time.sleep(3)
Scroll
driver.execute_script("window.scrollBy(0,2000)","")
time.sleep(3)
driver.execute_script("window.scrollBy(0,-2000)","")
time.sleep(4)

