from time import sleep

from pageObject.HomePage import HomePage
from utilities.BaseClass import BaseClass


class TestOne(BaseClass):

    def test_e2e(self):

        home_page = HomePage(self.driver)
        log = self.get_logger()

        # Navigate to shop
        log.info("Navigating shop page")
        checkout_page = home_page.shop_items()

        # Add item (blackberry) to cart
        log.info("Add blackberry to cart")
        products = checkout_page.get_product_card_titles()

        for product in products:
            product_name = product.text
            log.info(product_name)
            if product_name == "Blackberry":
                # Add item to cart
                log.info(product_name)
                checkout_page.add_item_to_checkout().click()

        # Navigate to checkout
        log.info("Navigate to checkout page")
        checkout_page.get_checkout_page().click()

        # Click on checkout button
        log.info("Click on checkout button")
        confirm_page = checkout_page.checkout()

        # Select country from dropdown
        log.info("Selecting delivery country")
        confirm_page.enter_country().send_keys("India")
        self.wait_by_link_text(7, "India")
        confirm_page.country().click()

        # Select check box
        log.info("selecting terms and conditions checkbox")
        confirm_page.checkbox().click()
        sleep(2)
        # assert element_by_xpath("//div[@class='checkbox checkbox-primary']").is_selected()

        # Click on purchase
        log.info("Completing purchase")
        confirm_page.purchase().click()

        # Validate that checkout is successful
        log.info("Validating successful checkout")
        order_confirmation = confirm_page.get_success_confirmation_text().text
        assert confirm_page.expected_confirmation_text in order_confirmation

