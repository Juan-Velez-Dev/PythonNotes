"""
"""

import logging


def exception_error_handler(e):
    """
    manejador de errores generales del scraper
    """
    print("Error : Durante el scraping de los nombres del producto: " + str(e))
    logging.critical("Ocurrio un error durante el scraping")
