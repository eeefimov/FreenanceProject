from selenium.webdriver.common.by import By
import allure
import time
from PAGES.StartPage import StartPage
from TESTS.utils import randomize_number


class IncomePage(StartPage):
    def __init__(self, driver):
        super().__init__(driver)

    incomepage_form_title = (By.CSS_SELECTOR, "h2.main_field_title")
    incomepage_constant_dropdown = (By.XPATH, "//div[contains(text(),'Постоянные')]")
    incomepage_constant_dropdown_add_value_list_item = (By.XPATH, "//div[contains(text(),'Добавить категорию')]")
    incomepage_constant_dropdown_add_value_field = (By.CSS_SELECTOR, "[placeholder='Название категории'")

    incomepage_constant_modal_window_add_value_btn = (By.CLASS_NAME, "Modal_button__CFXUj")
    incomepage_constant_modal_window_name_length_error = (By.XPATH, "//div[contains(text(),'Не более 14 символов')]")
    incomepage_constant_modal_window_name_exist_error = (By.XPATH, "//div[contains(text(),'Категория с таким именем "
                                                                   "уже существует')]")

    incomepage_constant_dropdown_items = (By.CSS_SELECTOR, "div.dropdown-item")
    incomepage_constant_dropdown_delete_btns = (By.CSS_SELECTOR, ".Modal_delete_icon__bvKEF")
    incomepage_delete_category_modal_window_delete_btn = (By.CSS_SELECTOR, ".Modal_active__c78VE "
                                                                           ".Modal_button__CFXUj:nth-child(1)")
    incomepage_delete_category_modal_window_archive_btn = (By.XPATH, "//button[contains(@class, "
                                                                     "'Modal_button_archive__TkwT3') and contains("
                                                                     "@class, 'Modal_button__CFXUj')]")
    incomepage_delete_category_modal_window_cancel_btn = (By.XPATH, "//button[contains(@class, "
                                                                    "'Modal_button_cancel__+SGvx') and contains("
                                                                    "@class, 'Modal_button__CFXUj')]")

    def income_setup_droplist(self, category_name, expected, login, pwd):
        self.start_page_login(login, pwd, expected)
        self.do_element_click("DropList 'Постоянные'", self.incomepage_constant_dropdown)
        self.do_element_click("Add Category", self.incomepage_constant_dropdown_add_value_list_item)
        self.do_element_send_keys("Название категории", self.incomepage_constant_dropdown_add_value_field,
                                  category_name)
        time.sleep(1)

    def income_category_in_income_droplist(self, name):
        item_names = []
        dropdown_items = self.driver.find_elements(*self.incomepage_constant_dropdown_items)
        for item in dropdown_items:
            item_names.append(item.text)

        if name in item_names:
            print(name)
            print("Now: ", len(item_names))
            return True
        else:
            return False

    def income_check_new_category_to_constant(self, login, pwd, expected, category_name):
        self.income_setup_droplist(category_name, expected, login, pwd)
        self.do_element_click("Add button", self.incomepage_constant_modal_window_add_value_btn)
        self.do_element_click("DropList 'Постоянные'", self.incomepage_constant_dropdown)
        assert self.income_category_in_income_droplist(category_name)

    def income_check_new_category_to_constant_invalid(self, login, pwd, expected, category_name):
        self.income_setup_droplist(category_name, expected, login, pwd)
        add_button = self.get_element(self.incomepage_constant_modal_window_add_value_btn)
        assert add_button.is_enabled() == False

    def income_check_new_category_to_constant_error_msg(self, login, pwd, expected, category_name):
        self.income_check_new_category_to_constant_invalid(login, pwd, expected, category_name)
        assert not self.wait_not_element(self.incomepage_constant_modal_window_name_length_error)

    def income_check_new_category_to_constant_exist_name_error_msg(self, login, pwd, expected):
        self.start_page_login(login, pwd, expected)
        self.do_element_click("DropList 'Постоянные'", self.incomepage_constant_dropdown)

        item_names = []
        dropdown_items = self.driver.find_elements(*self.incomepage_constant_dropdown_items)
        for item in dropdown_items:
            item_names.append(item.text)

        category_name = item_names[randomize_number(len(item_names)) - 1]
        print(category_name)

        self.do_element_click("Add Category", self.incomepage_constant_dropdown_add_value_list_item)
        self.do_element_send_keys("Название категории", self.incomepage_constant_dropdown_add_value_field,
                                  category_name)
        self.do_element_click("Add button", self.incomepage_constant_modal_window_add_value_btn)
        assert not self.wait_not_element(self.incomepage_constant_modal_window_name_exist_error)
        time.sleep(2)

    def income_delete(self, expected, login, pwd):
        self.start_page_login(login, pwd, expected)
        self.do_element_click("DropList 'Постоянные'", self.incomepage_constant_dropdown)
        dropdown_items = self.driver.find_elements(*self.incomepage_constant_dropdown_items)
        index = randomize_number(len(dropdown_items) - 1)
        random_element = dropdown_items[index - 2]
        print(random_element.text)
        delete_button = (By.XPATH, f"//div[@class='dropdown-item false' and @index='{index}']//span")
        return delete_button

    def income_check_delete_random_category_actions(self, login, pwd, expected, button_identifier):
        delete_button = self.income_delete(expected, login, pwd)
        self.do_element_click("Delete [x] button", delete_button)
        time.sleep(1)
        if button_identifier == "archive":
            self.do_element_click("Archive button in modal window",
                                  self.incomepage_delete_category_modal_window_archive_btn)
        elif button_identifier == "cancel":
            self.do_element_click("Cancel button in modal window",
                                  self.incomepage_delete_category_modal_window_cancel_btn)
        elif button_identifier == "delete":
            self.do_element_click("Delete button in modal window",
                                  self.incomepage_delete_category_modal_window_delete_btn)
        time.sleep(1)