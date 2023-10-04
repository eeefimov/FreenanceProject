import time
from PAGES.StartPage import StartPage
from PAGES.Features.CalendarManager import CalendarManager
from PAGES.Features.DropDownManager import DropDownManager
from PAGES.Features.OperationListManager import OperationListManager
from PAGES.Locators import IncomePageCalendarLocators, IncomePageCategoriesLocators, \
    IncomePageCategoriesDelete, IncomePageOperationListLocators
from TESTS.utils import randomize_latin_string


class IncomePage(StartPage,
                 IncomePageCalendarLocators,
                 IncomePageCategoriesLocators,
                 IncomePageCategoriesDelete,
                 IncomePageOperationListLocators):
    def __init__(self, driver):
        super().__init__(driver)
#################-Calendar-###################################################################################################

    def setup_income_calendar(self, login, pwd, expected):
        self.start_page_login(login, pwd, expected)
        cm = CalendarManager(self.driver)
        cm.set_date("Выбор даты", self.incomepage_calendar, self.incomepage_calendar_month)
        return cm

    def income_check_calendar_current_btn(self, login, pwd, expected):
        cm = self.setup_income_calendar(login, pwd, expected)
        selected_date = (cm.set_date("Сегодня", self.incomepage_calendar_today_btn, self.incomepage_calendar_month))
        current_date = self.current_date()
        assert selected_date == current_date

    def income_check_calendar_clear_btn(self, login, pwd, expected):
        cm = self.setup_income_calendar(login, pwd, expected)
        selected_date = (
            cm.set_date("Очистить", self.incomepage_calendar_clear_btn, self.incomepage_calendar_month))
        time.sleep(1)
        current_date = self.current_date()
        assert selected_date != current_date

    def income_check_calendar_random_date_current_month(self, login, pwd, expected):
        cm = self.setup_income_calendar(login, pwd, expected)
        selected_date = (cm.set_date("Случайная дата", self.incomepage_calendar_date,
                                     self.incomepage_calendar_month))
        time.sleep(2)
        assert selected_date != None or "" or "Выбор даты"

