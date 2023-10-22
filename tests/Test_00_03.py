import time

from selenium import webdriver
from bacic_.cartPage import CartPage
from bacic_.loginpage import LoginPage
from bacic_.navigationBar import NavigationBar



driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.maximize_window()

driver.get("https://www.amazon.com/ap/signin?openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon.com%2F%3Fref_%3Dnav_ya_signin&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.assoc_handle=usflex&openid.mode=checkid_setup&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0")

loginPageObj = LoginPage(driver)
loginPageObj.fill_username_field("lilmankan@gmail.com")

loginPageObj.click_to_continue_button()
loginPageObj.fill_password_field("amazonlilit2023@")
time.sleep(5)
loginPageObj.click_to_signin_button()

navigationBarObj = NavigationBar(driver)
navigationBarObj.click_to_cart_button()

cartPageObj = CartPage(driver)
cartPageObj.delete_firstProduct_from_cart()
time.sleep(20)


driver.close()



