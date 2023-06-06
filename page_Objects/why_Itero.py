from selenium.webdriver.common.by import By
from page_Objects.succes_Stories_Page import success_Stories_Page
from page_Objects.basePage import BasePage

class why_Itero(BasePage):

    success_Stories_Button = (By.XPATH, "//a[text()='View success stories']")
    def __init__(self, driver):

        self.driver = driver



    def clicking_successstoriesbutton(self):

        #self.driver.find_element(*why_Itero.success_Stories_Button).click()
        self.do_click(self.success_Stories_Button)

        return success_Stories_Page(self.driver)