#################-Categories-#####################################################################################
    def setup_dropdown(self, login, pwd, expected):
        self.start_page_login(login, pwd, expected)
        DdM = DropDownManager(self.driver)

        return DdM

    def add_category(self, login, pwd, expected, n: int, ln_error: bool,
                     list_name: str, list_locator, modal_field_locator, madal_add_btn_locator):

        value = randomize_latin_string(n)
        list_category = self.setup_dropdown(login, pwd, expected)
        list_category.select_categories_and_action(list_name, list_locator, "Добавить категорию",
                                                   self.incomepage_add_value_to_list)

        length_error = list_category.set_value_add_modal_window("Название категории", modal_field_locator,
                                                                value, self.incomepage_modal_window_length_name_error)
        assert length_error == ln_error

        if not length_error:
            return "Length error is displayed"
        else:
            exist_error = list_category.add_value_to_category("Добавить", madal_add_btn_locator,
                                                          self.incomepage_modal_window_exist_name_error)
            print(exist_error)
            name_check = list_category.check_added_value_in_category(value, list_name, list_locator,
                                                             self.incomepage_list_values)
            print(name_check)
            assert name_check

    def check_exist_name(self, login, pwd, expected, ex_error: bool,
                         list_name: str, list_locator, add_btn_locator,
                         list_values_locator,
                         modal_field_locator, modal_add_btn_locator,
                         name_exist_error_locator, logo_locator):

        list_category = self.setup_dropdown(login, pwd, expected)
        value = list_category.get_exist_name_from_the_list(list_name, list_locator,
                                                   list_values_locator, logo_locator, "")
        print(value)
        list_category.select_categories_and_action(list_name, list_locator,
                                                   "Добавить категорию", add_btn_locator)
        _ = list_category.set_value_add_modal_window("Название категории", modal_field_locator,
                                                               value, name_exist_error_locator)

        exist_error = list_category.add_value_to_category("Добавить", modal_add_btn_locator, name_exist_error_locator)

        assert exist_error == ex_error

    # ADD categories
    def income_check_add_category_to_constant(self, login, pwd, expected, n: int, ln_error):
        self.add_category(login, pwd, expected, n, ln_error,
                                "Доходы", self.incomepage_constant_dropdown,
                          self.incomepage_modal_window_value_field_constant,
                          self.incomepage_modal_window_add_value_btn_constant)

    def income_check_add_category_to_temp(self, login, pwd, expected, n, ln_error):
        self.add_category(login, pwd, expected, n, ln_error,
                                 "Временные", self.incomepage_temp_dropdown,
                          self.incomepage_modal_window_value_field_temp,
                          self.incomepage_modal_window_add_value_btn_temp)

    # LENGTH errors
    def income_check_category_name_length_error_constant(self, login, pwd, expected, n, ln_error):
        self.income_check_add_category_to_constant(login, pwd, expected, n, ln_error)

    def income_check_category_name_length_error_temp(self, login, pwd, expected, n, ln_error):
        self.income_check_add_category_to_temp(login, pwd, expected, n, ln_error)

    # EXIST errors
    def income_check_exist_category_name_error_constant(self, login, pwd, expected, ex_error):
        self.check_exist_name(login, pwd, expected, ex_error,
                              "Доходы", self.incomepage_constant_dropdown, self.incomepage_add_value_to_list,
                              self.incomepage_list_values,
                              self.incomepage_modal_window_value_field_constant,
                              self.incomepage_modal_window_add_value_btn_constant,
                              self.incomepage_modal_window_exist_name_error,
                              self.incomepage_logo)

    def income_check_exist_category_name_error_temp(self, login, pwd, expected, ex_error):
        self.check_exist_name(login, pwd, expected, ex_error,
                              "Временные", self.incomepage_temp_dropdown, self.incomepage_add_value_to_list,
                              self.incomepage_list_values,
                              self.incomepage_modal_window_value_field_temp,
                              self.incomepage_modal_window_add_value_btn_temp,
                              self.incomepage_modal_window_exist_name_error,
                              self.incomepage_logo)
    # REPEAT errors

    def income_check_length_error_repeat(self, login, pwd, expected, n, ln_error, check_func, select_name,
                                         select_locator):
        if n is not None:
            check_func(login, pwd, expected, n, ln_error)
        else:
            check_func(login, pwd, expected, ln_error)

        self.do_element_click("X", self.income_modal_window_add_x_btn)

        repeat_check = DropDownManager(self.driver)

        repeat_check.select_categories_and_action(select_name, select_locator,
                                                  "Добавить категорию", self.incomepage_add_value_to_list)
        assert self.wait_not_element(self.incomepage_modal_window_length_name_error)

    def income_check_length_error_repeat_constant(self, login, pwd, expected, n, ln_error):
        select_name = "Постоянные"
        select_locator = self.incomepage_constant_dropdown
        self.income_check_length_error_repeat(login, pwd, expected, n, ln_error,
                                              self.income_check_category_name_length_error_constant, select_name,
                                              select_locator)

    def income_check_length_error_repeat_temp(self, login, pwd, expected, n, ln_error):
        select_name = "Временные"
        select_locator = self.incomepage_temp_dropdown
        self.income_check_length_error_repeat(login, pwd, expected, n, ln_error,
                                              self.income_check_category_name_length_error_temp, select_name,
                                              select_locator)

    def income_check_exist_error_repeat_constant(self, login, pwd, expected, ex_error):
        select_name = "Постоянные"
        select_locator = self.incomepage_constant_dropdown
        self.income_check_length_error_repeat(login, pwd, expected, None, ex_error,
                                              self.income_check_exist_category_name_error_constant, select_name,
                                              select_locator)

    def income_check_exist_error_repeat_temp(self, login, pwd, expected, ex_error):
        select_name = "Временные"
        select_locator = self.incomepage_temp_dropdown
        self.income_check_length_error_repeat(login, pwd, expected, None, ex_error,
                                              self.income_check_exist_category_name_error_temp, select_name,
                                              select_locator)

    # DELETE category (DEL, ARCHIVE, CANCEL)

    def delete_category(self, login, pwd, expected,
                        list_name, list_locator, list_values,
                        del_action_btn_name: str, del_action_btn_locator):

        list_category = self.setup_dropdown(login, pwd, expected)
        list_category.select_categories_and_action(list_name, list_locator, "x", list_values)
        list_category.delete_value_modal_wndw_actions(del_action_btn_name, del_action_btn_locator)

    def income_check_random_archive_constant(self, login, pwd, expected):
        self.delete_category(login, pwd, expected,
                               "Постоянные", self.incomepage_constant_dropdown, self.incomepage_list_values,
                               "archive", self.incomepage_modal_window_archive_btn)

    def income_check_random_cancel_constant(self, login, pwd, expected):
        self.delete_category(login, pwd, expected,
                               "Постоянные", self.incomepage_constant_dropdown, self.incomepage_list_values,
                               "cancel", self.incomepage_modal_window_cancel_btn)

    def income_check_random_delete_constant(self, login, pwd, expected):
        self.delete_category(login, pwd, expected,
                               "Постоянные", self.incomepage_constant_dropdown, self.incomepage_list_values,
                               "delete", self.incomepage_modal_window_delete_btn)

    def income_check_random_archive_temp(self, login, pwd, expected):
        self.delete_category(login, pwd, expected,
                               "Временные", self.incomepage_temp_dropdown, self.incomepage_list_values,
                               "archive", self.incomepage_modal_window_archive_btn)

    def income_check_random_cancel_temp(self, login, pwd, expected):
        self.delete_category(login, pwd, expected,
                               "Временные", self.incomepage_temp_dropdown, self.incomepage_list_values,
                               "cancel", self.incomepage_modal_window_cancel_btn)

    def income_check_random_delete_temp(self, login, pwd, expected):
        self.delete_category(login, pwd, expected,
                               "Временные", self.incomepage_temp_dropdown, self.incomepage_list_values,
                               "delete", self.incomepage_modal_window_delete_btn)

