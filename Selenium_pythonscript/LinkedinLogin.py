import time
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.common.by import By
import itertools

Emailorphone = ["9791441132","mangalshri110697@gmail.com"]
Password = ["Anusha@256","Ozzzy@28"]

#credentials=[{"EmailOrPhone":"mangalshri110697@gmail.com","Password":"Ozzzy@28"},{"EmailOrPhone":"9791441132","Password":"Anusha234"}]

service_obj = Service(".\\chromedriver_win32\\chromedriver.exe")
driver = webdriver.Chrome(service= service_obj)
driver.implicitly_wait(5)
driver.maximize_window()
#time.sleep(3)
for (i, j) in itertools.zip_longest( Emailorphone , Password):
    driver.get("https://www.linkedin.com/home")
    driver.find_element(By.CSS_SELECTOR, "#session_key").send_keys(i)
    driver.find_element(By.XPATH, "//input[@id='session_password']").send_keys(j)
    time.sleep(3)
    driver.find_element(By.XPATH, "//button[@type='submit']").click()
    cur_title1=driver.title
    time.sleep(10)
    if cur_title1 == "LinkedIn Login, Sign in | LinkedIn":
        errormsg = driver.find_element(By.XPATH, "//div[@id='error-for-password']").text
        print(errormsg)
        assert "That’s not the right password" in errormsg
        # assert "Couldn’t find a LinkedIn account associated with this email" in errormsg
        continue
    if cur_title1 =="Security Verification | LinkedIn":
       print(cur_title1+(" Not able to login because of verification page"))
       time.sleep(3)
       continue
    else:
        driver.find_element(By.XPATH, "//span[@class='global-nav__primary-link-text']").click()
        time.sleep(3)
        driver.find_element(By.XPATH, '//*[@href="/m/logout/"]').click()
        time.sleep(2)

