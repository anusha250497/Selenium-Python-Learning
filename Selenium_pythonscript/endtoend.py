import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

service_obj = Service(".\\chromedriver_win32\\chromedriver.exe")
driver = webdriver.Chrome(service= service_obj)
driver.implicitly_wait(5)

driver.get("https://www.rahulshettyacademy.com/angularpractice/")
driver.maximize_window()
# xpath--> //a[contains(@href,'Shop')]  css--> a[href*='Shop']
driver.find_element(By.CSS_SELECTOR,"a[href*='shop']").click()
products = driver.find_elements(By.XPATH,"//div[@class='card h-100']")

for product in products:
    productName = product.find_element(By.XPATH,"div/h4/a").text
    if productName == "Blackberry":
        product.find_element(By.XPATH,"div/button").click()

driver.find_element(By.CSS_SELECTOR,"a[class*='btn-primary']").click()
driver.find_element(By.XPATH,"//button[@class='btn btn-success']").click()
driver.find_element(By.ID,"country").send_keys("Ind")

wait=WebDriverWait(driver,10)
wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT,"India")))
driver.find_element(By.LINK_TEXT,"India").click()

driver.find_element(By.XPATH,"//div[@class='checkbox checkbox-primary']").click()
driver.find_element(By.XPATH,"//input[@type='submit']").click()
message=driver.find_element(By.CLASS_NAME,"alert-success").text
print(message)
assert "Success" in message
driver.close()




