"""
"""

import logging


def register_error_handler(e):
    """
    manejador de errores generales del scraper
    """
    print("Error : Durante el scraping de registro: " + str(e))
    logging.critical("Ocurrio un error durante el scraping de registro")
