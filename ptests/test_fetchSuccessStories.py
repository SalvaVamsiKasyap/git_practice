from utilities.BaseClass import BaseClass
import pytest
from page_Objects.home_Page import home_Page
import datetime

now = datetime.datetime.now()

timestamp = now.strftime('%Y-%m-%d %H:%M:%S')

datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')


@pytest.mark.usefixtures("setup")
class Test_fetchSuccessStories(BaseClass):

    def test_fetchsucessstories(self):

        log = self.get_logger()
        log.info(f"{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')} Entering home page..")
        hom_pag = home_Page(self.driver)
        log.info(f"{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')} Checking whether the acceptance button for the disclaimer is fully rendered to click")
        self.verify_element_clickable("//div[@class='modal-content']/div[2]/span")
        log.info(f"{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')} Clicking on acceptance button")
        hom_pag.accepting_disclaimer()
        log.info(f"{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')} Successfully accepted the acceptance button")
        log.info(f"{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')} Checking whether the WHY ITERO button fully rendered to click")
        self.verify_element_clickable("//div[@class='TopNavigation_links__SM670']/a[text()='Why iTero']")
        why_iter = hom_pag.choosing_iteroOption()
        log.info(f"{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')} Checking whether the SUCCESS STORIES button fully rendered to click")
        self.verify_element_clickable("//a[text()='View success stories']")
        log.info(f"{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')} Successfully choosen WHY ITERO option")
        success_Stories = why_iter.clicking_successstoriesbutton()
        log.info(f"{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')} Clicked view success stories button")
        log.info(f"{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')} Waiting for the rendering of Orthodontics option")
        self.verify_element_clickable("//a[text()='Orthodontic']")
        success_Stories.clicking_orthodontics_button()
        log.info(f"{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')} Successfully clicked on orthodontics option")
        log.info(f"{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')} Waiting for the appearence of testimonals under Orthodontic option")
        self.verify_element_presence("//div[text()='orthodontic']/preceding-sibling::div/p")
        log.info(f"{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')} These are our testimonals{success_Stories.displaying_testimonals()}")

