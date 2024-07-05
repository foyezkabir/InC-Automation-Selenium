import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from constants import DeviceView
from base_page import BasePage


class Careerpage(BasePage):

    # Locators
    CAREER_PAGE = (By.XPATH, "//h3[normalize-space()='Career Path']")
    COURSE = (By.XPATH, "//div[5]//div[1]//div[1]//a[1]//img[1]")
    COURSE_LIVE = (By.XPATH, "//button[contains(text(),'লাইভ ক্লাস')]")
    COURSE_Project = (By.XPATH, "///button[contains(text(),'প্রজেক্ট অ্যান্ড অ্যাসাইনমেন্ট')]")
    COURSE_Resource = (By.XPATH, "//button[contains(text(),'প্রয়োজনীয় রিসোর্স')]")
    COURSE_COUPON = (By.XPATH, "//input[@placeholder='Apply Promo']")
    COURSE_COUPON_APPLY = (By.XPATH, "//span[@class='apply-text']")
    COURSE_ENROLL = (By.XPATH, "//span[@class='enroll-text']")
    USER_LOGIN = (By.XPATH, "//input[@placeholder='Enter your Username or Email']")
    USER_PASSWORD = (By.XPATH, "//input[@placeholder='Enter your Password']")
    CHECK_BOX = (By.XPATH, "//input[@type='checkbox']")
    LOGIN_BUTTON = (By.XPATH, "//button[contains(text(),'Login')]")
    REGISTER_NOW = (By.XPATH, "//a[normalize-space()='Register']")
    REGISTER_FIRST_NAME = (By.XPATH, "///input[@placeholder='First Name']")
    REGISTER_LAST_NAME = (By.XPATH, "///input[@placeholder='Last Name']")
    REGISTER_EMAIL = (By.XPATH, "//input[@placeholder='Email']")
    REGISTER_COUNTRY = (By.XPATH, "///div[@title='Bangladesh: + 880']")
    REGISTER_PHONE = (By.XPATH, "//input[@placeholder='1 (702) 123-4567']")
    REGISTER_PHONE_VERIFY = (By.XPATH, "//button[normalize-space()='Verify']")
    REGISTER_USERNAME = (By.XPATH, "//input[@placeholder='User Name']")
    REGISTER_PASSWORD = (By.XPATH, "//input[@name='password']")
    REGISTER_PASS_MASK = (By.CSS_SELECTOR, "body > div:nth-child(6) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > main:nth-child(1) > div:nth-child(1) > form:nth-child(3) > div:nth-child(6) > div:nth-child(1) > svg:nth-child(3)")
    REGISTER_CONFIRM_PASSWORD = (By.XPATH, "//input[@name='confirmPassword']")
    REGISTER_CONFIRM_PASS_MASK = (By.XPATH, "(//*[name()='svg'][@class='absolute right-3 bottom-5 cursor-pointer text-[#18B3C7]'])[2]")
    REGISTER_CHECKBOX = (By.XPATH, "//input[@value='false']")
    REGISTER_BUTTON = (By.XPATH, "//button[normalize-space()='Register']")
    LOGIN_PAGE = (By.XPATH, "//a[normalize-space()='Log In']")
    THREE_DOT = (By.XPATH, "(//*[name()='svg'][@stroke='currentColor'])[1]")
    CAREER_PAGE_MOBILE = (By.XPATH, "//a[contains(text(),'Career Path')]")

    def __init__(self, driver, view):
        super().__init__(driver)
        self.view = view

    def navigate_to_career(self):
        self.click(*self.CAREER_PAGE)

    def click_three_dot_menu(self):
        try:
            self.click(*self.THREE_DOT)
            time.sleep(2)
        except Exception as e:
            print(f"Error clicking three-dot menu: {e}")

    def mobile_courseenroll(self):
        self.click_three_dot_menu()
        time.sleep(2)
        self.click(*self.CAREER_PAGE_MOBILE)
        time.sleep(2)

    def desktop_courseenroll(self):
        self.click(*self.CAREER_PAGE)
        time.sleep(1)
        self.click(*self.COURSE)
        time.sleep(2)
        self.click(*self.COURSE_ENROLL)
        time.sleep(2)
        self.wait_for_element(*self.USER_LOGIN).send_keys("kabirwiit00@gmail.com")
        time.sleep(2)
        self.wait_for_element(*self.USER_PASSWORD).send_keys("Kabirwiit18#")
        time.sleep(2)
        self.click(*self.CHECK_BOX)
        time.sleep(2)
        self.click(*self.LOGIN_BUTTON)
        time.sleep(4)

    def courseenroll(self):
        if self.view == DeviceView.MOBILE:
            self.mobile_courseenroll()
        else:
            self.desktop_courseenroll()
