from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By


def go_to_register_form(driver: WebDriver):
    """
    proceso para ingresar al formulario de registro
    """
    driver.get('http://demo-store.seleniumacademy.com/')
    account = driver.find_element(
        By.XPATH, '//span[contains(text(), "Account")]')
    account.click()
    register = driver.find_element(
        By.XPATH, '//li/a[@title="Register"]')
    register.click()


def fill_register_form():
    pass
