import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("headless")      # without opening the browser it will run
chrome_options.add_argument("--ignore-certificate-errors")


service_obj = Service(".\\chromedriver_win32\\chromedriver.exe")
driver = webdriver.Chrome(service= service_obj,options=chrome_options)
driver.implicitly_wait(5)

driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()

driver.execute_script("window.scrollBy(0,document.body.scrollHeight);") # java scripts in this browser
driver.get_screenshot_as_file("screen.png")
time.sleep(2)