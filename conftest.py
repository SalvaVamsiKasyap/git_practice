# import pytest
# from time import sleep
# import requests
# from _pytest.config import Config
# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support import expected_conditions
# from selenium.webdriver.support.wait import WebDriverWait
# from webdriver_manager.chrome import ChromeDriverManager
# from webdriver_manager.firefox import GeckoDriverManager
# from webdriver_manager.microsoft import EdgeChromiumDriverManager
# from selenium.webdriver.chrome.service import Service as ChromeService
# from selenium.webdriver.firefox.service import Service as FirefoxService
# from selenium.webdriver.edge.service import Service as EdgeService
# from utilities.BaseClass import BaseClass
# import datetime
# from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.firefox.options import Options
# import os
#
#
#
#
# now = datetime.datetime.now()
#
# instance = BaseClass()
# log = instance.get_logger()
#
# def pytest_addoption(parser):
#     parser.addoption(
#         "--browser_Name", action="store", default="chrome")
#

# @pytest.fixture(scope="class")
#
# def setup(request):
#     """This is used to do cross browser testing at run timessssssss"""
#     log.info(f"{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')} Entered in to setup fixture")
#     browser_Name = request.config.getoption("browser_Name")
#     response = requests.head("https://itero.com/en-APAC")
#     response = str(response)[11:14]
#     log.info(f"I can access webpage and the reponse is {response}")
#     if browser_Name == "chrome" and response == '200':
#         log.info(f"{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')} Successfully Chosen chrome browser")
#         driver = webdriver.Chrome(ChromeDriverManager().install())
#         log.info(f"{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')} Successfully downloaded latest version of chrome driver {driver}")
#     elif browser_Name == "firefox" and response == '200':
#         firefox_options = Options()
#         firefox_options.add_argument("--headless")
#         log.info(f"{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')} Successfully Chosen firefox browser")
#         driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()),options=firefox_options)
#         log.info(f"{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')} Successfully downloaded latest version of firefox driver {driver}")
#     elif browser_Name == "edge" and response == '200':
#         log.info(f"{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')} Successfully Chosen edge browser")
#         driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))
#         log.info(f"{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')} Successfully downloaded latest version of edge driver {driver}")
#     driver.get("https://itero.com/en-APAC")
#     driver.maximize_window()
#     request.cls.driver = driver
#     yield
#     driver.close()

#Single responsblity model

# import datetime
# import requests
# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service as ChromeService
# from selenium.webdriver.firefox.options import Options as FirefoxOptions
# from selenium.webdriver.firefox.service import Service as FirefoxService
# from selenium.webdriver.edge.service import Service as EdgeService
# from webdriver_manager.chrome import ChromeDriverManager
# from webdriver_manager.firefox import GeckoDriverManager
# from webdriver_manager.microsoft import EdgeChromiumDriverManager
# from utilities.BaseClass import BaseClass
# import pytest
#
# now = datetime.datetime.now()
#
# instance = BaseClass()
# log = instance.get_logger()
#
# def pytest_addoption(parser):
#     parser.addoption(
#         "--browser_Name", action="store", default="chrome")
#
#
#
# @pytest.fixture(scope="class")
# def setup(request):
#     """This is used to do cross-browser testing at runtime"""
#     log_info("Entered into setup fixture")
#
#     browser_name = request.config.getoption("browser_Name")
#     response = get_response_code("https://itero.com/en-APAC")
#
#     if browser_name == "chrome" and response == 200:
#         log_info("Successfully chosen chrome browser")
#         driver = get_chrome_driver()
#     elif browser_name == "firefox" and response == 200:
#         log_info("Successfully chosen firefox browser")
#         driver = get_firefox_driver()
#     elif browser_name == "edge" and response == 200:
#         log_info("Successfully chosen edge browser")
#         driver = get_edge_driver()
#     else:
#         raise ValueError("Invalid browser_Name or unable to access the webpage")
#
#     driver.get("https://itero.com/en-APAC")
#     driver.maximize_window()
#     request.cls.driver = driver
#     yield
#     driver.quit()
#
#
# def log_info(message):
#     """Logs an informational message"""
#     current_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')
#     log.info(f"{current_time} {message}")
#
#
# def get_response_code(url):
#     """Gets the response code for the given URL"""
#     response = requests.head(url)
#     return response.status_code
#
#
# def get_chrome_driver():
#     """Returns the Chrome driver instance"""
#     driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
#     log_info(f"Successfully downloaded latest version of Chrome driver {driver}")
#     return driver
#
#
# def get_firefox_driver():
#     """Returns the Firefox driver instance"""
#     options = FirefoxOptions()
#     options.add_argument("--headless")
#     driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()), options=options)
#     log_info(f"Successfully downloaded latest version of Firefox driver {driver}")
#     return driver
#
#
# def get_edge_driver():
#     """Returns the Edge driver instance"""
#     driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))
#     log_info(f"Successfully downloaded latest version of Edge driver {driver}")
#     return driver
#

