import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

service_obj = Service(".\\chromedriver_win32\\chromedriver.exe");
driver = webdriver.Chrome(service= service_obj)

driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()
time.sleep(3)

checkboxes = driver.find_elements(By.XPATH,"//input[@type= 'checkbox']")
print(len(checkboxes))

for checkboxe in checkboxes:
    if checkboxe.get_attribute("value") == "option2":
        checkboxe.click()
        assert checkboxe.is_selected()
        break
#radiobutton
radiobuttons = driver.find_elements(By.CSS_SELECTOR,".radioButton")
radiobuttons[2].click()
assert  radiobuttons[2].is_selected()
#hide or show
assert driver.find_element(By.ID,"displayed-text").is_displayed()
driver.find_element(By.ID,"hide-textbox").click()
assert not driver.find_element(By.ID,"displayed-text").is_displayed()
driver.find_element(By.ID,"show-textbox").click()
#alerts
name = "rahul"
driver.find_element(By.CSS_SELECTOR,"#name").send_keys(name)
driver.find_element(By.ID,"alertbtn").click()
alert = driver.switch_to.alert
time.sleep(3)
alertText = alert.text
print(alertText)
assert name in alertText
alert.accept() #to click ok
#alert.dismiss() to click cancel
time.sleep(2)