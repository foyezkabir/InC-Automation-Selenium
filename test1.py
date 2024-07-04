import time
from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService, Service

# This is another approach to initialize a web browser using Selenium WebDriver without the need for manually installing the corresponding browser driver.

# Create a ChromeOptions object - This object allows you to set specific options for the Chrome browser
chromeoptions = webdriver.ChromeOptions()

# Add an argument to the ChromeOptions object - This argument starts Chrome in fullscreen mode
chromeoptions.add_argument("--start-fullscreen")
# chromeoptions.add_argument("--window-size=375,812")
# chromeoptions.add_argument("--window-size=414,896")
# chromeoptions.add_argument("--window-size=768,1024")
# chromeoptions.add_argument("--window-size=1024,1366")

# The webdriver_manager.chrome module manager handles the ChromeDriver needed to interface with the Chrome browser
from webdriver_manager.chrome import ChromeDriverManager

# driver: WebDriver = webdriver.Chrome(ChromeDriverManager().install(), options=options)

# Initialize the WebDriver for Chrome - The WebDriver is used to interface with the Chrome browser
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=chromeoptions)

# Navigate to a specific URL - The get method of the WebDriver object is used to navigate to a URL
driver.get("https://www.interactivecares.com/business")
time.sleep(10)