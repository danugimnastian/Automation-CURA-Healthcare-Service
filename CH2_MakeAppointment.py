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


class MakeAppointment(unittest.TestCase):
    
    def setUp(self):
        self.driver = webdriver.Chrome(options=options)

    def testMakeAppointmentSuccess(self):
        MakeAppointmentData.MakeAppointmentSuccess(self.driver)
        time.sleep(1)
        #Book Appointment
        self.driver.find_element(By.ID, "btn-book-appointment").click()
        time.sleep(2)
        #Go to HomePage
        self.driver.find_element(By.XPATH, "//a[@class='btn btn-default']").click()
        time.sleep(1)
        #Validate Make Appointment Success
        result = self.driver.find_element(By.XPATH, "//h1[normalize-space()='CURA Healthcare Service']").text
        assert("CURA") in result

    def testMakeAppointmentFailed(self):
        #Login Success
        LoginData.LoginSuccess(self.driver)
        time.sleep(1)
        #Click Login
        self.driver.find_element(By.ID, "btn-login").click()
        time.sleep(3)
        #Book Appointment
        self.driver.find_element(By.ID, "btn-book-appointment").click()
        time.sleep(2)
        #Validate Make Appointment Failed
        result = self.driver.find_element(By.XPATH, "//label[normalize-space()='Visit Date (Required)']").text
        assert("Visit Date (Required)") in result        

    def tearDown(self):
        # Close Webdriver Session
        self.driver.close()

if __name__ == "__main__":
    unittest.main(unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='ReportMakeAppointment')))