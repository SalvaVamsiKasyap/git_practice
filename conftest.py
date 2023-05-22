import pytest
from time import sleep
import requests
from _pytest.config import Config
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.edge.service import Service as EdgeService
from utilities.BaseClass import BaseClass
import datetime
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox.options import Options
import os




now = datetime.datetime.now()

instance = BaseClass()
log = instance.get_logger()

def pytest_addoption(parser):
    parser.addoption(
        "--browser_Name", action="store", default="chrome")


@pytest.fixture(scope="class")

def setup(request):
    """This is used to do cross browser testing at run time"""
    log.info(f"{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')} Entered in to setup fixture")
    browser_Name = request.config.getoption("browser_Name")
    response = requests.head("https://itero.com/en-APAC")
    response = str(response)[11:14]
    log.info(f"I can access webpage and the reponse is {response}")
    if browser_Name == "chrome" and response == '200':
        log.info(f"{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')} Successfully Chosen chrome browser")
        chrome_options = Options()
        chrome_options.binary_location = '/usr/bin/google-chrome'
        chrome_options.add_argument("--disable-gpu")
        chrome_options.headless = True
        driver_path = ChromeDriverManager(version='113.0.5672.24').install()
        os.chmod(driver_path, 0o777)
        driver = webdriver.Chrome(executable_path=driver_path,options=chrome_options)
        log.info(f"{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')} Successfully downloaded latest version of chrome driver {driver}")
    elif browser_Name == "firefox" and response == '200':
        firefox_options = Options()
        firefox_options.add_argument("--headless")
        log.info(f"{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')} Successfully Chosen firefox browser")
        driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()),options=firefox_options)
        time.sleep(25)
        log.info(f"{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')} Successfully downloaded latest version of firefox driver {driver}")
    elif browser_Name == "edge" and response == '200':
        log.info(f"{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')} Successfully Chosen edge browser")
        driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))
        log.info(f"{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')} Successfully downloaded latest version of edge driver {driver}")
    driver.get("https://itero.com/en-APAC")
    driver.maximize_window()
    request.cls.driver = driver
    yield
    driver.close()

