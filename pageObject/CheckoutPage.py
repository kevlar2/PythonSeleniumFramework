from selenium.webdriver.common.by import By
from pageObject.ConfirmPage import ConfirmPage


class CheckoutPage:

    def __init__(self, driver):
        self.driver = driver

    product_cards = (By.CSS_SELECTOR, ".card-title a")
    add_to_checkout = (By.CSS_SELECTOR, ".card-footer button")
    navigate_checkout_button = (By.CSS_SELECTOR, "a[class*='btn-primary']")
    checkout_button = (By.XPATH, "//button[@class='btn btn-success']")

    def get_product_card_titles(self):
        return self.driver.find_elements(*CheckoutPage.product_cards)

    def add_item_to_checkout(self):
        return self.driver.find_element(*CheckoutPage.add_to_checkout)

    def get_checkout_page(self):
        return self.driver.find_element(*CheckoutPage.navigate_checkout_button)

    def checkout(self):
        self.driver.find_element(*CheckoutPage.checkout_button).click()
        confirm_page = ConfirmPage(self.driver)
        return confirm_page
