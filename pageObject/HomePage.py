from selenium.webdriver.common.by import By
from pageObject.CheckoutPage import CheckoutPage


class HomePage:
    submit_confirmation_text = "Success! The Form has been submitted successfully!."

    def __init__(self, driver):
        self.driver = driver

    name = (By.NAME, "name")
    email = (By.NAME, "email")
    password = (By.ID, "exampleInputPassword1")
    checkbox = (By.ID, "exampleCheck1")
    gender_dropdown = (By.ID, "exampleFormControlSelect1")
    radio_button = (By.CSS_SELECTOR, "input[id='inlineRadio1']")
    dob = (By.CSS_SELECTOR, "input[name='bday']")
    submit = (By.XPATH, "//input[@value='Submit']")
    submit_confirmation = (By.CLASS_NAME, "alert-success")
    shop = (By.CSS_SELECTOR, "a[href*='shop']")

    def enter_name(self):
        return self.driver.find_element(*HomePage.name)

    def enter_email(self):
        return self.driver.find_element(*HomePage.email)

    def enter_password(self):
        return self.driver.find_element(*HomePage.password)

    def select_checkbox(self):
        return self.driver.find_element(*HomePage.checkbox)

    def select_gender(self):
        return self.driver.find_element(*HomePage.gender_dropdown)

    def select_radio_button(self):
        return self.driver.find_element(*HomePage.radio_button)

    def enter_dob(self):
        return self.driver.find_element(*HomePage.dob)

    def submit_form(self):
        return self.driver.find_element(*HomePage.submit)

    def get_submit_confirmation(self):
        return self.driver.find_element(*HomePage.submit_confirmation)

    def shop_items(self):
        self.driver.find_element(*HomePage.shop).click()
        checkout_page = CheckoutPage(self.driver)
        return checkout_page
