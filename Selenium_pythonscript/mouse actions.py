import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

service_obj = Service(".\\chromedriver_win32\\chromedriver.exe");
driver = webdriver.Chrome(service= service_obj)
driver.implicitly_wait(5)

driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()

mouseHover= driver.find_element(By.ID,"mousehover")

top = driver.find_element(By.XPATH,"/html/body/div[4]/div/fieldset/div/div/a[2]")
reload = driver.find_element(By.XPATH,"/html/body/div[4]/div/fieldset/div/div/a[2]")

actions = ActionChains(driver)
actions.move_to_element(mouseHover).context_click(top).move_to_element(reload).click().perform()

#or we can write directly like this

#actions = ActionChains(driver)

#actions.move_to_element(driver.find_element(By.ID,"mousehover")).perform()
#actions.context_click(driver.find_element(By.LINK_TEXT,"top")).perform()
#actions.move_to_element(driver.find_element(By.LINK_TEXT,"reload")).click().perform()