#Openclosed Principle

# import datetime
# import requests
# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service as ChromeService
# from selenium.webdriver.firefox.options import Options as FirefoxOptions
# from selenium.webdriver.firefox.service import Service as FirefoxService
# from selenium.webdriver.edge.service import Service as EdgeService
# from webdriver_manager.chrome import ChromeDriverManager
# from webdriver_manager.firefox import GeckoDriverManager
# from webdriver_manager.microsoft import EdgeChromiumDriverManager
# import pytest
# from utilities.BaseClass import BaseClass
#
# now = datetime.datetime.now()
#
# instance = BaseClass()
# log = instance.get_logger()
#
# def pytest_addoption(parser):
#     parser.addoption(
#         "--browser_Name", action="store", default="chrome")
#
#
# class DriverFactory:
#     @staticmethod
#     def create_driver(browser_name):
#         if browser_name == "chrome":
#             return get_chrome_driver()
#         elif browser_name == "firefox":
#             return get_firefox_driver()
#         elif browser_name == "edge":
#             return get_edge_driver()
#         else:
#             raise ValueError("Invalid browser_Name")
#
# @pytest.fixture(scope="class")
# def setup(request):
#     """This is used to do cross-browser testing at runtime"""
#     log_info("Entered into setup fixture")
#
#     browser_name = request.config.getoption("browser_Name")
#     response = get_response_code("https://itero.com/en-APAC")
#
#     if response != 200:
#         raise ValueError("Unable to access the webpage")
#
#     driver = DriverFactory.create_driver(browser_name)
#     driver.get("https://itero.com/en-APAC")
#     driver.maximize_window()
#     request.cls.driver = driver
#     yield
#     driver.quit()
#
# def log_info(message):
#     """Logs an informational message"""
#     current_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')
#     log.info(f"{current_time} {message}")
#
# def get_response_code(url):
#     """Gets the response code for the given URL"""
#     response = requests.head(url)
#     return response.status_code
#
# def get_chrome_driver():
#     """Returns the Chrome driver instance"""
#     driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
#     log_info(f"Successfully downloaded latest version of Chrome driver {driver}")
#     return driver
#
# def get_firefox_driver():
#     """Returns the Firefox driver instance"""
#     options = FirefoxOptions()
#     options.add_argument("--headless")
#     driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()), options=options)
#     log_info(f"Successfully downloaded latest version of Firefox driver {driver}")
#     return driver
#
# def get_edge_driver():
#     """Returns the Edge driver instance"""
#     driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))
#     log_info(f"Successfully downloaded latest version of Edge driver {driver}")
#     return driver
#

#Liskov Substitution principle

import datetime
import requests
from abc import ABC, abstractmethod
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
import pytest
from utilities.BaseClass import BaseClass

now = datetime.datetime.now()

instance = BaseClass()
log = instance.get_logger()

def pytest_addoption(parser):
    parser.addoption(
        "--browser_Name", action="store", default="chrome")


class DriverFactory(ABC):
    @abstractmethod
    def create_driver(self):
        pass

class ChromeDriverFactory(DriverFactory):
    def create_driver(self):
        return get_chrome_driver()

class FirefoxDriverFactory(DriverFactory):
    def create_driver(self):
        return get_firefox_driver()

class EdgeDriverFactory(DriverFactory):
    def create_driver(self):
        return get_edge_driver()

@pytest.fixture(scope="class")
def setup(request):
    """This is used to do cross-browser testing at runtime"""
    log_info("Entered into setup fixture")

    browser_name = request.config.getoption("browser_Name")
    response = get_response_code("https://itero.com/en-APAC")

    if response != 200:
        raise ValueError("Unable to access the webpage")

    factory = None

    if browser_name == "chrome":
        factory = ChromeDriverFactory()
    elif browser_name == "firefox":
        factory = FirefoxDriverFactory()
    elif browser_name == "edge":
        factory = EdgeDriverFactory()
    else:
        raise ValueError("Invalid browser_Name")

    driver = factory.create_driver()
    driver.get("https://itero.com/en-APAC")
    driver.maximize_window()
    request.cls.driver = driver
    yield
    driver.quit()

def log_info(message):
    """Logs an informational message"""
    current_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')
    log.info(f"{current_time} {message}")

def get_response_code(url):
    """Gets the response code for the given URL"""
    response = requests.head(url)
    return response.status_code

def get_chrome_driver():
    """Returns the Chrome driver instance"""
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    log_info(f"Successfully downloaded latest version of Chrome driver {driver}")
    return driver

def get_firefox_driver():
    """Returns the Firefox driver instance"""
    options = FirefoxOptions()
    options.add_argument("--headless")
    driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()), options=options)
    log_info(f"Successfully downloaded latest version of Firefox driver {driver}")
    return driver

def get_edge_driver():
    """Returns the Edge driver instance"""
    driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))
    log_info(f"Successfully downloaded latest version of Edge driver {driver}")
    return driver
