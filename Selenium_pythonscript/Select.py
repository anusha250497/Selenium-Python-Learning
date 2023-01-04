import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

service_obj = Service(".\\chromedriver_win32\\chromedriver.exe");
driver = webdriver.Chrome(service= service_obj)

driver.get("https://www.google.com")
driver.maximize_window()
driver.get("https://rahulshettyacademy.com/angularpractice/")
time.sleep(3)
driver.find_element(By.NAME,"name").send_keys("ABC")
driver.find_element(By.XPATH,"/html/body/app-root/form-comp/div/form/div[2]/input").send_keys("abcd1234@gmail.com")
driver.find_element(By.XPATH,"//*[@id='exampleInputPassword1']").send_keys("Abcd@1234")
driver.find_element(By.ID,"exampleCheck1").click()
#static dropdown
dropdown= Select(driver.find_element(By.ID,"exampleFormControlSelect1"))
dropdown.select_by_index(0)
dropdown.select_by_visible_text("Female")
#dropdown.select_by_value()
#OR this method
#driver.find_element(By.ID,"exampleFormControlSelect1").send_keys("Female")
driver.find_element(By.CSS_SELECTOR,"body > app-root > form-comp > div > form > input").click()
driver.find_element(By.CSS_SELECTOR,"#inlineRadio1").click()
driver.find_element(By.NAME,"bday").send_keys("25-04-1997")
driver.find_element(By.XPATH,"/html/body/app-root/form-comp/div/h4/input").clear()
time.sleep(5)
message = driver.find_element(By.CLASS_NAME,"alert-success").text
print(message)
#to validate test pass or fail
assert "Success" in message  #pass