# File: src/automated_testing/test_login.py

import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginTest(unittest.TestCase):
    LOGIN_URL = "https://the-internet.herokuapp.com/login"
    VALID_USER = "tomsmith"
    VALID_PASS = "SuperSecretPassword!"
    INVALID_USER = "wrong_user"
    INVALID_PASS = "wrong_pass"

    def setUp(self):
        # Make sure you have the matching ChromeDriver for your Chrome version on PATH
        self.driver = webdriver.Chrome()
        self.wait = WebDriverWait(self.driver, 10)
        self.driver.get(self.LOGIN_URL)

    def test_valid_login(self):
        d = self.driver
        # Wait for username field
        self.wait.until(EC.presence_of_element_located((By.ID, "username")))
        d.find_element(By.ID, "username").send_keys(self.VALID_USER)
        d.find_element(By.ID, "password").send_keys(self.VALID_PASS)
        d.find_element(By.CSS_SELECTOR, "button.radius").click()

        # Wait for success flash
        flash = self.wait.until(EC.visibility_of_element_located((By.ID, "flash")))
        self.assertIn("You logged into a secure area!", flash.text)

    def test_invalid_login(self):
        d = self.driver
        self.wait.until(EC.presence_of_element_located((By.ID, "username")))
        d.find_element(By.ID, "username").send_keys(self.INVALID_USER)
        d.find_element(By.ID, "password").send_keys(self.INVALID_PASS)
        d.find_element(By.CSS_SELECTOR, "button.radius").click()

        # Wait for error flash
        flash = self.wait.until(EC.visibility_of_element_located((By.ID, "flash")))
        self.assertIn("Your username is invalid!", flash.text)

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
