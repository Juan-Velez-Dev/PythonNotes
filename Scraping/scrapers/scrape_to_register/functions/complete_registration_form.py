"""
"""

import os
import logging

from dotenv import load_dotenv
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By

from scrapers.scrape_to_register.errors.exception_error import register_error_handler


load_dotenv()

api_web = os.getenv("RUTE_TO_CREATE_ACCOUNT")


async def complete_registration_form(driver: WebDriver, url):
    driver.get(url)
    first_name_input = driver.find_element(
        By.XPATH, "//input[@id='firstname']")
    first_name_input.send_keys("Juanito")
    middlename_input = driver.find_element(
        By.XPATH, "//input[@id='middlename']")
    middlename_input.send_keys("Velez")
