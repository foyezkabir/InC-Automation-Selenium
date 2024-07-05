Here are the step-by-step instructions on how to run the Selenium-based automated test script for the Interactive Cares website. The script is designed to perform several actions, including filling out a contact form and verifying different input scenarios.

#### Prerequisites

1.  Python Installation: Ensure you have Python installed on your machine.
    
2.  Activate the virtual environment:

For Windows:

    .venv\Scripts\activate

For macOS/Linux:

    source .venv/bin/activate

4.  Install Required Packages: Install the necessary Python packages. You can do this by running the following command in your terminal or command prompt:  

	    pip install -r requirements.txt

#### Running the Script

1.  Save the Script: Save the provided Python script in a file named test_script.py.
    
2.  Create Supporting Files: Ensure you have the following supporting files in the same directory as test_script.py:

		 `home_page.py`
		    
		`business_page.py`
		    
		`careerpath_page.py`
		    
		`search_bar.py`
		    
		`base_page.py`
		    
		`constants.py`
    

4.  Modify constants.py: Ensure constants.py contains the following constants:
    
		class DeviceView: 

	    DESKTOP = "1"  
	    MOBILE = "2"

	    class Browsers:
		    Chrome = "chrome"
		    Firefox = "firefox"
		    InternetExplorer = "internetExplorer"
		    Edge = "edge"

You can choose any browser in which you want to run the test. Just have to pass the browser name in this line of code of test_script.py

	driver, current_option = get_driver_and_option(Browsers.Chrome, view)

1.  Run the Script:

	1.  Open your terminal or command prompt.
	    
	2.  Navigate to the directory where test_script.py is saved.
	    
	3.  Run the script using the following command:  

			python test_script.py
	    
					Or
     
			Run the test_script.py via the run button of the IDE

3.  User Input:
    
	The script will prompt you to enter your preference for the view mode. You can choose between desktop and mobile view.
    
	Enter 1 for desktop view or 2 for mobile view.  

		Enter 1 for desktop view or 2 for mobile view: 

5.  Execution Flow:  
	1.  The script will initialize the browser in the specified view mode.
	    
	2.  It will navigate to the Interactive Cares website and close any advertisements.
	    
	3.  It will scroll to the bottom and top of the homepage.
	    
	4.  It will search for a course using the search bar and verify the search results.
	    
	5.  It will navigate to the Career Path page and perform actions to enroll in a course.
	    
	6.  It will navigate to the Business page and perform the following test cases:

		1.  TC-01: Fill out the 'Get in Touch' form with valid data and verify the success message.
		    
		2.  TC-02: Fill out the form with an invalid email and verify the error message.
		    
		3.  TC-03: Fill out the form with a missing first name and verify the error message.
		    
		4.  TC-04: Fill out the form with a missing last name and verify the error message.

8.  The script will refresh the page between test cases to reset the form.
    
9.  Finally, the script will close the browser.

### Troubleshooting

-   Browser Not Opening: Ensure you have the correct web drivers installed for your browser. The script uses webdriver-manager to manage driver installations.
    
-   Invalid Input: Make sure to enter the correct input when prompted. The script only accepts 1 for desktop view and 2 for mobile view.

**Should be able to run the automated test script by following these instructions. If you encounter any issues, verify that all dependencies are correctly installed and that the supporting files are appropriately configured.**
