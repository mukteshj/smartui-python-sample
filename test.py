import unittest

from selenium import webdriver
import os


username = os.getenv("LT_USERNAME")  # Replace the username
access_key = os.getenv("LT_ACCESS_KEY")  # Replace the access key


class FirstSampleTest(unittest.TestCase):
    # Generate capabilities from here: https://www.lambdatest.com/capabilities-generator/
    # setUp runs before each test case and
    def setUp(self):
        chrome_options = webdriver.ChromeOptions()
        option = {
            "build": 'PyunitTest sample build',  # Change your build name here
            "name": 'Py-unittest',  # Change your test name here
            "browserName": 'Chrome',
            "version": 'latest',
            "platform": 'Windows 11',
            # "resolution": '1024x768', # change the resolution
            "network": 'true',  # Enable or disable network logs
            "smartUI.project": "Testing-Smart-UI"
            # Build name for smartUI(optional)
            # "smartUI.build" : "buildName"
        }
        chrome_options.set_capability("LT:Options", option)
        self.driver = webdriver.Remote(
            command_executor="https://{}:{}@hub.lambdatest.com/wd/hub".format(
                username, access_key),
            options = chrome_options
        )
    # tearDown runs after each test case

    def tearDown(self):
        self.driver.quit()

    # """ You can write the test cases here """
    def test_unit_user_should_able_to_add_item(self):
        # try:
        driver = self.driver

        # Url
        driver.get("https://lambdatest.com")
        print("Taking screenshot")
        driver.execute_script("smartui.takeScreenshot,{\"screenshotName\":\"sample-screenshot-1\"}")
        print("screenshot taken successfully")


if __name__ == "__main__":
    unittest.main()
