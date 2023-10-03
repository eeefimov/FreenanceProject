import random
import time
import re
from PAGES.main import Main
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver
from TESTS.utils import randomize_number


class OperationListManager(Main):
    def __init__(self, driver):
        super().__init__(driver)

    def operation_list_check_amount(self, values_locator, amount):
        list_items = self.driver.find_elements(*values_locator)
        matching_numbers = []

        for value in list_items:
            text = value.text
            match = re.search(r'(?<=\+)(\d+)₽', text)  # Match the number following a '+'
            if match:
                number = int(match.group(1))
                if number == amount:
                    matching_numbers.append(number)
                    return matching_numbers[0]

    def operation_list_get_btn(self, values_locator, btn_name: str):
        list_items = self.driver.find_elements(*values_locator)

        for value in list_items:
            if btn_name == "delete":
                delete_btn = value.find_element(By.CSS_SELECTOR, "div.Transactions_icons__xnfue > button:nth-child(1)")
                ActionChains(self.driver).click(delete_btn).perform()
                break
            elif btn_name == "edit":
                edit_btn = value.find_element(By.CSS_SELECTOR, 'div.Transactions_icons__xnfue > button:nth-child(2)')
                ActionChains(self.driver).click(edit_btn).perform()
                break






