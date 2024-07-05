import time

from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from base_page import BasePage


class SearchCourse(BasePage):

    # Locators
    SEARCH_BAR = (By.XPATH, "(//input[@class='text-white w-[170px] lg:w-[180px] xl:w-[180px] outline-none bg-transparent px-2'])[1]")
    SEARCH_ICON = (By.XPATH, "//button[normalize-space()='Search']")

    def __init__(self, driver):
        super().__init__(driver)

    def search_course(self, course):
        self.wait_for_element(*self.SEARCH_BAR).send_keys(course)
        self.click(*self.SEARCH_ICON)
        time.sleep(2)



