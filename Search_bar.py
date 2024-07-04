import time

from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from base_page import BasePage


class SearchCourse(BasePage):

    # Locators
    SEARCH_BAR = (By.XPATH, "(//input[@class='text-white w-[170px] lg:w-[180px] xl:w-[180px] outline-none bg-transparent px-2'])[1]")
    SEARCH_ICON = (By.XPATH, "//button[normalize-space()='Search']")
    # SEARCH_RESULTS = (By.XPATH, "(//h3[normalize-space()='Flutter App Development Career Path - Batch 2'])[1]")
    SEARCH_RESULTS = (By.XPATH, "(//div[@class='grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 lg:grid-cols-3 xl:grid-cols-4 gap-4 mt-5 lg:mt-8 xl:mt-8 2xl:mt-8 pb-20 px-6 md:px-0 lg:px-6 xl:px-6 2xl:px-6'])[1]")

    def __init__(self, driver):
        super().__init__(driver)

    def search_course(self, course):
        self.wait_for_element(*self.SEARCH_BAR).send_keys(course)
        self.click(*self.SEARCH_ICON)
        time.sleep(2)

    # def verify_search_results(self, keyword):
    #     results = self.wait_for_elements(*self.SEARCH_RESULTS)
    #     for result in results:
    #         if keyword in result.text:
    #             return True
    #     return False

    def verify_search_results(self, keyword):
        results = self.wait_for_elements(*self.SEARCH_RESULTS)
        found = False
        for result in results:
            if keyword in result.text:
                found = True
                break
        return found


