from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.opera import OperaDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
import requests
import time
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.edge.service import Service as EdgeService
import datetime
from selenium.webdriver.chrome.options import Options

now = datetime.datetime.now()

timestamp = now.strftime('%Y-%m-%d %H:%M:%S')


def itero_success_stories():
    chrome_options = Options()
    chrome_options.binary_location = '/usr/bin/google-chrome'
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--enable-logging')
    chromedriver_binary_path = '/usr/bin/google-chrome'
    chrome_options.add_argument('--disable-gpu')
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()),options=chrome_options)
    #driver = webdriver.Firefox(GeckoDriverManager().install())
    #driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
    #driver = webdriver.Opera(OperaDriverManager().install())
    #time.sleep(10)
    print(driver)
    #driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))
    response = requests.head("https://itero.com/en-APAC")
    response = str(response)[11:14]
    if response == '200':
        driver.get("https://itero.com/en-APAC")
        driver.maximize_window()
        time.sleep(5)
        #assert driver.title == "iTero - Intraoral Scanners for Dental, Restorative & Orthondontic Work"
        #driver.find_element(By.XPATH,"//div[@class='modal-content']/div[2]/span").click()
        #time.sleep(5)
        #driver.find_element(By.XPATH,"//div[@class='TopNavigation_links__SM670']/a[text()='Why iTero']").click()
        #time.sleep(5)
        #assert driver.title == "Discover the efficiency of digital dentistry | iTero intraoral scanner"
        #driver.find_element(By.XPATH,"//a[text()='View success stories']").click()
        #time.sleep(5)
        #assert driver.title == "Testimonials | iTero"
    #     time.sleep(5)
    #     driver.find_element(By.XPATH,"//a[text()='Orthodontic']").click()
    #     time.sleep(5)
    #     driver.execute_script("arguments[0].scrollIntoView();",
    #                           driver.find_element(By.XPATH, '//div[@class="tab-buttons-layout"]'))
    #     testimonals = []
    #     testimonals = driver.find_elements(By.XPATH,"//div[text()='orthodontic']/preceding-sibling::div/p")
    #     for ele in testimonals:
    #         print(ele.text)
    # else:
    #     print("Web page is not accessible")

itero_success_stories()
