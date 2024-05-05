"""
"""

import logging


def register_error_handler():
    """
    manejador de errores al momento de registrarnos
    """
    print("#" * 120 + "\n")
    print("Error al logearse : ")
    logging.error(
        'Ha ocurrido algun error con los elementos que se buscan, cambiaron su nombre la logica ahora no funciona')
    print("#" * 120 + "\n")
