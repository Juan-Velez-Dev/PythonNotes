import os

from dotenv import load_dotenv
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By


load_dotenv()

api_web = os.getenv("RUTE_TO_REGISTER_FORM")


async def navigate_to_register_form(driver: WebDriver):
    """
    proceso para ingresar al formulario de registro
    retorna la URL del formulario
    """
    driver.get(api_web)
    account = driver.find_element(
        By.XPATH, '//span[contains(text(), "Account")]')
    account.click()
    register = driver.find_element(
        By.XPATH, '//li/a[@title="Register"]')
    register.click()
    currten_url = driver.current_url
    return currten_url
