import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

s=Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=s)
#driver.maximize_window()
#driver.get('https://www.google.com')

loginname = '7218820479'
password = 'Varunkarwa012'
#chrdriv = "D:\beminiprojects\STQA\selenium\chromedriver.exe"
#driver = webdriver.Chrome(chrdriv)

driver.get('http://www.facebook.com')
driver.maximize_window()
print("Opened Facebook")
time.sleep(1)

emailid = driver.find_element_by_id("email")
emailid.send_keys(loginname)
print("Email Id entered")
time.sleep(1)

passw = driver.find_element_by_id('pass')
passw.send_keys(password)
print("Password entered")
time.sleep(2)

nextButton = driver.find_element_by_name('login')
nextButton.click()
print('Logged in successfully')
time.sleep(2)


print('Now Closing Window')
time.sleep(10)

driver.close()
print('Test carried out successfully!')