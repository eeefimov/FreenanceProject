from selenium.webdriver.common.by import By


class CalendarLocators:
    calendar = (By.XPATH, "//input[@class='input']")
    calendar_today_btn = (By.XPATH, "//span[contains(text(),'Сегодня')]")
    calendar_clear_btn = (By.XPATH, "//span[contains(text(),'Очистить')]")


class CategoriesLocators:
    income_logo = (By.CLASS_NAME, "logo_block")

    constant_dropdown = (By.XPATH, "//div[@class='dropdown-selected-value' and contains(text(), 'Постоянные')]")
    temp_dropdown = (By.XPATH, "//div[@class='dropdown-selected-value' and contains(text(), 'Временные')]")
    saves_dropdown = (By.XPATH, "//div[@class='dropdown-selected-value' and contains(text(), 'Накопления')]")
    list_add_value_btn = (By.XPATH, "//div[@class='option_list_add' and contains(@data-value, 'Добавить категорию')]")

    list_elements = (By.XPATH, "//div[@class='dropdown-item false']")
    list_element_del_btn_locator = (By.XPATH, "//div/span[@title='Удаление категории']")

    modal_window_add_name_value_field = (By.XPATH, "//div[contains(@class, 'Modal_active')]//input")
    modal_window_add_name_value_btn = (By.XPATH, "//div[contains(@class, 'Modal_active')]//button")

    exist_name_error = (By.XPATH, "//div[contains(text(),'Категория с таким именем уже существует')]")
    length_error = (By.XPATH, "//div[contains(text(), 'Не более 14 символов')]")
    modal_window_add_x_btn = (By.XPATH, "//div[contains(@class, 'Modal_active')]//img")

    add_amount_to_category_field_const = (By.XPATH, "(//input[@class='main_field_string_input'])[1]")
    add_amount_to_category_field_temp = (By.XPATH, "(//input[@class='main_field_string_input'])[2]")
    add_amount_to_category_field_saves = (By.XPATH, "(//input[@class='main_field_string_input'])[3]")

    add_amount_to_category_btn_const = (By.XPATH, "(//button[@class='main_field_string_button'])[1]")
    add_amount_to_category_btn_temp = (By.XPATH, "(//button[@class='main_field_string_button'])[2]")
    add_amount_to_category_btn_saves = (By.XPATH, "(//button[@class='main_field_string_button'])[3]")

    total_amount = (By.XPATH, "(//div[@class='main']//input)[1]")
    balance_aside = (By.XPATH, "(//div[@class='aside']//input)[1]")


class OperationListLocators:
    oper_list_values = (By.XPATH, "//div[@class='transactions']//*[@id]")

    oper_modal_delete_btn = (By.XPATH, "//div[contains(@class, 'Modal_active')]//button[text() = 'Удалить']")
    oper_modal_cancel_btn = (By.XPATH, "//div[contains(@class, 'Modal_active')]//button[text() = 'Отмена']")

    oper_modal_edit_field = (By.XPATH, "//div[contains(@class, 'Modal_active')]//input")

    oper_modal_add_btn = (By.XPATH, "//div[contains(@class, 'Modal_active')]//button")


class PageLinks:
    outcome_link_btn = (By.XPATH, "//a[@class='button' and contains(@href, '/rectangle/mainfieldcosts')]")
    saves_link_btn = (By.XPATH, "//a[@class='button' and contains(@href, '/rectangle/mainfieldstorage')]")
    analitic_lnk_btn = (By.XPATH, "//a[@class='button' and contains(@href, '/rectangle/mainfieldanalitic')]")