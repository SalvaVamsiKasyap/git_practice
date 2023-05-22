from selenium.webdriver.common.by import By

class success_Stories_Page():

    def __init__(self,driver):

        self.driver = driver

    segment_Button = (By.XPATH,"//nav/a")
    testimonals = (By.XPATH,'//div[@class="fade tab-pane active show"]/div/div/div/div/div[@class="videoPreview_descriptionWrapper__78IlX"]/div/p')


    def clicking_segment_button(self):

        segment_Option = self.driver.find_elements(*success_Stories_Page.segment_Button)
        def fetch_seg_stories(option):

            option.click()
            avaliable_testimonals = self.driver.find_elements(*success_Stories_Page.testimonals)
            testimonals_text = []
            for each in avaliable_testimonals:
                testimonals_text.append(each.text)
            return testimonals_text

        return list(map(fetch_seg_stories,segment_Option))




