from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By


def form_access_handler(driver: WebDriver):
    driver.get('http://demo-store.seleniumacademy.com/')
    account = driver.find_element(
        By.XPATH, '//span[contains(text(), "Account")]')
    account.click()
    register = driver.find_element(
        By.XPATH, '//li/a[@title="Register"]')
    register.click()
