from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
import time
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.chrome.options import Options

def create_webdriver_instance():
    chrome_options = Options()
    #chrome_options.add_argument("--headless")  
    chrome_options.add_argument("--disable-gpu")  
    chrome_options.add_argument("--no-sandbox")  
    chrome_options.add_argument("start-maximized")  
    chrome_options.add_argument("disable-infobars")  
    chrome_options.add_argument("--disable-extensions")  


    driver = webdriver.Chrome(options=chrome_options)
    return driver

driver = create_webdriver_instance()

driver.get('C:\\Open Source\\Selenium Login Form\\frontend\\login\\index.html')
time.sleep(1)

emailInput = driver.find_element(By.ID, "email")

emailInput.clear()

emailInput.send_keys('test@gmail.com')

time.sleep(1)

passwordInput = driver.find_element(By.ID, "password")

passwordInput.clear()

passwordInput.send_keys('yapyapyap!')

time.sleep(1)

loginButton = driver.find_element(By.ID, 'loginButton')

loginButton.click()
    
time.sleep(1)

driver.quit()


