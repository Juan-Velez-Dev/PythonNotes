"""
"""
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.common.exceptions import NoSuchElementException
from scrapers.scrape_to_register.errors.exception_error import exception_error_handler
from scrapers.scrape_to_register.errors.register_errors import register_error_handler
from scrapers.scrape_to_register.functions.go_to_register_form import go_to_register_form


def scrape_to_register(driver: WebDriver):
    """
    scraper que hace todo el proceso de registro en la web:
    navegacion, relleno de formularios
    """
    try:
        go_to_register_form(driver)
    except NoSuchElementException:
        register_error_handler()
    except Exception as e:
        exception_error_handler(e)