# ADD AMOUNT
    def add_amount(self, login, pwd, expected, list_name, list_locator, list_values_locator,
                   logo_locator, amount_field_locator, amount, add_btn_locator):

        amount_category = self.setup_dropdown(login, pwd, expected)
        category_name = amount_category.get_exist_name_from_the_list(list_name, list_locator,
                                                                     list_values_locator, logo_locator, "")

        _ = amount_category.get_exist_name_from_the_list(list_name, list_locator,
                                                        list_values_locator, logo_locator, category_name)

        self.do_element_send_keys("Amount field", amount_field_locator, amount)

        self.do_element_click("Add", add_btn_locator)
        time.sleep(1)

    def income_check_add_value_constant(self, login, pwd, expected, amount):
        self.add_amount(login, pwd, expected,
                        "Постоянные", self.incomepage_constant_dropdown, self.incomepage_list_values,
                        self.incomepage_logo, self.incomepage_add_value_to_category_field_constant, amount,
                        self.incompage_add_value_btn_constant)

    def income_check_add_value_temp(self, login, pwd, expected, amount):
        self.add_amount(login, pwd, expected,
                        "Временные", self.incomepage_temp_dropdown, self.incomepage_list_values,
                        self.incomepage_logo, self.incomepage_add_value_to_category_field_temp, amount,
                        self.incompage_add_value_btn_temp)

    #OPERATION List

    def setup_operation_list(self):
        time.sleep(1)
        ol = OperationListManager(self.driver)
        return ol

    def income_check_operation_constant(self, login, pwd, expected, amount):
        self.income_check_add_value_constant(login, pwd, expected, amount)

        operations = self.setup_operation_list()
        income = operations.operation_list_check_amount(self.incomepage_operation_list_values, amount)
        print(amount, "=", income)
        assert income == amount

    def income_check_operation_temp(self, login, pwd, expected, amount):
        self.income_check_add_value_temp(login, pwd, expected, amount)

        operations = self.setup_operation_list()
        income = operations.operation_list_check_amount(self.incomepage_operation_list_values, amount)
        print(amount, "=", income)
        assert income == amount

    def income_check_operation_x_del_btn(self, login, pwd, expected):
        self.start_page_login(login, pwd, expected)
        operation = self.setup_operation_list()
        operation.operation_list_get_btn(self.incomepage_operation_list_values, "delete")
        time.sleep(1)
        self.do_element_click("delete", self.incomepage_operation_modal_delete_btn)

    def income_check_operation_x_cancel_btn(self, login, pwd, expected):
        self.start_page_login(login, pwd, expected)
        operation = self.setup_operation_list()
        operation.operation_list_get_btn(self.incomepage_operation_list_values, "delete")
        time.sleep(1)
        self.do_element_click("delete", self.incomepage_operation_modal_cancel_btn)

    def income_check_operation_edit_btn(self, login, pwd, expected):
        self.start_page_login(login, pwd, expected)
        operation = self.setup_operation_list()
        operation.operation_list_get_btn(self.incomepage_operation_list_values, "edit")
        time.sleep(1)
        edit_field = self.get_element(self.incomepage_operation_modal_edit_field)
        edit_field.clear()
        time.sleep(1)
        self.do_element_send_keys("Field with old amount",
                                  self.incomepage_operation_modal_edit_field,
                                  1000)
        time.sleep(1)
        self.do_element_click("edit", self.incomepage_operation_modal_add_btn)

    def income_check_operation_edit_amount(self, login, pwd, expected):
        self.income_check_operation_edit_btn(login, pwd, expected)












