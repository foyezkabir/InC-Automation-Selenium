import time

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver):
        self.driver = drivermi
        self.timeout = 10

    def wait_for_element(self, by, value):
        return WebDriverWait(self.driver, self.timeout).until(EC.presence_of_element_located((by, value)))

    def wait_for_elements(self, by, value):
        return WebDriverWait(self.driver, self.timeout).until(EC.presence_of_element_located((by, value)))

    def click(self, by, value):
        self.wait_for_element(by, value).click()

    def navigate_to(self, url):
        self.driver.get(url)

    def close_browser(self):
        self.driver.quit()

    # Sroll by a specific pixel amount
    def scroll_page(self, scroll_amount):
        self.driver.execute_script(f"window.scrollBy(0, {scroll_amount});")

    # Scroll to a specific element
    def scroll_to_element(self, element):
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    # Scroll to the bottom of the page
    def scroll_to_bottom(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    # Scroll to the top of the page
    def scroll_to_top(self):
        self.driver.execute_script("window.scrollTo(0, 0);")

    # def click_three_dot_menu(self):
    #     try:
    #         self.click(*self.Careerpage.THREE_DOT)
    #         time.sleep(2)
    #     except Exception as e:
    #         print(f"Error clicking three-dot menu: {e}")
