import random
import time
from PAGES.main import Main
from selenium.webdriver.common.by import By


class DropDownManager(Main):
    def __init__(self, driver):
        super().__init__(driver)

    def select_categories_and_action(self, list_name: str, list_locator,
                                     action_name: str, action_locator):
        self.do_element_click(list_name, list_locator)
        time.sleep(1)
        if action_name == "Добавить категорию":
            self.do_element_click(action_name, action_locator)
        else:
            list_items = self.driver.find_elements(*action_locator)

            if list_items:
                selected_item = random.choice(list_items)
                delete_button = selected_item.find_element(By.CLASS_NAME, "Modal_delete_icon__bvKEF")
                self.do_list_item_delete_click(delete_button)
                time.sleep(1)

    def set_value_add_modal_window(self, field_name: str, field_locator, value, name_length_error_locator):
        self.do_element_send_keys(field_name, field_locator, value)
        return self.wait_not_element(name_length_error_locator)

    def add_value_to_category(self, add_btn_name: str, modal_add_btn_locator, name_exist_error_locator):
        self.do_element_click(add_btn_name, modal_add_btn_locator)
        return self.wait_not_element(name_exist_error_locator)

    def check_added_value_in_category(self, name, list_name, list_locator, list_items):
        self.do_element_click(list_name, list_locator)
        item_names = set(item.text for item in self.driver.find_elements(*list_items))

        if name in item_names:
            print("New category name: ", name)
            return True
        else:
            return False

    def get_exist_name_from_the_list(self, list_name: str, list_locator, list_values_locator,
                                     logo_locator, category_name):
        self.do_element_click(list_name, list_locator)
        item_names = set(item.text for item in self.driver.find_elements(*list_values_locator))
        for item in item_names:
            if item == category_name:
                item.click()
                break
        category_name = random.choice(list(item_names))
        self.do_element_click("Logo", logo_locator)
        return category_name

    def delete_value_modal_wndw_actions(self, modal_wndw_delete_btn_name: str, moda_wndw_btn_locator):
        if modal_wndw_delete_btn_name == "archive":
            self.do_element_click("Archive button in modal window", moda_wndw_btn_locator)

        elif modal_wndw_delete_btn_name == "cancel":
            self.do_element_click("Cancel button in modal window", moda_wndw_btn_locator)

        elif modal_wndw_delete_btn_name == "delete":
            self.do_element_click("Delete button in modal window", moda_wndw_btn_locator)
        time.sleep(1)

