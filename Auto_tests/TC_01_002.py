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

#Close webbrowser
sleep(3)
driver.close()