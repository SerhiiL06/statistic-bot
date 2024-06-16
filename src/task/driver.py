from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


class Driver:

    def __init__(self, options: Options, service: Service) -> None:
        self._options = options
        self._service = service
        self._options.add_argument("--no-sandbox")
        self._options.add_argument("--disable-gpu")
        self._options.add_argument("--headless")

    @property
    def instance(self):
        return webdriver.Chrome(self._options, self._service)


driver = Driver(Options(), Service())
