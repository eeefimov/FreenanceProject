from selenium.webdriver.common.by import By
from TESTS.utils import randomize_date


class IncomePageCalendarLocators:
    incomepage_form_title = (By.CSS_SELECTOR, "h2.main_field_title")
    incomepage_calendar = (By.CSS_SELECTOR, "input[placeholder='Выбор даты'][readonly]")
    incomepage_calendar_today_btn = (By.XPATH, "//span[contains(text(),'Сегодня')]")
    incomepage_calendar_clear_btn = (By.XPATH, "//span[contains(text(),'Очистить')]")
    incomepage_calendar_month = (By.CSS_SELECTOR, "input.input")
    incomepage_calendar_date = (By.XPATH, f"//div[contains(text(),'{randomize_date()}')]")


class IncomePageCategoriesLocators:
    incomepage_logo = (By.CLASS_NAME, "logo_block")

    incomepage_constant_dropdown = (By.XPATH, "//div[contains(text(),'Постоянные')]")
    incomepage_temp_dropdown = (By.XPATH, "//div[contains(text(),'Временные')]")
    incomepage_add_value_to_list = (By.XPATH, "//div[@class='option_list_add' and @data-value='Добавить категорию']")
    incomepage_modal_window_value_field_constant = (By.XPATH,
                                                    "(//input[@class='Modal_modal_input__LHDfG' and contains("
                                                    "@placeholder, 'Название категории')])[1]")
    incomepage_modal_window_value_field_temp = (By.XPATH,
                                                "(//input[@class='Modal_modal_input__LHDfG' and contains("
                                                "@placeholder, 'Название категории')])[2]")
    incomepage_modal_window_add_value_btn_constant = (By.XPATH, "(//button[contains(text(), 'Добавить')])[1]")
    incomepage_modal_window_add_value_btn_temp = (By.XPATH, "(//button[contains(text(), 'Добавить')])[3]")

    incomepage_list_values = (By.CSS_SELECTOR, "div.dropdown-item")

    incomepage_modal_window_exist_name_error = (By.XPATH,
                                                "//div[contains(text(),'Категория с таким именем уже существует')]")
    incomepage_modal_window_length_name_error = (By.XPATH,
                                                 "//div[@class='Modal_modal__fokG5 Modal_active__c78VE']//div"
                                                 "[@class='Modal_errorMessage__OvxDq' and contains(text(), "
                                                 "'Не более 14 символов')]")
    income_modal_window_add_x_btn = (By.CSS_SELECTOR, ".Modal_active__c78VE img")

    incomepage_add_value_to_category_field_constant = (By.XPATH, "(//input[@class='main_field_string_input'])[1]")
    incomepage_add_value_to_category_field_temp = (By.XPATH, "(//input[@class='main_field_string_input'])[2]")

    incompage_add_value_btn_constant = (By.CSS_SELECTOR, "form.main_field_string:nth-child(4) > button.main_field_string_button:nth-child(6)")
    incompage_add_value_btn_temp = (By.CSS_SELECTOR, "form.main_field_string:nth-child(6) > button.main_field_string_button:nth-child(6)")

    incompage_add_value_plus_btn_constant = (By.XPATH, "(//button[@class='main_field_string_button_plus'])[1]")
    incompage_add_value_plus_btn_temp = (By.XPATH, "(//button[@class='main_field_string_button_plus'])[2]")


class IncomePageCategoriesDelete:
    incomepage_modal_window_delete_btn = (By.CSS_SELECTOR, ".Modal_active__c78VE .Modal_button__CFXUj:nth-child(1)")
    incomepage_modal_window_archive_btn = (By.CSS_SELECTOR, ".Modal_active__c78VE .Modal_button__CFXUj:nth-child(2)")
    incomepage_modal_window_cancel_btn = (By.CSS_SELECTOR, ".Modal_active__c78VE .Modal_button__CFXUj:nth-child(3)")






