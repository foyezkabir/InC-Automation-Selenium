import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from home_page import HomePage
from business_page import BusinessPage

# Initialize driver to None
driver = None

# Specify the browser to use
browsername = "chrome"

# Initialize the webdriver based on the specified browser
try:
    if browsername == "chrome":
        print("Initializing Chrome browser...")
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    elif browsername == "firefox":
        print("Initializing Firefox browser...")
        driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
    elif browsername == "internetExplorer":
        print("Initializing Internet Explorer browser...")
        driver = webdriver.Ie()
    elif browsername == "edge":
        print("Initializing Edge browser...")
        driver = webdriver.Edge()
    else:
        print("Please pass the correct browser name: chrome, firefox, edge, or internetExplorer: ", browsername)
except Exception as e:
    print(f"Error initializing the browser: {e}")

# Maximizes the browser window to fill the entire screen.
if driver is not None:
    driver.maximize_window()
    print("Browser window maximized")

    # Navigate to a specific URL
    try:
        home_page = HomePage(driver)
        home_page.navigate_to("https://www.interactivecares.com/")
        print("Navigated to interactive cares.com")
        time.sleep(2)

        # Close the advertisement
        home_page.close_advertisement()
        print("Advertisement closed")
        time.sleep(2)

        # Navigate to Business page
        business_page = BusinessPage(driver)
        business_page.navigate_to_business()
        print("Navigated to Business page")
        time.sleep(2)

        # Perform 'Get in Touch' action and fill out the form
        business_page.get_in_touch("Less than 500 employees", "1 to 30 trainees")
        print("Filled out the form with valid data")
        time.sleep(4)

        business_page.get_in_touch_invalid_email(company_size_value="Less than 500 employees",
                                                 number_trainees_value="1 to 30 trainees")
        print("Filled out the form with invalid email")

        business_page.get_in_touch_missing_first_name(company_size_value="Less than 500 employees",
                                                      number_trainees_value="1 to 30 trainees")
        print("Filled out the form with missing first name")

        business_page.get_in_touch_missing_last_name(company_size_value="Less than 500 employees",
                                                     number_trainees_value="1 to 30 trainees")
        print("Filled out the form with missing last name")

        # Verify success message
        # assert business_page.verify_success_message(), "Success message not displayed or incorrect"

        # Close the browser
        # business_page.close_browser()
    except Exception as e:
        print(f"Error during test execution: {e}")
else:
    print("Driver not initialized. Cannot navigate to URL.")
