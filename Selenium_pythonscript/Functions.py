import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
#list
expectedList = ['Cucumber - 1 Kg','Raspberry - 1/4 Kg','Strawberry - 1/4 Kg']
actualList =[]
service_obj = Service(".\\chromedriver_win32\\chromedriver.exe");
driver = webdriver.Chrome(service= service_obj)

driver.implicitly_wait(5) #implicit wait

driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
driver.maximize_window()

driver.find_element(By.CSS_SELECTOR,".search-keyword").send_keys("ber")
time.sleep(3)

results= driver.find_elements(By.XPATH,"//div[@class='products']/div")
count = len(results)
assert count > 0

for result in results:
    actualList.append(result.find_element(By.XPATH,"h4").text) # add in list
    result.find_element(By.XPATH,"div/button").click()

assert expectedList == actualList

driver.find_element(By.CSS_SELECTOR,"img[alt='Cart']").click()

driver.find_element(By.XPATH,"//button[text()='PROCEED TO CHECKOUT']").click()
#sum validation
prices = driver.find_elements(By.CSS_SELECTOR,"tr td:nth-child(5) p")
sum = 0
for price in prices:
    sum = sum + int(price.text)
print(sum)
totalAmount = int(driver.find_element(By.CSS_SELECTOR,".totAmt").text)
assert sum == totalAmount

driver.find_element(By.CLASS_NAME,"promoCode").send_keys("rahulshettyacademy")
driver.find_element(By.CLASS_NAME,"promoBtn").click()

#EXPLICIT WAIT

wait=WebDriverWait(driver,10)
wait.until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR,".promoInfo")))
print(driver.find_element(By.CLASS_NAME,"promoInfo").text)

#comparing totlamt with disc amt

totalAfterDiscount = float(driver.find_element(By.CSS_SELECTOR,".discountAmt").text)
print(totalAfterDiscount)
assert  totalAfterDiscount < totalAmount
