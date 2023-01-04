import XLUtils
import time
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.common.by import By

service_obj = Service(".\\chromedriver_win32\\chromedriver.exe")
driver = webdriver.Chrome(service= service_obj)
driver.implicitly_wait(5)

driver.get("https://www.linkedin.com/home")
driver.maximize_window()
time.sleep(3)

path = "C:\\Users\\AnushaDeivasigamani\\Documents\\Linkedin_login.xlsx"
rows=XLUtils.getRowCount(path,'Sheet1')

for r in range(2,rows+1):
    EmailOrPhone = XLUtils.readData(path,"Sheet1",r,1)
    Password = XLUtils.readData(path,"Sheet1",r,2)

    driver.find_element(By.CSS_SELECTOR, "#session_key").send_keys(EmailOrPhone)
    driver.find_element(By.XPATH, "//input[@id='session_password']").send_keys(Password)
    time.sleep(3)
    driver.find_element(By.XPATH, "//button[@type='submit']").click()
    time.sleep(5)
    if driver.title == "LinkedIn Login, Sign in | LinkedIn":
        errormsg = driver.find_element(By.XPATH, "//div[@id='error-for-password']").text
        print(errormsg)
        assert "That’s not the right password.Try again"
        "sign in with a one-time link" in errormsg
        print("Test Failed")
        XLUtils.writeData(path, "Sheet1", r, 3, "Test Failed")

    else:
        driver.find_element(By.XPATH, "//span[@class='global-nav__primary-link-text']").click()
        driver.find_element(By.XPATH, '//*[@href="/m/logout/"]').click()
        time.sleep(2)
        print("Test passed")
        XLUtils.writeData(path, "Sheet1", r, 3, "Test passed")
        continue
    break



