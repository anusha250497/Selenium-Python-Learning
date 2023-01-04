import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

service_obj = Service(".\\chromedriver_win32\\chromedriver.exe");
driver = webdriver.Chrome(service= service_obj)
driver.implicitly_wait(5)

driver.get("https://the-internet.herokuapp.com/windows")
driver.maximize_window()
time.sleep(3)

driver.find_element(By.LINK_TEXT,"Click Here").click()
windowsOpened = driver.window_handles

driver.switch_to.window(windowsOpened[1])
print(driver.find_element(By.XPATH,"/html/body/div/h3").text)
time.sleep(3)
driver.close()

driver.switch_to.window(windowsOpened[0])

assert "Opening a new window" == driver.find_element(By.TAG_NAME,"h3").text

