from time import sleep
from login_password import login_standard
from login_password import password_login
from selenium.webdriver.common.by import By
from lib2to3.pgen2 import driver
from selenium import webdriver

#Open webbrowser
driver = webdriver.Edge()
driver.maximize_window()
driver.get('https://www.saucedemo.com/')

#Login to shop
login = driver.find_element(By.ID, 'user-name')
login.click()
login.send_keys(login_standard)
sleep(0.5)

password = driver.find_element(By.ID, 'password')
password.click()
password.send_keys(password_login)
sleep(0.5)

login_button = driver.find_element(By.ID, 'login-button')
login_button.click()

#Add products to cart in main site and remove 
item_01 = driver.find_element(By.XPATH, '/html/body/div/div/div/div[2]/div/div/div/div[1]/div[2]/div[2]/button')
item_01.click()
sleep(0.5)
item_01_remove = driver.find_element(By.XPATH, '/html/body/div/div/div/div[2]/div/div/div/div[1]/div[2]/div[2]/button')
item_01_remove.click()
sleep(0.5)

item_02 = driver.find_element(By.XPATH, '/html/body/div/div/div/div[2]/div/div/div/div[2]/div[2]/div[2]/button')
item_02.click()
sleep(0.5)
item_02_remove = driver.find_element(By.XPATH, '/html/body/div/div/div/div[2]/div/div/div/div[2]/div[2]/div[2]/button')
item_02_remove.click()
sleep(0.5)

item_03 = driver.find_element(By.XPATH, '/html/body/div/div/div/div[2]/div/div/div/div[3]/div[2]/div[2]/button')
item_03.click()
sleep(0.5)
item_03_remove = driver.find_element(By.XPATH, '/html/body/div/div/div/div[2]/div/div/div/div[3]/div[2]/div[2]/button')
item_03_remove.click()
sleep(0.5)

item_04 = driver.find_element(By.XPATH, '/html/body/div/div/div/div[2]/div/div/div/div[4]/div[2]/div[2]/button')
item_04.click()
sleep(0.5)
item_04_remove = driver.find_element(By.XPATH, '/html/body/div/div/div/div[2]/div/div/div/div[4]/div[2]/div[2]/button')
item_04_remove.click()
sleep(0.5)

item_05 = driver.find_element(By.XPATH, '/html/body/div/div/div/div[2]/div/div/div/div[5]/div[2]/div[2]/button')
item_05.click()
sleep(0.5)
item_05_remove = driver.find_element(By.XPATH, '/html/body/div/div/div/div[2]/div/div/div/div[5]/div[2]/div[2]/button')
item_05_remove.click()
sleep(0.5)

item_06 = driver.find_element(By.XPATH, '/html/body/div/div/div/div[2]/div/div/div/div[6]/div[2]/div[2]/button')
item_06.click()
sleep(0.5)
item_06_remove = driver.find_element(By.XPATH, '/html/body/div/div/div/div[2]/div/div/div/div[6]/div[2]/div[2]/button')
item_06_remove.click()
sleep(0.5)

#Close webbrowser
sleep(3)
driver.close()