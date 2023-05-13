import inspect
import logging
import time
import datetime
from time import strftime

from selenium.common import TimeoutException
from selenium.webdriver.support.select import Select

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

#from pageObject.confirm import confirm


@pytest.mark.usefixtures("setup")
class BaseClass:
    def get_logger(self):
        loggername = inspect.stack()[1][3]  # enables to print from the test which this method is called in output.
        logger = logging.getLogger(loggername)  # created an object from logging class

        #filehandler = logging.FileHandler(strftime("orange_hrm_%H_%M_%m_%d_%Y.log"))  # passing the file location. Here a file is created with logfile.log name and all logs will be sent there.
        filehandler = logging.FileHandler(strftime(r"C:\Users\Lenovo\PycharmProjects\itero_project\ptests\testcase_logs\itero_test_%Y%m%d_%H%M.log"))
        formatter = logging.Formatter("%(asctime)s :%(levelname)s :%(name)s :%(message)s")
        filehandler.setFormatter(formatter)  # Conneting formatting and file handling
        logger.addHandler(
            filehandler)  # There is a other class called file handler we have to pass file handler object to it
        # In above statement logger is asking information about in which file i have to print and what is the format
        # File handler is nothing but the file location
        # File location will come from parent loging not the object
        logger.setLevel(logging.DEBUG)
        return logger



    def verify_element_presence(self, element):

        wait = WebDriverWait(self.driver,50)
        wait.until(expected_conditions.presence_of_element_located((By.XPATH, element)))
        self.driver.find_element(By.XPATH, element)
        return self.driver.find_element(By.XPATH, element).get_attribute("innerHTML")

    def verify_element_absence(self,element):

        wait=WebDriverWait(self.driver,25)
        wait.until_not(expected_conditions.presence_of_element_located((By.XPATH,element)))
        self.driver.find_element(By.XPATH,element)










    def verify_element_clickable(self, element):
        wait1 = WebDriverWait(self.driver,5)
        wait1.until(expected_conditions.element_to_be_clickable((By.XPATH, element)))

    def select_option_by_text(self,locator,text,index):
        drop = Select(locator)
        drop.select_by_visible_text(text)
        drop.select_by_index(index)