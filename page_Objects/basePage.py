from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utilities.BaseClass import BaseClass
import datetime

now = datetime.datetime.now()

timestamp = now.strftime('%Y-%m-%d %H:%M:%S')


"""This class 
 the parent of all pages"""
"""It contains all the generic methods and utilities for all the pages"""

class BasePage(BaseClass):


    def __init__(self,driver):

        self.driver = driver

    def do_click(self,by_locator):
        log = self.get_logger()
        log.debug(f"{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')} The element present in by_locator variable is {by_locator}")
        WebDriverWait(self.driver,10).until(EC.visibility_of_element_located(by_locator)).click()

    def do_click_collection(self, by_locator):
        log = self.get_logger()
        log.debug(
             f"{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')} The elements present in by_locator variable are {by_locator}")
        elements = WebDriverWait(self.driver, 10).until(EC.visibility_of_all_elements_located(by_locator))
        for element in elements:
            element.click()
        return elements

    def do_send_keys(self,by_locator,text):

        WebDriverWait(self.driver,10).until(EC.visibility_of_element_located(by_locator)).send_keys(text)

    def get_element_text(self,by_locator):

        element = WebDriverWait(self.driver,10).until(EC.visibility_of_element_located(by_locator))
        return element.text

    def is_enabled(self,by_locator):

        element = WebDriverWait(self.driver,10).until(EC.visibility_of_element_located(by_locator))
        return bool(element)

    def get_title(self,title):

        WebDriverWait(self.driver,10).until(EC.title_is(title))
        return self.driver.title

    def click_element(self,by_locator):

        element = WebDriverWait(self.driver,10).until(EC.element_to_be_clickable(by_locator))
        return bool(element)

    def get_collection(self,by_locator):

        elements = WebDriverWait(self.driver, 10).until(EC.visibility_of_all_elements_located(by_locator))
        return elements