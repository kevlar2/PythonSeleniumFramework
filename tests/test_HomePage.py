from time import sleep
import pytest

from TestData.HomePageData import HomePageData
from pageObject.HomePage import HomePage
from utilities.BaseClass import BaseClass


class TestHomePage(BaseClass):

    def test_form_submission(self, get_data):
        home_page = HomePage(self.driver)
        log = self.get_logger()

        # Enter name, email, password
        log.info("Entering name, email, password")
        home_page.enter_name().send_keys(get_data["fullname"])
        home_page.enter_email().send_keys(get_data["Email address"])
        home_page.enter_password().send_keys(get_data["Password"])

        # Click on checkbox
        log.info("Select checkbox")
        home_page.select_checkbox().click()

        # Click on gender dropdown
        log.info("Selecting gender from dropdown")
        home_page.select_gender().click()

        self.select_element_by_visible_text_from_static_dropdown_using_id(home_page.select_gender(), get_data["Gender"])

        self.select_element_by_index_from_static_dropdown_using_id(home_page.select_gender(), get_data["Gender_value"])

        # select Employment Status radio button
        log.info("Selecting employment status radio button")
        home_page.select_radio_button().click()

        # Enter dob
        log.info("Entering dob")
        sleep(2)
        home_page.enter_dob().send_keys(get_data["DOB"])
        log.info("Grabbed screenshot after entering dob")
        self.driver.get_screenshot_as_file("ConfirmHomePageDob.png")

        # Submit form
        log.info("Form submitted")
        home_page.submit_form().click()

        # Validate form after submission
        log.info("Validating confirmation message")
        submit_confirmation = home_page.get_submit_confirmation()
        value = submit_confirmation.text
        assert (home_page.submit_confirmation_text in value)

        self.refresh_page()

    # Tuple example
    # @pytest.fixture(params=[("Kevin Oru", "Kevin.Oru@hpdlendscape.com", "password", "Male", 0, "22/04/1984"),
    #                         ("Aryah Oru", "Aryah.Oru@hpdlendscape.com", "Aryah", "Female", 1, "01/02/2020")])
    # Dictionary example
    # @pytest.fixture(params=[{"fullname": "Kevin Oru",
    #                         "Email address": "Kevin.Oru@hpdlendscape.com",
    #                         "Password": "password",
    #                         "Gender": "Male",
    #                         "Gender_value": 0,
    #                         "DOB": "22/04/1984"},
    #                        {"fullname": "Aryah Oru",
    #                         "Email address": "Aryah.Oru@hpdlendscape.com",
    #                         "Password": "Aryah",
    #                         "Gender": "Female",
    #                         "Gender_value": 1,
    #                         "DOB": "01/02/2020"}])

    # Loading data from another class
    @pytest.fixture(params=HomePageData.get_test_data_from_excel("TestCase2"))
    def get_data(self, request):
        return request.param
