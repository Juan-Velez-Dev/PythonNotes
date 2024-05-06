"""
Proceso para scrapear una web y resgistrarme con diferentes usuarios
"""

from time import sleep

import asyncio
import logging
# from selenium.webdriver.remote.webdriver import WebDrive
from initialize_driver import initialize_driver
from scrapers.scrape_to_register.scrape_register import scrape_to_register


async def main():
    """
    separe todo el codigo en diferentes funciones
    con una estructura de carpetas facil de entender

    esto permite optimizar el momento de debuggear el codigo
    usando diferentes metodos para manejar errores e identificar el problema con mayor rapidez

    al separar el codigo tambien mejora su escalabilidad y comprension del mismo
    permitiendo al codigo ser manejable para cualquier persona e implementar mejoras con mucha mas facilidad
    """
    try:
        driver = await initialize_driver()
        await scrape_to_register(driver)
        sleep(3)
        driver.quit()
    except Exception as e:
        print("Error: ", e)
        logging.critical("Se produjo un error durante la ejecucion")


if __name__ == "__main__":
    asyncio.run(main())


############################ FUNCIONES DE TESTEO ############################


# def scrape_product_names(drivers):
#     """
#     """
#     try:
#         drivers.get('http://demo-store.seleniumacademy.com/')
#         products = drivers.find_elements(
#             By.XPATH, '//h3[contains(@class, "product-name")]')
#         if not products:
#             print('No se encontraron productos con la clase "product-name"')
#             logging.warning(
#                 'No se encontraron productos con la clase "product-name"')
#         else:
#             return products
#     except Exception as e:
#         print("Error :" + e)
