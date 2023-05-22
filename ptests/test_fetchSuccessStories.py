from utilities.BaseClass import BaseClass
import pytest
from page_Objects.home_Page import home_Page
import datetime

now = datetime.datetime.now()

timestamp = now.strftime('%Y-%m-%d %H:%M:%S')

#datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')


@pytest.mark.usefixtures("setup")
class Test_fetchSuccessStories(BaseClass):
    @pytest.mark.stories
    def test_fetchorthosucessstories(self):

        log = self.get_logger()
        log.info(f"{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')} Entering home page..")
        hom_pag = home_Page(self.driver)
        log.info(f"{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')} Checking whether the acceptance button for the disclaimer is fully rendered to click")
        self.verify_element_clickable("//div[@class='modal-content']/div[2]/span")
        log.info(f"{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')} Clicking on acceptance button")
        hom_pag.accepting_disclaimer()
        log.info(f"{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')} Successfully accepted the acceptance button")
        log.info(f"{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')} Checking whether the WHY ITERO button fully rendered to click")
        self.verify_element_clickable("//div[@class='TopNavigation_links__SM670']/a[text()='Why iTero']")
        why_iter = hom_pag.choosing_iteroOption()
        log.info(f"{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')} Checking whether the SUCCESS STORIES button fully rendered to click")
        self.verify_element_clickable("//a[text()='View success stories']")
        log.info(f"{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')} Successfully choosen WHY ITERO option")
        success_Stories = why_iter.clicking_successstoriesbutton()
        log.info(f"{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')} Clicked view success stories button")
        log.info(f"{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')} Segment options are {success_Stories.clicking_segment_button()}")