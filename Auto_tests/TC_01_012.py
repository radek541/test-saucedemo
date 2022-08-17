from genericpath import exists
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

#Add products to cart in main site
item_01 = driver.find_element(By.XPATH, '/html/body/div/div/div/div[2]/div/div/div/div[1]/div[2]/div[2]/button')
item_01.click()
sleep(0.5)

item_02 = driver.find_element(By.XPATH, '/html/body/div/div/div/div[2]/div/div/div/div[2]/div[2]/div[2]/button')
item_02.click()
sleep(0.5)

item_03 = driver.find_element(By.XPATH, '/html/body/div/div/div/div[2]/div/div/div/div[3]/div[2]/div[2]/button')
item_03.click()
sleep(0.5)

item_04 = driver.find_element(By.XPATH, '/html/body/div/div/div/div[2]/div/div/div/div[4]/div[2]/div[2]/button')
item_04.click()
sleep(0.5)

item_05 = driver.find_element(By.XPATH, '/html/body/div/div/div/div[2]/div/div/div/div[5]/div[2]/div[2]/button')
item_05.click()
sleep(0.5)

item_06 = driver.find_element(By.XPATH, '/html/body/div/div/div/div[2]/div/div/div/div[6]/div[2]/div[2]/button')
item_06.click()
sleep(0.5)

#Go to cart and go to checkout
cart_button = driver.find_element(By.ID, 'shopping_cart_container')
cart_button.click()
sleep(1)

checkout_button = driver.find_element(By.ID, 'checkout')
checkout_button.click()
sleep(0.5)

#Send infromation
first_name_textbox = driver.find_element(By.ID, 'first-name')
first_name_textbox.send_keys('Jack')

last_name_textbox = driver.find_element(By.ID, 'last-name')
last_name_textbox.send_keys('Black')

postal_code_textbox = driver.find_element(By.ID, 'postal-code')
postal_code_textbox.send_keys('00-000')
sleep(0.5)

continue_button = driver.find_element(By.ID, 'continue')
continue_button.click()
sleep(0.5)

finish_button = driver.find_element(By.ID, 'finish')
finish_button.click()
sleep(0.5)

#back to home site
back_to_products = driver.find_element(By.ID, 'back-to-products')
back_to_products.click()

#Close webbrowser
sleep(3)
driver.close()