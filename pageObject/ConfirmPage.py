from selenium.webdriver.common.by import By


class ConfirmPage:
    expected_confirmation_text = "Success! Thank you! Your order will be delivered in next few weeks :-)"

    def __init__(self, driver):
        self.driver = driver

    country_field = (By.ID, "country")
    select_country = (By.LINK_TEXT, "India")
    checkbox_o = (By.XPATH, "//div[@class='checkbox checkbox-primary']")
    purchase_button = (By.CSS_SELECTOR, "[type='submit']")
    success_confirmation_text = (By.CSS_SELECTOR, "div.alert-success")

    def enter_country(self):
        return self.driver.find_element(*ConfirmPage.country_field)

    def country(self):
        return self.driver.find_element(*ConfirmPage.select_country)

    def checkbox(self):
        return self.driver.find_element(*ConfirmPage.checkbox_o)

    def purchase(self):
        return self.driver.find_element(*ConfirmPage.purchase_button)

    def get_success_confirmation_text(self):
        return self.driver.find_element(*ConfirmPage.success_confirmation_text)
