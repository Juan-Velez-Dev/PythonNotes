"""
Scraping en airbnb
"""

from time import sleep

import logging

import os

from selenium import webdriver  # Ayuda a utilizar el navegador
# common expression para poder usar XPATH en la busqueda
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.common.exceptions import WebDriverException
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager


from Functions import register
from Errors import login_errors, exception_error


opts = Options()
# opts.add_argument("--headless")
logging.basicConfig(level=logging.DEBUG)

"""
"""
############################################################################################################################################


############################################################################################################################################
def initialize_driver():
    """
    """
    try:
        driver = webdriver.Chrome(service=ChromeService(
            ChromeDriverManager().install()),
            options=opts)
        return driver
    except WebDriverException as e:
        print("Error al inicializar el navegador : ", e)
        logging.critical("Error al inicializar el navegador")
        return None


############################################################################################################################################
def scrape_product_names(drivers):
    """
    """
    try:
        drivers.get('http://demo-store.seleniumacademy.com/')
        products = drivers.find_elements(
            By.XPATH, '//h3[contains(@class, "product-name")]')
        if not products:
            print('No se encontraron productos con la clase "product-name"')
            logging.warning(
                'No se encontraron productos con la clase "product-name"')
        else:
            return products
    except Exception as e:
        exception_error(e)


def scrape_to_register(driver: WebDriver):
    try:
        register.form_access_handler(driver)
    except NoSuchElementException:
        login_errors.login_error_handler()
    except Exception as e:
        exception_error(e)


def main():
    try:
        driver = initialize_driver()
        product_list = []
        if driver:
            products = scrape_product_names(driver)
            for product in products:
                product_list.append(product.text)
            scrape_to_register(driver)
            sleep(3)
            driver.quit()
        else:
            print("El driver no inicializo")
        print(product_list)
    except Exception as e:
        print("Error: ", e)
        logging.critical("Se produjo un error durante la ejecucion")


if __name__ == "__main__":
    main()
