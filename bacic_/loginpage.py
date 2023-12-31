from selenium.webdriver.common.by import By
from selenium import webdriver
import time
from bacic_.bacePage import BasePage



class LoginPage(BasePage):
    def __init__(self, driver: webdriver):
        self.driver = driver
        pass
    def fill_username_field(self, username):
        #userNameFieldElement = self.driver.find_element(By.ID, "ap_email")
        userNameFieldElement = self._find_element(By.ID, "ap_email")
        self._fill_field(userNameFieldElement, username)
        #userNameFieldElement.clear()
        #userNameFieldElement.send_keys(username)

    def click_to_continue_button(self):
        #continueButtonElement = self.driver.find_element(By.ID, "continue")
        continueButtonElement = self._find_element(By.ID, "continue")
        self._click(continueButtonElement)
        #continueButtonElement.click()

    def fill_password_field(self, password):
        #passwordFieldElement = self.driver.find_element(By.ID, "ap_password")
        passwordFieldElement = self._find_element(By.ID, "ap_password")
        self._fill_field(passwordFieldElement, password)
        #passwordFieldElement.clear()
        #passwordFieldElement.send_keys(password)


    def click_to_signin_button(self):
        time.sleep(10)
        #signinButtonElement = self.driver.find_element(By.ID, "signInSubmit")
        signinButtonElement = self._find_element(By.ID, "signInSubmit")
        self._click(signinButtonElement)
        #signinButtonElement.click()
        time.sleep(10)
