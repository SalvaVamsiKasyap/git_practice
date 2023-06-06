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
    def test_fetchSuccessStories(self):

        log = self.get_logger()
        home_page_cursor = self.enter_home_page(log)
        self.accept_disclaimer(home_page_cursor,log)
        itero_page_cursor = self.choose_whyItero(home_page_cursor,log)
        success_stories_page_cursor = self.choose_successStoriesButton(itero_page_cursor,log)
        self.retreive_testimonals(success_stories_page_cursor,log)




    # def log__info(self,message,log):
    #
    #     log.info(f"{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')} {message}")

    def enter_home_page(self,log):

        """This method is used to gain access to the homepage on website"""

        hom_pag = home_Page(self.driver)
        log.info(f"{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')} Entered in to home page")
        return hom_pag

    def accept_disclaimer(self, home_page_cursor,log):

        """This method contains click action which will accept the disclaimer on the homepage"""

        home_page_cursor.accepting_disclaimer()
        log.info(f"{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')} Accepted the disclaimer in home_Page")

    def choose_whyItero(self, home_page_cursor,log):

        """This function will be executed on home page and this will chose why itero button on the homepage"""

        why_iter = home_page_cursor.choosing_iteroOption()
        log.info(f"{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')} Choosed the Why itero option")
        return why_iter

    def choose_successStoriesButton(self, itero_page_cursor,log):

        """This function will be executed on itero page and will choose successstories button on itero page"""

        success_stories_page_cursor = itero_page_cursor.clicking_successstoriesbutton()
        log.info(f"{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')} Successfully chosen success stories button")
        return success_stories_page_cursor

    def retreive_testimonals(self, success_stories_page_cursor,log):

        """The method will retrieve all the testimonals from the website """

        log.info(
            f"{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')} Segment options are {success_stories_page_cursor.clicking_segment_button()}")