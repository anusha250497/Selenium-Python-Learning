import time

from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains

service_obj = Service(".\\chromedriver_win32\\chromedriver.exe")
driver = webdriver.Chrome(service= service_obj)
driver.implicitly_wait(5)
driver.maximize_window()

driver.get("https://jqueryui.com/droppable/")

driver.switch_to.frame(driver.find_element(By.CSS_SELECTOR,".demo-frame"))
drag=driver.find_element(By.XPATH,"//div[@id='draggable']")
drop=driver.find_element(By.XPATH,"//div[@id='droppable']")

ActionChains(driver).drag_and_drop(drag,drop).perform()