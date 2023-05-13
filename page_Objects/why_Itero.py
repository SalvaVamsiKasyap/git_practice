from selenium.webdriver.common.by import By
from page_Objects.succes_Stories_Page import success_Stories_Page

class why_Itero():

    def __init__(self, driver):

        self.driver = driver

    success_Stories_Button = (By.XPATH,"//a[text()='View success stories']")

    def clicking_successstoriesbutton(self):

        self.driver.find_element(*why_Itero.success_Stories_Button).click()

        return success_Stories_Page(self.driver)