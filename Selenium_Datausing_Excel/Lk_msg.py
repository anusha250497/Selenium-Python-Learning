import time

from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.common.by import By

import pandas as pd

dataframe = pd.read_excel('Linkedin_Message.xlsx')

service_obj = Service(".\\chromedriver_win32\\chromedriver.exe")
driver = webdriver.Chrome(service= service_obj)
driver.implicitly_wait(5)


driver.get("https://www.linkedin.com/home")
driver.maximize_window()
time.sleep(3)

driver.find_element(By.XPATH, "//input[@class='input__input']").send_keys("9791441132")
driver.find_element(By.XPATH, "//input[@type='password']").send_keys("Anusha@25")
driver.find_element(By.XPATH, "//button[@type='submit']").click()
time.sleep(5)

#search
for index, i in enumerate( dataframe.index):
    print(dataframe.loc[i], end='\n\n')

    search= driver.find_element(By.CSS_SELECTOR,"input[placeholder='Search']")
    search.send_keys(dataframe.loc[i]['Name'])
    search.send_keys(Keys.ENTER)
    driver.find_element(By.XPATH,"(//span[normalize-space()='Message'])[1]").click()
    driver.find_element(By.XPATH,"//div[@aria-label='Write a message…']").send_keys("Hello")
    driver.find_element(By.CSS_SELECTOR,"button[type='submit']").click()
    driver.find_element(By.XPATH,"(//li-icon[@type='close'])[2]").click()
    driver.find_element(By.XPATH,"(//li-icon[@type='app-linkedin-bug-color-icon'])[1]").click()
    time.sleep(5)
