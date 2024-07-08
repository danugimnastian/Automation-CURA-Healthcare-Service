import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import LoginData
import MakeAppointmentData
import HtmlTestRunner

options = Options()

options.add_experimental_option("excludeSwitches", ["enable-logging"])


class HistoryCheck(unittest.TestCase):
    
    def setUp(self):
        self.driver = webdriver.Chrome(options=options)

    def testHistoryCheck(self):
        MakeAppointmentData.MakeAppointmentSuccess(self.driver)
        time.sleep(1)
        #Book Appointment
        self.driver.find_element(By.ID, "btn-book-appointment").click()
        time.sleep(2)
        #Click Burger Bar
        self.driver.find_element(By.XPATH,"//i[@class='fa fa-bars']").click()
        time.sleep(2)
        #History Check 
        self.driver.find_element(By.XPATH, "//a[normalize-space()='History']").click()
        time.sleep(2)
        #Validate History Check Success
        result = self.driver.find_element(By.XPATH, "//h2[normalize-space()='History']").text
        assert("History") in result

    def testHistoryEmpty(self):
        #Login with Empty Data
        LoginData.LoginSuccess(self.driver)
        time.sleep(1)
        #Click Login
        self.driver.find_element(By.ID, "btn-login").click()    
        time.sleep(3)
        #Click Burger Bar
        self.driver.find_element(By.XPATH,"//i[@class='fa fa-bars']").click()
        time.sleep(2)
        #History Check 
        self.driver.find_element(By.XPATH, "//a[normalize-space()='History']").click()
        time.sleep(2)
        #Validate History is Empty
        result = self.driver.find_element(By.XPATH, "//p[normalize-space()='No appointment.']").text
        assert("No appointment") in result      

    def tearDown(self):
        # Close Webdriver Session
        self.driver.close()

if __name__ == "__main__":
    unittest.main(unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='ReportHistoryCheck')))