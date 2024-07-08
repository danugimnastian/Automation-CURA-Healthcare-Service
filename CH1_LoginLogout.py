import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import LoginData
import HtmlTestRunner

options = Options()

options.add_experimental_option("excludeSwitches", ["enable-logging"])


class LoginLogout(unittest.TestCase):
    
    def setUp(self):
        self.driver = webdriver.Chrome(options=options)


    def testLoginSuccess(self):
        #Login with Valid credentials
        LoginData.LoginSuccess(self.driver)
        time.sleep(1)
        #Click Login
        self.driver.find_element(By.ID, "btn-login").click()
        time.sleep(3)
        #Validate Login Success
        result = self.driver.find_element(By.XPATH, "//h2[normalize-space()='Make Appointment']").text
        assert("Make Appointment") in result

    def testLoginWrongPassword(self):
        #Login with Wrong Password
        LoginData.LoginWrongPassword(self.driver)
        time.sleep(1)
        #Click Login
        self.driver.find_element(By.ID, "btn-login").click()
        time.sleep(3)
        result = self.driver.find_element(By.XPATH, "//p[@class='lead text-danger']").text
        assert("Login failed!") in result

    def testEmpty(self):
        #Login with Empty Data
        LoginData.LoginEmpty(self.driver)
        time.sleep(1)
        #Click Login
        self.driver.find_element(By.ID, "btn-login").click()    
        time.sleep(3)
        #Validate Login Failed
        result = self.driver.find_element(By.XPATH, "//p[@class='lead text-danger']").text
        assert("Login failed!") in result       

    def testLogoutSuccess(self):
        #Login with Valid credentials
        LoginData.LoginSuccess(self.driver)
        time.sleep(1)
        #Click Login
        self.driver.find_element(By.ID, "btn-login").click()
        time.sleep(3)
        #Logout
        #Click Burger Bar
        self.driver.find_element(By.XPATH,"//i[@class='fa fa-bars']").click()
        time.sleep(2)
        #Click Logout
        self.driver.find_element(By.XPATH, "//a[normalize-space()='Logout']").click()
        time.sleep(2)
        #Validate Logout Success
        result = self.driver.find_element(By.ID, "btn-make-appointment").text
        assert("Make Appointment") in result 
        
    def tearDown(self):
        # Close Webdriver Session
        self.driver.close()

if __name__ == "__main__":
    unittest.main(unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='ReportLoginLogout')))