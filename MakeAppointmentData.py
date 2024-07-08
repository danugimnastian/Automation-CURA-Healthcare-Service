import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import LoginData
from webdriver_manager.chrome import ChromeDriverManager

def MakeAppointmentSuccess(driver):
        #Login Success
        LoginData.LoginSuccess(driver)
        time.sleep(1)
        #Click Login
        driver.find_element(By.ID, "btn-login").click()
        time.sleep(3)
        result = driver.find_element(By.XPATH, "//h2[normalize-space()='Make Appointment']").text
        assert("Make Appointment") in result
        #Make Appointment
        #Choose Facility
        driver.find_element(By.ID, "combo_facility").click()
        time.sleep(1)
        driver.find_element(By.XPATH, "//option[@value='Hongkong CURA Healthcare Center']").click()
        time.sleep(1)
        #Apply readmission
        driver.find_element(By.ID, "chk_hospotal_readmission").click()
        time.sleep(1)
        #Choose Healthcare Program
        driver.find_element(By.ID, "radio_program_medicaid").click()
        time.sleep(1)
        #Visit Date
        driver.find_element(By.XPATH, "//input[@id='txt_visit_date']").send_keys("28/06/2024")
        time.sleep(2)
        #Comment
        driver.find_element(By.ID, "txt_comment").send_keys("a healthy outside starts from the inside")
