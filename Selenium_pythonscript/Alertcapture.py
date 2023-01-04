import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

service_obj = Service(".\\chromedriver_win32\\chromedriver.exe");
driver = webdriver.Chrome(service= service_obj)
driver.implicitly_wait(5)

driver.get("https://rahulshettyacademy.com/loginpagePractise/")
driver.maximize_window()
time.sleep(3)
driver.find_element(By.CLASS_NAME,"blinkingText").click()
time.sleep(3)
windowsOpened = driver.window_handles
driver.switch_to.window(windowsOpened[1])

message = driver.find_element(By.CSS_SELECTOR, ".red").text
var = message.split("at")[1].strip().split(" ")[0]
driver.close()
driver.switch_to.window(windowsOpened[0])

driver.find_element(By.ID, "username").send_keys(var)
driver.find_element(By.ID, "password").send_keys(var)
driver.find_element(By.CSS_SELECTOR, "#signInBtn").click()
time.sleep(2)

wait = WebDriverWait(driver,10)
wait.until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, ".alert-danger")))
print(driver.find_element(By.CSS_SELECTOR, ".alert-danger").text)
time.sleep(3)

