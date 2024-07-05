import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

from home_page import HomePage
from business_page import BusinessPage
from careerpath_page import Careerpage
from Search_bar import SearchCourse
from constants import DeviceView, Browsers


def get_user_preference():
    while True:
        view_preference = input(f"Enter {DeviceView.DESKTOP} for desktop view or {DeviceView.MOBILE} for mobile view: ")
        if view_preference in [DeviceView.MOBILE, DeviceView.DESKTOP]:
            return view_preference
        else:
            print("Invalid input. Please enter '1' or '2'.")


def get_driver_and_option(browsername, view):
    chrome_options = webdriver.ChromeOptions()
    firefox_options = webdriver.FirefoxOptions()

    if view == DeviceView.MOBILE:
        chrome_options.add_argument("--window-size=375,812")

        firefox_options.add_argument("--width=375")
        firefox_options.add_argument("--height=812")

    else:
        chrome_options.add_argument("--start-fullscreen")
        firefox_options.add_argument("--start-fullscreen")

    if browsername == Browsers.Chrome:
        return webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()),
                                options=chrome_options), chrome_options
    elif browsername == Browsers.Firefox:
        return webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()),
                                 options=firefox_options), firefox_options
    elif browsername == Browsers.InternetExplorer:
        return webdriver.Ie(options=chrome_options), chrome_options
    elif browsername == Browsers.Edge:
        return webdriver.Edge(options=chrome_options), chrome_options

    raise ValueError("Browser Not Found")


# Specify the browser to use
view = get_user_preference()
driver, current_option = get_driver_and_option(Browsers.Chrome, view)

# Navigate to a specific URL
if driver is not None:
    home_page = HomePage(driver)
    home_page.navigate_to("https://www.interactivecares.com/")
    time.sleep(2)

    # Close the advertisement
    home_page.close_advertisement()
    time.sleep(1)

    home_page.scroll_to_bottom()
    time.sleep(4)

    home_page.scroll_to_top()
    time.sleep(4)

    # Search for a course from the search bar
    Search_bar = SearchCourse(driver)
    Search_bar.search_course("Flutter")
    time.sleep(4)

    # Navigate to Career Path page
    careerpath_page = Careerpage(driver, view)

    careerpath_page.courseenroll()
    time.sleep(2)

    # Navigate to Business page
    business_page = BusinessPage(driver)
    business_page.navigate_to_business()
    time.sleep(2)

    # TC-01: Perform 'Get in Touch' action and fill out the form
    business_page.get_in_touch("Less than 500 employees", "1 to 30 trainees")
    time.sleep(0.5)
    assert business_page.verify_success_message(), "Success message not displayed or incorrect"
    driver.refresh()
    time.sleep(2)

    # TC-02: Perform 'Get in Touch' action with invalid Email
    business_page.get_in_touch_invalid_email("Less than 500 employees", "1 to 30 trainees")
    time.sleep(2)
    assert business_page.EMAIL_ERROR, "Email error message not displayed or incorrect"
    driver.refresh()
    time.sleep(2)

    # TC-03: Perform 'Get in Touch' action with missing First Name
    business_page.get_in_touch_missing_first_name("Less than 500 employees", "1 to 30 trainees")
    time.sleep(2)
    assert business_page.FIRST_NAME_ERROR, "First Name error message not displayed or incorrect"
    driver.refresh()
    time.sleep(2)

    # TC-04: Perform 'Get in Touch' action with missing Last Name
    business_page.get_in_touch_missing_last_name("Less than 500 employees", "1 to 30 trainees")
    time.sleep(2)
    assert business_page.LAST_NAME_ERROR, "Last Name error message not displayed or incorrect"
    time.sleep(3)

    # Close the browser
    business_page.close_browser()
else:
    print("Driver not initialized. Cannot navigate to URL.")
