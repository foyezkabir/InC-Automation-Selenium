from selenium.webdriver.common.by import By
from base_page import BasePage  # Ensure BasePage is correctly imported


class HomePage(BasePage):
    # Locators
    CLOSE_AD_BUTTON = (By.CSS_SELECTOR, 'svg[class="absolute top-0 right-0 text-3xl text-white cursor-pointer"]')

    def __init__(self, driver):
        super().__init__(driver)

    def close_advertisement(self):
        self.click(*self.CLOSE_AD_BUTTON)
