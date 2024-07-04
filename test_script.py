import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

from home_page import HomePage
from business_page import BusinessPage
from CareerPath_Page import Careerpage
from Search_bar import SearchCourse

# Initialize driver to None
driver = None

chromeoptions = webdriver.ChromeOptions()


def get_user_preference():
    while True:
        view_preference = input("Enter '1' for desktop view or '2' for mobile view: ")
        if view_preference in ['1', '2']:
            return view_preference
        else:
            print("Invalid input. Please enter '1' or '2'.")

def main():
    view_preference = get_user_preference()
    if view_preference == '1':
        chromeoptions = webdriver.ChromeOptions()
        chromeoptions.add_argument("--start-fullscreen")
    else:  # '2' for mobile view
        chromeoptions = webdriver.ChromeOptions()
        chromeoptions.add_argument("--window-size=375,812")
    return chromeoptions


chromeoptions = main()

# chromeoptions = webdriver.ChromeOptions()
# chromeoptions.add_argument("--start-fullscreen")
# chromeoptions.add_argument("--window-size=375,812")

# Specify the browser to use
browsername = "chrome"

# Initialize the webdriver based on the specified browser
if browsername == "chrome":
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=chromeoptions)
elif browsername == "firefox":
    driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()), options=chromeoptions)
elif browsername == "internetExplorer":
    driver = webdriver.Ie(options=chromeoptions)
elif browsername == "edge":
    driver = webdriver.Edge(options=chromeoptions)
else:
    print("Please pass the correct browser name: chrome, firefox, edge, or internetExplorer: ", browsername)

# Maximizes the browser window to fill the entire screen.
# driver.maximize_window()

# Navigate to a specific URL
if driver is not None:
    home_page = HomePage(driver)
    home_page.navigate_to("https://www.interactivecares.com/")
    time.sleep(2)

    # Close the advertisement
    home_page.close_advertisement()
    time.sleep(1)

    # home_page.scroll_to_bottom()
    # time.sleep(4)
    #
    # home_page.scroll_to_top()
    # time.sleep(4)

    # Search for a course from the search bar
    # Search_bar = SearchCourse(driver)
    # Search_bar.search_course("Flutter")
    # time.sleep(4)
    # assert Search_bar.verify_search_results("Flutter App Development Career Path - Batch 2"), "Search result not found"
    # time.sleep(2)

    # Navigate to Career Path page
    CareerPath_Page = Careerpage(driver)
    CareerPath_Page.courseenroll(chromeoptions)
    time.sleep(2)
    CareerPath_Page.navigate_to_career()
    time.sleep(6)

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
