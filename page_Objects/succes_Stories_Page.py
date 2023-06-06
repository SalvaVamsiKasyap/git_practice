from selenium.webdriver.common.by import By
from page_Objects.basePage import BasePage

class success_Stories_Page(BasePage):

    segment_Button = (By.XPATH, "//nav/a")
    testimonals = (By.XPATH,
                   '//div[@class="fade tab-pane active show"]/div/div/div/div/div[@class="videoPreview_descriptionWrapper__78IlX"]/div/p')
    def __init__(self,driver):

        self.driver = driver




    def clicking_segment_button(self):

        segment_Option = self.get_collection(self.segment_Button)
        segment_name = ""
        result = []
        for option in segment_Option:

            option.click()
            available_testimonals = self.get_collection(self.testimonals)
            container = []
            for text in available_testimonals:
                container.append(text.text)
            segment_name = option.text
            result.append(f"{segment_name} : {container}")
        return result



