"""
"""

import logging


def navigate_to_register_error_message(e):
    """
    manejador de errores al momento de registrarnos
    """
    print("#" * 120 + "\n")
    print("Error al navegar al formulario de registro : " + str(e))
    logging.error(
        'Ha ocurrido algun error con los elementos que se buscan, para acceder al formulario de registro')
    print("#" * 120 + "\n")


def complete_form_error_message(e):
    """
    manejador de errores al momento de registrarnos
    """
    print("#" * 120 + "\n")
    print("Error al llenar el formulario de registro :  " + str(e))
    logging.error(
        'Ha ocurrido algun error con los elementos que se buscan, para llenar al formulario de registro')
    print("#" * 120 + "\n")
