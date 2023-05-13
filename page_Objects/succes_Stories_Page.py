from selenium.webdriver.common.by import By

class success_Stories_Page():

    def __init__(self,driver):

        self.driver = driver

    orthodontic_button = (By.XPATH,"//a[text()='Orthodontic']")
    testimonals = (By.XPATH,"//div[text()='orthodontic']/preceding-sibling::div/p")

    def clicking_orthodontics_button(self):

        self.driver.find_element(*success_Stories_Page.orthodontic_button).click()

    def displaying_testimonals(self):

        testimonals = []
        actual_testimonals = []
        testimonals = self.driver.find_elements(*success_Stories_Page.testimonals)
        for name in testimonals:
            actual_testimonals.append(name.text)
        return actual_testimonals