from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver  # Ayuda a utilizar el navegador
from selenium.common.exceptions import WebDriverException
import logging
from selenium.webdriver.chrome.service import Service as ChromeService


from selenium.webdriver.chrome.options import Options

opts = Options()
opts.add_argument("--headless")
logging.basicConfig(level=logging.INFO)
# logging.basicConfig(level=logging.DEBUG)


async def initialize_driver():
    """
    configuracion e inicializacion del driver
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
