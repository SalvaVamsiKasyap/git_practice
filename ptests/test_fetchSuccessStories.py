from utilities.BaseClass import BaseClass
import pytest
from page_Objects.home_Page import home_Page



@pytest.mark.usefixtures("setup")
class Test_fetchSuccessStories(BaseClass):

    def test_fetchsucessstories(self):

        log = self.get_logger()
        log.info("Entering home page..")
        hom_pag = home_Page(self.driver)
        log.info("Checking whether the acceptance button for the disclaimer is fully rendered to click")
        self.verify_element_clickable("//div[@class='modal-content']/div[2]/span")
        log.info("Clicking on acceptance button")
        hom_pag.accepting_disclaimer()
        log.info("Successfully accepted the acceptance button")
        log.info("Checking whether the WHY ITERO button fully rendered to click")
        self.verify_element_clickable("//div[@class='TopNavigation_links__SM670']/a[text()='Why iTero']")
        why_iter = hom_pag.choosing_iteroOption()
        log.info("Checking whether the SUCCESS STORIES button fully rendered to click")
        self.verify_element_clickable("//a[text()='View success stories']")
        log.info("Successfully choosen WHY ITERO option")
        success_Stories = why_iter.clicking_successstoriesbutton()
        log.info("Clicked view success stories button")
        log.info("Waiting for the rendering of Orthodontics option")
        self.verify_element_clickable("//a[text()='Orthodontic']")
        success_Stories.clicking_orthodontics_button()
        log.info("Successfully clicked on orthodontics option")
        log.info("Waiting for the appearence of testimonals under Orthodontic option")
        self.verify_element_presence("//div[text()='orthodontic']/preceding-sibling::div/p")
        log.info(f"These are our testimonals{success_Stories.displaying_testimonals()}")

