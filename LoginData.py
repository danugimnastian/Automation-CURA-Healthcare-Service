import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

   
def LoginSuccess(driver):
    driver.get("https://katalon-demo-cura.herokuapp.com/")
    driver.maximize_window()
    time.sleep(2)
    driver.maximize_window()
    driver.find_element(By.ID, "btn-make-appointment").click()
    time.sleep(1)
    driver.find_element(By.ID, "txt-username").send_keys("John Doe")
    time.sleep(1)
    driver.find_element(By.ID, "txt-password").send_keys("ThisIsNotAPassword")

def LoginWrongPassword(driver):
    driver.get("https://katalon-demo-cura.herokuapp.com/")
    driver.maximize_window()
    time.sleep(2)
    driver.maximize_window()
    driver.find_element(By.ID, "btn-make-appointment").click()
    time.sleep(1)
    driver.find_element(By.ID, "txt-username").send_keys("John Doe")
    time.sleep(1)
    driver.find_element(By.ID, "txt-password").send_keys("WrongPass")

def LoginEmpty(driver):
    driver.get("https://katalon-demo-cura.herokuapp.com/")
    driver.maximize_window()
    time.sleep(2)
    driver.maximize_window()
    driver.find_element(By.ID, "btn-make-appointment").click()


