import time

import allure
import pytest
from TESTS.utils import randomize_float, randomize_latin_string
from TESTS.params import params_amount_values
from PAGES.Locators import CategoriesLocators, OperationListLocators


@allure.suite("Income Page")
class TestIncomePage:
    # ###########################CATEGORIES ADD###############################################
    @allure.title("Add new category to Constant Income list")
    @allure.feature("Dropdown list")
    @allure.description("""
    Attempt to add a new category to Constant Income list using the criteria:
    - New category name is less than 14 characters
    - New category name is not exist in the list

    Precondition:
    - User uses valid login and password

    Expected Result:
    - New category is added to Constant income (DropList).
    """)
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.dropdown_list
    def test_check_add_category_to_constant_income(self, income_page):
        income_const = income_page(list_name="Постоянные", list_locator=CategoriesLocators.constant_dropdown)
        income_const.add_category(randomize_latin_string(10))

    @allure.title("Add new category to Temp Income list")
    @allure.feature("Dropdown list")
    @allure.description("""
    Attempt to add a new category to Temp Income list using the criteria:
    - New category name is less than 14 characters
    - New category name is not exist in the list

    Precondition:
    - User uses valid login and password

    Expected Result:
    - New category is added to Temp income (DropList).
    """)
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.dropdown_list
    def test_check_add_category_to_temp_income(self, income_page):
        income_temp = income_page(list_name="Временные", list_locator=CategoriesLocators.temp_dropdown)
        income_temp.add_category(randomize_latin_string(10))

    # #########################CATEGORIES ERRORS CHECK############################################################

    @allure.title("Error Message in Modal Window When New Category Name Already Exists in the List (Constant Income)")
    @allure.feature("Dropdown errors")
    @allure.description("""
    An error message is shown in the modal window when the user tries to add a new category
    with a name that already exists in the Constant Incomes list.

    Precondition:
    - User uses valid login and password
    - Category name already exists in the Constant Incomes list

    Expected Result:
    - An error message is shown in the modal window when the user fills the proper field in the modal window
    trying to add a new income category which already exists in the Constant Incomes List.
    """)
    @allure.severity(allure.severity_level.MINOR)
    @pytest.mark.dropdown_errors
    def test_check_exist_category_name_error_constant_income(self, income_page):
        income_const = income_page(list_name="Постоянные", list_locator=CategoriesLocators.constant_dropdown)
        income_const.error_name_exist()

    @allure.title("Error Message in Modal Window When New Category Name Already Exists in the List (Temp Income)")
    @allure.feature("Dropdown errors")
    @allure.description("""
    An error message is shown in the modal window when the user tries to add a new category
    with a name that already exists in the Temp Incomes list.

    Precondition:
    - User uses valid login and password
    - Category name already exists in the Temp Incomes list

    Expected Result:
    - An error message is shown in the modal window when the user fills the proper field in the modal window
    trying to add a new income category which already exists in the Temp Incomes List.
    """)
    @allure.severity(allure.severity_level.MINOR)
    @pytest.mark.dropdown_errors
    def test_check_exist_category_name_error_temp_income(self, income_page):
        income_temp = income_page(list_name="Временные", list_locator=CategoriesLocators.temp_dropdown)
        income_temp.error_name_exist()

    @allure.title("Error Message in Modal Window When New Category Name "
                  "Is More Than 14 Characters (Constant Income list)")
    @allure.feature("Dropdown errors")
    @allure.description("""
    An error message is shown in the modal window when the user tries to add a new category
    with a name that is more than 14 characters.

    Precondition:
    - User uses valid login and password
    - Category name more than 14 characters

    Expected Result:
    - An error message is shown in the modal window when the user fills the proper field in the modal window
    trying to add a new Constant income category with a name more than 14 characters.
    """)
    @allure.severity(allure.severity_level.MINOR)
    @pytest.mark.dropdown_errors
    def test_check_category_name_length_error_constant_income(self, income_page):
        income_const = income_page(list_name="Постоянные", list_locator=CategoriesLocators.constant_dropdown)
        income_const.error_name_length(randomize_latin_string(15))

    @allure.title("Error Message in Modal Window When New Category Name "
                  "Is More Than 14 Characters (Temp Income list)")
    @allure.feature("Dropdown errors")
    @allure.description("""
    An error message is shown in the modal window when the user tries to add a new category
    with a name that is more than 14 characters.

    Precondition:
    - User uses valid login and password
    - Category name more than 14 characters

    Expected Result:
    - An error message is shown in the modal window when the user fills the proper field in the modal window
    trying to add a new Temp income category with a name more than 14 characters.
    """)
    @allure.severity(allure.severity_level.MINOR)
    @pytest.mark.dropdown_errors
    def test_check_category_name_length_error_temp_income(self, income_page):
        income_temp = income_page(list_name="Временные", list_locator=CategoriesLocators.temp_dropdown)
        income_temp.error_name_length(randomize_latin_string(15))

    # #########################CATEGORIES ERRORS CHECK REPEAT######################################################

    @allure.title("Length Error Message does not shows in Modal Window repeat open(Constant Income)")
    @allure.feature("Dropdown errors")
    @allure.description("""
    An exist error message is does not shows in the modal window when the user tries to add a new category
    with a name that more then 14 chars in the Constant Incomes list then close window and repeat. 

    Precondition:
    - User uses valid login and password
    - Category name is more then 14 chars

    Expected Result:
    - An error message does not shows in the modal window when the user fills the proper field in the modal window
    trying to add a new income category which already exists in the Constant Incomes List, 
    then close window and try again.
    """)
    @allure.severity(allure.severity_level.MINOR)
    @pytest.mark.dropdown_errors
    def test_check_length_error_repeat_constant_income(self, income_page):
        income_const = income_page(list_name="Постоянные", list_locator=CategoriesLocators.constant_dropdown)
        income_const.repeat_error_name_length(randomize_latin_string(15))

    @allure.title("Length Error Message does not shows in Modal Window repeat open(Temp Income)")
    @allure.feature("Dropdown errors")
    @allure.description("""
    An exist error message is does not shows in the modal window when the user tries to add a new category
    with a name that more then 14 chars in the Temp Incomes list then close window and repeat. 

    Precondition:
    - User uses valid login and password
    - Category name is more then 14 chars

    Expected Result:
    - An error message does not shows in the modal window when the user fills the proper field in the modal window
    trying to add a new income category which already exists in the Temp Incomes List, 
    then close window and try again.
    """)
    @allure.severity(allure.severity_level.MINOR)
    @pytest.mark.dropdown_errors
    def test_check_length_error_repeat_temp_income(self, income_page):
        income_temp = income_page(list_name="Временные", list_locator=CategoriesLocators.temp_dropdown)
        income_temp.repeat_error_name_length(randomize_latin_string(15))

    @allure.title("Exists Error Message does not shows in Modal Window repeat open(Constant Income)")
    @allure.feature("Dropdown errors")
    @allure.description("""
    An exist error message is does not shows in the modal window when the user tries to add a new category
    with a name that already exists in the Constant Incomes list then close window and repeat. 

    Precondition:
    - User uses valid login and password
    - Category name already exists in the Constant Incomes list

    Expected Result:
    - An error message does not shows in the modal window when the user fills the proper field in the modal window
    trying to add a new income category which already exists in the Constant Incomes List, 
    then close window and try again.
    """)
    @allure.severity(allure.severity_level.MINOR)
    @pytest.mark.dropdown_errors
    def test_check_exist_error_repeat_constant_income(self, income_page):
        income_const = income_page(list_name="Постоянные", list_locator=CategoriesLocators.constant_dropdown)
        income_const.repeat_error_name_exist()

    @allure.title("Exists Error Message does not shows in Modal Window repeat open(Temp Income)")
    @allure.feature("Dropdown errors")
    @allure.description("""
    An exist error message is does not shows in the modal window when the user tries to add a new category
    with a name that already exists in the Temp Incomes list then close window and repeat. 

    Precondition:
    - User uses valid login and password
    - Category name already exists in the Temp Incomes list

    Expected Result:
    - An error message does not shows in the modal window when the user fills the proper field in the modal window
    trying to add a new income category which already exists in the Temp Incomes List, 
    then close window and try again.
    """)
    @allure.severity(allure.severity_level.MINOR)
    @pytest.mark.dropdown_errors
    def test_check_exist_error_repeat_temp_income(self, income_page):
        income_temp = income_page(list_name="Временные", list_locator=CategoriesLocators.temp_dropdown)
        income_temp.repeat_error_name_exist()

    # #########################CATEGORIES DELETE ######################################################
    @allure.title("Archive Category from Constant Income list")
    @allure.feature("Dropdown Modal Actions")
    @allure.description("""
    Attempt to archive selected category from Constant Income list
    when user click 'Archive' button in modal window.

    Precondition:
    - User uses valid login and password
    - One o more category exist in the list

    Expected Result:
    - The selected category is archived from Constant Income list
    when user click 'Archive' button in modal window.
    """)
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.dropdown_modal_actions
    def test_check_archive_random_constant_income(self, income_page):
        income_const = income_page(list_name="Постоянные", list_locator=CategoriesLocators.constant_dropdown)
        income_const.category_modal_action("В архив")

    @allure.title("Archive Category from Temp Income list")
    @allure.feature("Dropdown Modal Actions")
    @allure.description("""
    Attempt to archive selected category from Temp Income list
    when user click 'Archive' button in modal window.

    Precondition:
    - User uses valid login and password
    - One o more category exist in the list

    Expected Result:
    - The selected category is archived from Temp Income list
    when user click 'Archive' button in modal window.
    """)
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.dropdown_modal_actions
    def test_check_archive_random_temp_income(self, income_page):
        income_temp = income_page(list_name="Временные", list_locator=CategoriesLocators.temp_dropdown)
        income_temp.category_modal_action("В архив")

    @allure.title("Cancel Delete Category operation from Constant Income list")
    @allure.feature("Dropdown Modal Actions")
    @allure.description("""
    Attempt to cancel delete selected category operation from Constant Income list
    when user click 'Cancel' button in modal window.

    Precondition:
    - User uses valid login and password
    - One o more category exist in the list

    Expected Result:
    - The selected category is not deleted from Constant Income list
    when user click 'Cancel' button in modal window.
    """)
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.dropdown_modal_actions
    def test_check_cancel_random_constant_income(self, income_page):
        income_const = income_page(list_name="Постоянные", list_locator=CategoriesLocators.constant_dropdown)
        income_const.category_modal_action("Отмена")

    @allure.title("Cancel Delete Category operation from Temp Income list")
    @allure.feature("Dropdown Modal Actions")
    @allure.description("""
    Attempt to cancel delete selected category operation from Temp Income list
    when user click 'Cancel' button in modal window.

    Precondition:
    - User uses valid login and password
    - One o more category exist in the list

    Expected Result:
    - The selected category is not deleted from Temp Income list
    when user click 'Cancel' button in modal window.
    """)
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.dropdown_modal_actions
    def test_check_cancel_random_temp_income(self, income_page):
        income_temp = income_page(list_name="Временные", list_locator=CategoriesLocators.temp_dropdown)
        income_temp.category_modal_action("Отмена")

    @allure.title("Delete Category from Constant Income list")
    @allure.feature("Dropdown Modal Actions")
    @allure.description("""
    Attempt to delete selected category from Constant Income list
    when user click 'Delete' button in modal window.

    Precondition:
    - User uses valid login and password
    - One o more category exist in the list

    Expected Result:
    - The selected category is deleted from Constant Income list
    when user click 'Delete' button in modal window.
    """)
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.dropdown_modal_actions
    def test_check_delete_random_constant_income(self, income_page):
        income_const = income_page(list_name="Постоянные", list_locator=CategoriesLocators.constant_dropdown)
        income_const.category_modal_action("Удалить")

    @allure.title("Delete Category from Temp Income list")
    @allure.feature("Dropdown Modal Actions")
    @allure.description("""
    Attempt to delete selected category from Temp Income list
    when user click 'Delete' button in modal window.

    Precondition:
    - User uses valid login and password
    - One o more category exist in the list

    Expected Result:
    - The selected category is deleted from Temp Income list
    when user click 'Delete' button in modal window.
    """)
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.dropdown_modal_actions
    def test_check_delete_random_temp_income(self, income_page):
        income_temp = income_page(list_name="Временные", list_locator=CategoriesLocators.temp_dropdown)
        income_temp.category_modal_action("Удалить")

    # ########################-OPERATION LIST-######################################################

    @allure.title("Shows Added Amount in Operation List (Constant)")
    @allure.feature("Operation list")
    @allure.description("""
    Attempt to add random amount to exist category in Constant Income list.
    After user click "Add" button on the page, amount shows adds to category.
    Operation shows in the bottom page section in Operation List.

    Precondition:
    - User uses valid login and password
    - Positive amount

    Expected Result:
    - Amount added to existing category in Constant Income list.
    - Added amount shows in Operation list.
    """)
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.operation_list
    @pytest.mark.parametrize("value", params_amount_values)
    def test_check_operation_list_constant_income(self, income_page, value):
        income_const = income_page(list_name="Постоянные", list_locator=CategoriesLocators.constant_dropdown,
                                   add_amount_field=CategoriesLocators.add_amount_to_category_field_const,
                                   add_amount_btn=CategoriesLocators.add_amount_to_category_btn_const
                                   )
        income_const.operation_add_amount(value)

    @allure.title("Shows Added Amount in Operation List (temp)")
    @allure.feature("Operation list")
    @allure.description("""
    Attempt to add random amount to exist category in Temp Income list.
    After user click "Add" button on the page, amount shows adds to category.
    Operation shows in the bottom page section in Operation List.

    Precondition:
    - User uses valid login and password
    - Positive amount

    Expected Result:
    - Amount added to existing category in Constant Income list.
    - Added amount shows in Operation list.
    """)
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.operation_list
    @pytest.mark.parametrize("value", params_amount_values)
    def test_check_operation_list_temp_income(self, income_page, value):
        income_const = income_page(list_name="Временные", list_locator=CategoriesLocators.temp_dropdown,
                                   add_amount_field=CategoriesLocators.add_amount_to_category_field_temp,
                                   add_amount_btn=CategoriesLocators.add_amount_to_category_btn_temp
                                   )
        income_const.operation_add_amount(value)

    @allure.title("Delete Amount in Operation List (Income)")
    @allure.feature("Operation list")
    @allure.description("""
    Attempt to delete amount from Operation list. User clic 'x' in the List item line.

    Precondition:
    - User uses valid login and password
    - One o more category exist in the list

    Expected Result:
    - Amount deleted from Operation list after user click 'x' in Item line in the list.
    """)
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.operation_list
    def test_check_operation_del_btn_income(self, income_page):
        income = income_page(btn_name_locator=OperationListLocators.oper_modal_delete_btn)
        income.operations_del(btn_name="delete")

    @allure.title("Cancel Deleting Amount in Operation List")
    @allure.feature("Operation list")
    @allure.description("""
    Attempt to delete amount from Operation list. User clic 'x' in the List item line.

    Precondition:
    - User uses valid login and password
    - One o more category exist in the list

    Expected Result:
    - Amount deleted from Operation list after user click 'x' in Item line in the list.
    """)
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.operation_list
    def test_check_operation_cancel_btn_income(self, income_page):
        income = income_page(btn_name_locator=OperationListLocators.oper_modal_cancel_btn)
        income.operations_del(btn_name="cancel")

    @allure.title("Edit Amount in Operation List (Income)")
    @allure.feature("Incomes Operation list")
    @allure.description("""
    Attempt to edit amount in Operation list. User click 'edit' icon in the List item line.

    Precondition:
    - User uses valid login and password
    - One o more category exist in the list

    Expected Result:
    - Amount edited and updated in Operation list after user click 'edit' icon in Item line in the list.
    """)
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.operation_list
    def test_check_operation_edit_btn_income(self, income_page):
        income = income_page()
        income.operation_edit_btn(randomize_float(10000))

    # ##########################CALENDAR########################################################
    @allure.title("Set current date in calendar (Income Page)")
    @allure.feature("Calendar")
    @allure.description("""
    Attempt to set current date in calendar using "Today" button:

    Precondition:
    - User uses valid login and password

    Expected Result:
    - Current date set in calendar when user click 'Today' button in calendar.
    """)
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.calendar
    def test_calendar_current_btn_income(self, income_page):
        income = income_page()
        income.calendar_current_btn()

    @allure.title("Clear date in calendar (Income Page)")
    @allure.feature("Calendar")
    @allure.description("""
    Attempt to clear date in calendar using "Clear" button:

    Precondition:
    - User uses valid login and password

    Expected Result:
    - Current date cleared in calendar when user click 'Clear' button in calendar.
    """)
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.calendar
    def test_calendar_clear_btn_income(self, income_page):
        income = income_page()
        income.calendar_clear_btn()

    def test_total_amount_const_income(self, income_page):
        income = income_page(list_name="Постоянные", list_locator=CategoriesLocators.constant_dropdown,
                             add_amount_field=CategoriesLocators.add_amount_to_category_field_const,
                             add_amount_btn=CategoriesLocators.add_amount_to_category_btn_const
                             )
        old_amount = income.total_amount(CategoriesLocators.total_amount)
        summ = randomize_float(10000)
        income.operation_add_amount(amount=summ)
        time.sleep(3)
        new_amount = income.total_amount(CategoriesLocators.total_amount)
        assert new_amount == old_amount + summ

    def test_total_amount_temp_income(self, income_page):
        income = income_page(list_name="Временные", list_locator=CategoriesLocators.temp_dropdown,
                             add_amount_field=CategoriesLocators.add_amount_to_category_field_temp,
                             add_amount_btn=CategoriesLocators.add_amount_to_category_btn_temp
                             )
        old_amount = income.total_amount(CategoriesLocators.balance_aside)
        summ = randomize_float(10000)
        income.operation_add_amount(amount=summ)
        time.sleep(3)
        new_amount = income.total_amount(CategoriesLocators.balance_aside)
        assert new_amount == old_amount + summ

