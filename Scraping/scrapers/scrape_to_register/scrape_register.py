"""
"""
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.common.exceptions import NoSuchElementException
from scrapers.scrape_to_register.errors.exception_error import register_error_handler
from scrapers.scrape_to_register.errors.register_errors import navigate_to_register_error_message, complete_form_error_message
from scrapers.scrape_to_register.functions.navigate_to_register_form import navigate_to_register_form
from scrapers.scrape_to_register.functions.complete_registration_form import complete_registration_form


async def scrape_to_register(driver: WebDriver):
    """
    scraper que hace todo el proceso de registro en la web:
    navegacion, relleno de formularios
    """
    try:
        try:
            current_url = await navigate_to_register_form(driver)
        except NoSuchElementException as e:
            navigate_to_register_error_message(e)
        try:
            await complete_registration_form(driver, current_url)
        except NoSuchElementException as e:
            complete_form_error_message(e)
    except Exception as e:
        register_error_handler(e)
