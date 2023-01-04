import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

service_obj = Service(".\\chromedriver_win32\\chromedriver.exe");
driver = webdriver.Chrome(service= service_obj)
driver.implicitly_wait(5)
browserSortedVeggies=[]
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
driver.maximize_window()
time.sleep(3)
driver.find_element(By.LINK_TEXT,"Top Deals").click()
windowsOpened = driver.window_handles
driver.switch_to.window(windowsOpened[1])

driver.find_element(By.XPATH,"//span[text()='Veg/fruit name']").click()
time.sleep(3)
#collecting all veggies name
veggieWebElements = driver.find_elements(By.XPATH,"//tr/td[1]")  #debugging
for ele in veggieWebElements:
    browserSortedVeggies.append(ele.text)

originalbrowserSortedList = browserSortedVeggies.copy() #or slice()
#sort this browserSortedVeggies
browserSortedVeggies.sort()
assert browserSortedVeggies == originalbrowserSortedList
