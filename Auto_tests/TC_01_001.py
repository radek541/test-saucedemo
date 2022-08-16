
from lib2to3.pgen2 import driver
from time import sleep
from selenium import webdriver

#Open webbrowser
driver = webdriver.Edge()
driver.maximize_window()
driver.get('https://www.saucedemo.com/')

#Close webbrowser
sleep(3)
driver.close()