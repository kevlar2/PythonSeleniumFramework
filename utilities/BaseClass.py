import inspect
import logging
import os

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select


@pytest.mark.usefixtures("setup")
class BaseClass:

    # Logging utility--------------------------------------------------------------------------------
    def get_logger(self):
        # To get the name where the method is being called form
        logger_name = inspect.stack()[1][3]

        # Create a new logger object, and always add __name__ to indicate file name
        logger = logging.getLogger(logger_name)

        # This handles the file creation for the logs
        path = os.getcwd()[:60]
        file_handler = logging.FileHandler(path + '\\utilities\\logfile.log')

        # Logging format
        formatter = logging.Formatter("%(asctime)s :%(levelname)s : %(name)s : %(message)s")
        file_handler.setFormatter(formatter)

        # This logs the data to the file
        logger.addHandler(file_handler)

        # Set logging levels
        logger.setLevel(logging.DEBUG)

        return logger

    # Element locators function-------------------------------------------------------------------------
    def element_by_id(self, locator):
        return self.driver.find_element_by_id(locator)

    def element_by_name(self, locator):
        return self.driver.find_element_by_name(locator)

    def element_by_link_text(self, locator):
        return self.driver.find_element_by_link_text(locator)

    def element_by_class_name(self, locator):
        return self.driver.find_element_by_class_name(locator)

    def element_by_tag_name(self, locator):
        return self.driver.find_element_by_tag_name(locator)

    def element_by_css_selector(self, locator):
        return self.driver.find_element_by_css_selector(locator)

    def element_by_xpath(self, locator):
        return self.driver.find_element_by_xpath(locator)

    def elements_by_xpath(self, locator):
        return self.driver.find_elements_by_xpath(locator)

    def elements_by_name(self, locator):
        return self.driver.find_elements_by_name(locator)

    def elements_by_css_selector(self, locator):
        return self.driver.find_elements_by_css_selector(locator)

    def refresh_page(self):
        self.driver.refresh()

    # Wait functions--------------------------------------------------------
    def wait_by_link_text(self, time, locator):
        WebDriverWait(self.driver, time).until(
            EC.presence_of_element_located((By.LINK_TEXT, locator)))

    def wait_for_element_by_xpath(self, enter_xpath):
        WebDriverWait(self.driver, 30).until(
            EC.visibility_of_element_located((By.XPATH, enter_xpath))
        )

    def wait_for_element_by_css(self, time, locator):
        WebDriverWait(self.driver, time).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, locator))
        )

    # Dropdown selectors-------------------------------------------------------
    # Select class provides the methods to handle the options in a dropdown
    # only use the select class if the html tag-name is select
    def select_element_by_visible_text_from_static_dropdown_using_id(self, locator, element_to_select):
        return Select(locator).select_by_visible_text(element_to_select)

    def select_element_by_index_from_static_dropdown_using_id(self, locator, element_to_select):
        return Select(locator).select_by_index(element_to_select)

    # Javascript executors--------------------------------------------------------------------------------
    def javascript_executor(self, script_to_execute):
        self.driver.execute_script(script_to_execute)

    def javascript_executor2(self, script_to_execute, locator):
        self.driver.execute_script(script_to_execute, locator)
