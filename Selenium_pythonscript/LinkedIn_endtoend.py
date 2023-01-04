import time

from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

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
Homepage=driver.find_element(By.XPATH,"//nav[@aria-label='Primary Navigation']").text
print("|| HOME-- PAGE --MENU ||")
print(Homepage)

#search
search= driver.find_element(By.CSS_SELECTOR,"input[placeholder='Search']")
search.send_keys("jobs")
search.send_keys(Keys.ENTER)
print("___search Done___")
time.sleep(3)

#jobmenu
driver.find_element(By.XPATH,"//span[@title='Jobs']").click()
print("||JOB *--* MENU *--* LIST||")
jobmenu=driver.find_element(By.CSS_SELECTOR,".display-flex.flex-column.list-style-none.pt1.pl4.pb5").text
print(jobmenu)
driver.find_element(By.XPATH,"(//span[contains(@class,'t-black t-bold t-14')][normalize-space()='My jobs'])[1]").click()
time.sleep(3)

#notify menu nd delete
driver.find_element(By.XPATH,"//span[@title='Notifications']").click()
driver.find_element(By.XPATH,"//body/div/div/div/div/div/div/main/div/section/div/div/div/div[1]")
driver.find_element(By.XPATH,"(//*[name()='svg'][@class='mercado-match'])[15]").click()
driver.find_element(By.XPATH,"(//li-icon[@type='trash'])[1]").click()
time.sleep(3)
print("___Notification Deleted___")

#sign out LinkedIn
driver.find_element(By.XPATH, "//span[@class='global-nav__primary-link-text']").click()
time.sleep(3)
driver.find_element(By.XPATH, '//*[@href="/m/logout/"]').click()
time.sleep(2)
print("___Linkedin sign out___")

driver.close()


