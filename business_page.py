import time

from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from base_page import BasePage


class BusinessPage(BasePage):
    # Locators
    BUSINESS_PAGE = (By.XPATH, "//h3[normalize-space()='Business']")
    GetInTouch_Modal = (By.XPATH, "//span[contains(text(),'Get in Touch')]")
    FIRST_NAME = (By.XPATH, "//input[@placeholder='Enter your First Name']")
    LAST_NAME = (By.XPATH, "//input[@placeholder='Enter your Last Name']")
    PHONE_NUMBER = (By.XPATH, "//input[@placeholder='Enter your Phone Number']")
    EMAIL = (By.XPATH, "(//input[@placeholder='Enter your Email Address'])[1]")
    COMPANY_NAME = (By.XPATH, "(//input[@placeholder='Enter your Company Name'])[1]")
    COMPANY_ADDRESS = (By.XPATH, "(//input[@placeholder='Enter your Company Address'])[1]")
    COMPANY_SIZE = (By.XPATH, "//div[@role='dialog']//div[1]//select[1]")
    NUMBER_TRAINEES = (By.XPATH, "//div[@role='dialog']//div//div[2]//select[1]")
    TRAINING_TOPIC = (By.XPATH, "(//input[@placeholder='Enter your Preferred Topic'])[1]")
    YOUR_ROLE = (By.XPATH, "//input[@placeholder='Enter your Role']")
    DESCRIPTION = (By.XPATH, "//textarea[@placeholder='Enter your Description']")
    SUBMIT_BUTTON = (By.XPATH, "//button[@type='submit']//span[contains(text(),'Get in Touch')]")
    SUCCESS_MESSAGE = (By.XPATH, '//span[contains(@class, "text-green-600 text-xl my-3") and text()="Email sent '
                                 'successfully"]')
    FIRST_NAME_ERROR = (By.XPATH, "(//span[contains(text(),'This field is required')])[1]")
    LAST_NAME_ERROR = (By.XPATH, "(//span[contains(text(),'This field is required')])[1]")
    PHONE_ERROR = (By.XPATH, "(//span[contains(text(),'This field is required')])[3]")
    EMAIL_ERROR = (By.XPATH, "//div[@role='dialog']//div//div[2]//div[2]//div[1]//span[2]")
    COMPANY_NAME_ERROR = (By.XPATH, "//body//div[@role='presentation']//div[@role='presentation']//div[3]//div[1]//div[1]//span[2]")
    COMPANY_ADDRESS_ERROR = (By.XPATH, "//body//div[@role='presentation']//div[@role='presentation']//div[3]//div[2]//div[1]//span[2]")
    COMPANY_SIZE_ERROR = (By.XPATH, "(//span[contains(text(),'This field is required')])[7]")
    NUMBER_TRAINEES_ERROR = (By.XPATH, "(//span[contains(text(),'This field is required')])[8]")
    TRAINING_TOPIC_ERROR = (By.XPATH, "//div[5]//div[1]//div[1]//span[2]")
    YOUR_ROLE_ERROR = (By.XPATH, "//div[5]//div[2]//div[1]//span[2]")
    DESCRIPTION_ERROR = (By.XPATH, "(//span[contains(text(),'This field is required')])[11]")
    THREE_DOT = (By.XPATH, "(//*[name()='svg'][@stroke='currentColor'])[1]")

    def __init__(self, driver):
        super().__init__(driver)
        self.GET_IN_TOUCH_MODAL = None

    def navigate_to_business(self):
        self.click(*self.BUSINESS_PAGE)


    # Iterates through each option in the dropdown, selects it, and reopens the dropdown for the next selection. Finally, selects a specified option.
    def interact_with_dropdown(self, locator, final_option):
        select_element = Select(self.wait_for_element(*locator))
        for option in select_element.options:
            select_element.select_by_visible_text(option.text)
            time.sleep(1)  # A delay to see each selection
            self.wait_for_element(*locator).click()  # open the dropdown again

        # Select final option
        select_element.select_by_visible_text(final_option)
        time.sleep(2)

    def get_in_touch(self, company_size_value=None, number_trainees_value=None):
        self.click(*self.GetInTouch_Modal)
        time.sleep(1)
        self.wait_for_element(*self.FIRST_NAME).send_keys("John")
        time.sleep(1)
        self.wait_for_element(*self.LAST_NAME).send_keys("Doe")
        time.sleep(1)
        self.wait_for_element(*self.PHONE_NUMBER).send_keys("1234567890")
        time.sleep(1)
        self.wait_for_element(*self.EMAIL).send_keys("Foyez@gmail.com")
        time.sleep(1)
        self.wait_for_element(*self.COMPANY_NAME).send_keys("Interactive Cares")
        time.sleep(1)
        self.wait_for_element(*self.COMPANY_ADDRESS).send_keys("123 Main Street")
        time.sleep(1)

        # Interact with COMPANY_SIZE dropdown
        self.interact_with_dropdown(self.COMPANY_SIZE, company_size_value)
        # Interact with NUMBER_TRAINEES dropdown
        self.interact_with_dropdown(self.NUMBER_TRAINEES, number_trainees_value)

        self.wait_for_element(*self.TRAINING_TOPIC).send_keys("Automation Testing")
        time.sleep(1)
        self.wait_for_element(*self.YOUR_ROLE).send_keys("QA Engineer")
        time.sleep(1)
        self.wait_for_element(*self.DESCRIPTION).send_keys("This is a test description.")
        time.sleep(1)
        self.click(*self.SUBMIT_BUTTON)
        time.sleep(1)

    # def get_in_touch_with_no_data(self):
    #     self.click(*self.GetInTouch_Modal)
    #     time.sleep(1)
    #     self.click(*self.SUBMIT_BUTTON)
    #     time.sleep(1)

    def get_in_touch_invalid_email(self, company_size_value=None, number_trainees_value=None):
        # self.wait_for_element(*self.GetInTouch_Modal).click()
        self.click(*self.GetInTouch_Modal)
        time.sleep(1)
        self.wait_for_element(*self.FIRST_NAME).send_keys("John")
        time.sleep(1)
        self.wait_for_element(*self.LAST_NAME).send_keys("Doe")
        time.sleep(1)
        self.wait_for_element(*self.PHONE_NUMBER).send_keys("1234567890")
        time.sleep(1)
        self.wait_for_element(*self.EMAIL).send_keys("invalid_email")
        time.sleep(1)
        self.wait_for_element(*self.COMPANY_NAME).send_keys("Interactive Cares")
        time.sleep(1)
        self.wait_for_element(*self.COMPANY_ADDRESS).send_keys("123 Main Street")
        time.sleep(1)

        # Interact with COMPANY_SIZE dropdown
        self.interact_with_dropdown(self.COMPANY_SIZE, company_size_value)
        # Interact with NUMBER_TRAINEES dropdown
        self.interact_with_dropdown(self.NUMBER_TRAINEES, number_trainees_value)

        self.wait_for_element(*self.TRAINING_TOPIC).send_keys("Automation Testing")
        time.sleep(1)
        self.wait_for_element(*self.YOUR_ROLE).send_keys("QA Engineer")
        time.sleep(1)
        self.wait_for_element(*self.DESCRIPTION).send_keys("This is a test description.")
        time.sleep(1)
        self.click(*self.SUBMIT_BUTTON)
        time.sleep(2)

    def get_in_touch_missing_first_name(self, company_size_value=None, number_trainees_value=None):
        self.click(*self.GetInTouch_Modal)
        time.sleep(1)
        self.wait_for_element(*self.LAST_NAME).send_keys("Doe")
        time.sleep(1)
        self.wait_for_element(*self.PHONE_NUMBER).send_keys("1234567890")
        time.sleep(1)
        self.wait_for_element(*self.EMAIL).send_keys("Foyez@gmail.com")
        time.sleep(1)
        self.wait_for_element(*self.COMPANY_NAME).send_keys("Interactive Cares")
        time.sleep(1)
        self.wait_for_element(*self.COMPANY_ADDRESS).send_keys("123 Main Street")
        time.sleep(1)

        # Interact with COMPANY_SIZE dropdown
        self.interact_with_dropdown(self.COMPANY_SIZE, company_size_value)
        # Interact with NUMBER_TRAINEES dropdown
        self.interact_with_dropdown(self.NUMBER_TRAINEES, number_trainees_value)

        self.wait_for_element(*self.TRAINING_TOPIC).send_keys("Automation Testing")
        time.sleep(1)
        self.wait_for_element(*self.YOUR_ROLE).send_keys("QA Engineer")
        time.sleep(1)
        self.wait_for_element(*self.DESCRIPTION).send_keys("This is a test description.")
        time.sleep(1)
        self.click(*self.SUBMIT_BUTTON)
        time.sleep(1)

    def get_in_touch_missing_last_name(self, company_size_value=None, number_trainees_value=None):
        self.click(*self.GetInTouch_Modal)
        time.sleep(1)
        self.wait_for_element(*self.FIRST_NAME).send_keys("John")
        time.sleep(1)
        self.wait_for_element(*self.PHONE_NUMBER).send_keys("1234567890")
        time.sleep(1)
        self.wait_for_element(*self.EMAIL).send_keys("Foyez@gmail.com")
        time.sleep(1)
        self.wait_for_element(*self.COMPANY_NAME).send_keys("Interactive Cares")
        time.sleep(1)
        self.wait_for_element(*self.COMPANY_ADDRESS).send_keys("123 Main Street")
        time.sleep(1)

        # Interact with COMPANY_SIZE dropdown
        self.interact_with_dropdown(self.COMPANY_SIZE, company_size_value)
        # Interact with NUMBER_TRAINEES dropdown
        self.interact_with_dropdown(self.NUMBER_TRAINEES, number_trainees_value)

        self.wait_for_element(*self.TRAINING_TOPIC).send_keys("Automation Testing")
        time.sleep(1)
        self.wait_for_element(*self.YOUR_ROLE).send_keys("QA Engineer")
        time.sleep(1)
        self.wait_for_element(*self.DESCRIPTION).send_keys("This is a test description.")
        time.sleep(1)
        self.click(*self.SUBMIT_BUTTON)
        time.sleep(1)

    def verify_success_message(self):
        try:
            success_element = self.wait_for_element(*self.SUCCESS_MESSAGE)
            print(f"Success message found: {success_element.text}")
            return "Email sent successfully" in success_element.text
        except TimeoutException:
            print("Success message not found.")
            print(f"Current page source:\n{self.driver.page_source}")
            return False

    def first_name_validation(self):
        success_element = self.wait_for_element(*self.FIRST_NAME_ERROR)
        return "This field is required" in success_element.text

    def last_name_validation(self):
        success_element = self.wait_for_element(*self.LAST_NAME_ERROR)
        return "This field is required" in success_element.text

    def phone_validation(self):
        success_element = self.wait_for_element(*self.PHONE_ERROR)
        return "This field is required" in success_element.text

    def email_validation(self):
        success_element = self.wait_for_element(*self.EMAIL_ERROR)
        return "This field is required" in success_element.text

    def company_name_validation(self):
        success_element = self.wait_for_element(*self.COMPANY_NAME_ERROR)
        return "This field is required" in success_element.text

    def company_address_validation(self):
        success_element = self.wait_for_element(*self.COMPANY_ADDRESS_ERROR)
        return "This field is required" in success_element.text

    def company_size_validation(self):
        success_element = self.wait_for_element(*self.COMPANY_SIZE_ERROR)
        return "This field is required" in success_element.text

    def number_trainees_validation(self):
        success_element = self.wait_for_element(*self.NUMBER_TRAINEES_ERROR)
        return "This field is required" in success_element.text

    def training_topic_validation(self):
        success_element = self.wait_for_element(*self.TRAINING_TOPIC_ERROR)
        return "This field is required" in success_element.text

    def your_role_validation(self):
        success_element = self.wait_for_element(*self.YOUR_ROLE_ERROR)
        return "This field is required" in success_element.text

    def description_validation(self):
        success_element = self.wait_for_element(*self.DESCRIPTION_ERROR)
        return "This field is required" in success_element.text
