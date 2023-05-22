from selenium.webdriver.common.by import By
from page_Objects.why_Itero import why_Itero

class home_Page():

    def __init__(self,driver):

        self.driver = driver
    discliamer_acceptance = (By.XPATH,"//div[@class='modal-content']/div[2]/span")
    why_itero_option = (By.XPATH,"//div[@class='TopNavigation_links__SM670']/a[text()='Why iTero']")

    def accepting_disclaimer(self):

        self.driver.find_element(*home_Page.discliamer_acceptance).click()

    def choosing_iteroOption(self):

        self.driver.find_element(*home_Page.why_itero_option).click()

        return why_Itero(self.driver)
