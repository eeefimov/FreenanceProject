import allure
import pytest
from TESTS.utils import randomize_float, randomize_latin_string
from TESTS.params import params_amount_values
from PAGES.Locators import CategoriesLocators, OperationListLocators


@allure.suite("Outcome Page")
class TestOutcomePage:
    # ##########################CATEGORIES ADD###############################################
    @allure.title("Add new category to Constant Outcome")
    @allure.feature("Dropdown list")
    @allure.description("""
    Attempt to add a new category to Constant Outcome list using the criteria:
    - New category name is less than 14 characters
    - New category name is not exist in the list

    Precondition:
    - User uses valid login and password

    Expected Result:
    - New category is added to Constant Outcome (DropList).
    """)
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.dropdown_list
    def test_check_add_category_to_constant_outcome(self, outcome_page):
        outcome_const = outcome_page(list_name="Постоянные", list_locator=CategoriesLocators.constant_dropdown)
        outcome_const.add_category(randomize_latin_string(10))

    @allure.title("Add new category to Temp Outcome")
    @allure.feature("Dropdown list")
    @allure.description("""
    Attempt to add a new category to Temp Outcome list using the criteria:
    - New category name is less than 14 characters
    - New category name is not exist in the list

    Precondition:
    - User uses valid login and password

    Expected Result:
    - New category is added to Temp Outcome (DropList).
    """)
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.dropdown_list
    def test_check_add_category_to_temp_outcome(self, outcome_page):
        outcome_temp = outcome_page(list_name="Временные", list_locator=CategoriesLocators.temp_dropdown)
        outcome_temp.add_category(randomize_latin_string(10))

    # #########################CATEGORIES ERRORS CHECK############################################################

    @allure.title("Error Message in Modal Window When New Category Name Already Exists in the List (Constant)")
    @allure.feature("Dropdown errors")
    @allure.description("""
    An error message is shown in the modal window when the user tries to add a new category
    with a name that already exists in the Constant Outcomes list.

    Precondition:
    - User uses valid login and password
    - Category name already exists in the Constant Outcomes list

    Expected Result:
    - An error message is shown in the modal window when the user fills the proper field in the modal window
    trying to add a new Outcome category which already exists in the Constant Outcomes List.
    """)
    @allure.severity(allure.severity_level.MINOR)
    @pytest.mark.dropdown_errors
    def test_check_exist_category_name_error_constant_outcome(self, outcome_page):
        outcome_const = outcome_page(list_name="Постоянные", list_locator=CategoriesLocators.constant_dropdown)
        outcome_const.error_name_exist()

    @allure.title("Error Message in Modal Window When New Category Name Already Exists in the List (Temp)")
    @allure.feature("Dropdown errors")
    @allure.description("""
    An error message is shown in the modal window when the user tries to add a new category
    with a name that already exists in the Temp Outcomes list.

    Precondition:
    - User uses valid login and password
    - Category name already exists in the Temp Outcomes list

    Expected Result:
    - An error message is shown in the modal window when the user fills the proper field in the modal window
    trying to add a new Outcome category which already exists in the Temp Outcomes List.
    """)
    @allure.severity(allure.severity_level.MINOR)
    @pytest.mark.dropdown_errors
    def test_check_exist_category_name_error_temp_outcome(self, outcome_page):
        outcome_temp = outcome_page(list_name="Временные", list_locator=CategoriesLocators.temp_dropdown)
        outcome_temp.error_name_exist()

    @allure.title("Error Message in Modal Window When New Category Name Is More Than 14 Characters (Constant list)")
    @allure.feature("Dropdown errors")
    @allure.description("""
    An error message is shown in the modal window when the user tries to add a new category
    with a name that is more than 14 characters.

    Precondition:
    - User uses valid login and password
    - Category name more than 14 characters

    Expected Result:
    - An error message is shown in the modal window when the user fills the proper field in the modal window
    trying to add a new Constant Outcome category with a name more than 14 characters.
    """)
    @allure.severity(allure.severity_level.MINOR)
    @pytest.mark.dropdown_errors
    def test_check_category_name_length_error_constant_outcome(self, outcome_page):
        outcome_const = outcome_page(list_name="Постоянные", list_locator=CategoriesLocators.constant_dropdown)
        outcome_const.error_name_length(randomize_latin_string(15))

    @allure.title("Error Message in Modal Window When New Category Name Is More Than 14 Characters (Temp list)")
    @allure.feature("Dropdown errors")
    @allure.description("""
    An error message is shown in the modal window when the user tries to add a new category
    with a name that is more than 14 characters.

    Precondition:
    - User uses valid login and password
    - Category name more than 14 characters

    Expected Result:
    - An error message is shown in the modal window when the user fills the proper field in the modal window
    trying to add a new Temp Outcome category with a name more than 14 characters.
    """)
    @allure.severity(allure.severity_level.MINOR)
    @pytest.mark.dropdown_errors
    def test_check_category_name_length_error_temp_outcome(self, outcome_page):
        outcome_temp = outcome_page(list_name="Временные", list_locator=CategoriesLocators.temp_dropdown)
        outcome_temp.error_name_length(randomize_latin_string(15))

    # #########################CATEGORIES ERRORS CHECK REPEAT######################################################

    @allure.title("Length Error Message does not shows in Modal Window repeat open(Constant)")
    @allure.feature("Dropdown errors")
    @allure.description("""
    An exist error message is does not shows in the modal window when the user tries to add a new category
    with a name that more then 14 chars in the Constant Outcomes list then close window and repeat. 

    Precondition:
    - User uses valid login and password
    - Category name is more then 14 chars

    Expected Result:
    - An error message does not shows in the modal window when the user fills the proper field in the modal window
    trying to add a new Outcome category which already exists in the Constant Outcomes List, 
    then close window and try again.
    """)
    @allure.severity(allure.severity_level.MINOR)
    @pytest.mark.dropdown_errors
    def test_check_length_error_repeat_constant_outcome(self, outcome_page):
        outcome_const = outcome_page(list_name="Постоянные", list_locator=CategoriesLocators.constant_dropdown)
        outcome_const.repeat_error_name_length(randomize_latin_string(15))

    @allure.title("Length Error Message does not shows in Modal Window repeat open(Temp)")
    @allure.feature("Dropdown errors")
    @allure.description("""
    An exist error message is does not shows in the modal window when the user tries to add a new category
    with a name that more then 14 chars in the Temp Outcomes list then close window and repeat. 

    Precondition:
    - User uses valid login and password
    - Category name is more then 14 chars

    Expected Result:
    - An error message does not shows in the modal window when the user fills the proper field in the modal window
    trying to add a new Outcome category which already exists in the Temp Outcomes List, 
    then close window and try again.
    """)
    @allure.severity(allure.severity_level.MINOR)
    @pytest.mark.dropdown_errors
    def test_check_length_error_repeat_temp_outcome(self, outcome_page):
        outcome_temp = outcome_page(list_name="Временные", list_locator=CategoriesLocators.temp_dropdown)
        outcome_temp.repeat_error_name_length(randomize_latin_string(15))

    @allure.title("Exists Error Message does not shows in Modal Window repeat open(Constant)")
    @allure.feature("Dropdown errors")
    @allure.description("""
    An exist error message is does not shows in the modal window when the user tries to add a new category
    with a name that already exists in the Constant Outcomes list then close window and repeat. 

    Precondition:
    - User uses valid login and password
    - Category name already exists in the Constant Outcomes list

    Expected Result:
    - An error message does not shows in the modal window when the user fills the proper field in the modal window
    trying to add a new Outcome category which already exists in the Constant Outcomes List, 
    then close window and try again.
    """)
    @allure.severity(allure.severity_level.MINOR)
    @pytest.mark.dropdown_errors
    def test_check_exist_error_repeat_constant_outcome(self, outcome_page):
        outcome_const = outcome_page(list_name="Постоянные", list_locator=CategoriesLocators.constant_dropdown)
        outcome_const.repeat_error_name_exist()

    @allure.title("Exists Error Message does not shows in Modal Window repeat open(Temp)")
    @allure.feature("Dropdown errors")
    @allure.description("""
    An exist error message is does not shows in the modal window when the user tries to add a new category
    with a name that already exists in the Temp Outcomes list then close window and repeat. 

    Precondition:
    - User uses valid login and password
    - Category name already exists in the Temp Outcomes list

    Expected Result:
    - An error message does not shows in the modal window when the user fills the proper field in the modal window
    trying to add a new Outcome category which already exists in the Temp Outcomes List, 
    then close window and try again.
    """)
    @allure.severity(allure.severity_level.MINOR)
    @pytest.mark.dropdown_errors
    def test_check_exist_error_repeat_temp_outcome(self, outcome_page):
        outcome_temp = outcome_page(list_name="Временные", list_locator=CategoriesLocators.temp_dropdown)
        outcome_temp.repeat_error_name_exist()

    # #########################CATEGORIES DELETE ######################################################
    @allure.title("Archive Category from Constant Outcome list")
    @allure.feature("Dropdown Modal Actions")
    @allure.description("""
    Attempt to archive selected category from Constant Outcome list
    when user click 'Archive' button in modal window.

    Precondition:
    - User uses valid login and password
    - One o more category exist in the list

    Expected Result:
    - The selected category is archived from Constant Outcome list
    when user click 'Archive' button in modal window.
    """)
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.dropdown_modal_actions
    def test_check_archive_random_constant_outcome(self, outcome_page):
        outcome_const = outcome_page(list_name="Постоянные", list_locator=CategoriesLocators.constant_dropdown)
        outcome_const.category_modal_action("В архив")

    @allure.title("Archive Category from Temp Outcome list")
    @allure.feature("Dropdown Modal Actions")
    @allure.description("""
    Attempt to archive selected category from Temp Outcome list
    when user click 'Archive' button in modal window.

    Precondition:
    - User uses valid login and password
    - One o more category exist in the list

    Expected Result:
    - The selected category is archived from Temp Outcome list
    when user click 'Archive' button in modal window.
    """)
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.dropdown_modal_actions
    def test_check_archive_random_temp_outcome(self, outcome_page):
        outcome_temp = outcome_page(list_name="Временные", list_locator=CategoriesLocators.temp_dropdown)
        outcome_temp.category_modal_action("В архив")

    @allure.title("Cancel Delete Category operation from Constant Outcome list")
    @allure.feature("Dropdown Modal Actions")
    @allure.description("""
    Attempt to cancel delete selected category operation from Constant Outcome list
    when user click 'Cancel' button in modal window.

    Precondition:
    - User uses valid login and password
    - One o more category exist in the list

    Expected Result:
    - The selected category is not deleted from Constant Outcome list
    when user click 'Cancel' button in modal window.
    """)
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.dropdown_modal_actions
    def test_check_cancel_random_constant_outcome(self, outcome_page):
        outcome_const = outcome_page(list_name="Постоянные", list_locator=CategoriesLocators.constant_dropdown)
        outcome_const.category_modal_action("Отмена")

    @allure.title("Cancel Delete Category operation from Temp Outcome list")
    @allure.feature("Dropdown Modal Actions")
    @allure.description("""
    Attempt to cancel delete selected category operation from Temp Outcome list
    when user click 'Cancel' button in modal window.

    Precondition:
    - User uses valid login and password
    - One o more category exist in the list

    Expected Result:
    - The selected category is not deleted from Temp Outcome list
    when user click 'Cancel' button in modal window.
    """)
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.dropdown_modal_actions
    def test_check_cancel_random_temp_outcome(self, outcome_page):
        outcome_temp = outcome_page(list_name="Временные", list_locator=CategoriesLocators.temp_dropdown)
        outcome_temp.category_modal_action("Отмена")

    @allure.title("Delete Category from Constant Outcome list")
    @allure.feature("Dropdown Modal Actions")
    @allure.description("""
    Attempt to delete selected category from Constant Outcome list
    when user click 'Delete' button in modal window.

    Precondition:
    - User uses valid login and password
    - One o more category exist in the list

    Expected Result:
    - The selected category is deleted from Constant Outcome list
    when user click 'Delete' button in modal window.
    """)
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.dropdown_modal_actions
    def test_check_delete_random_constant_outcome(self, outcome_page):
        outcome_const = outcome_page(list_name="Постоянные", list_locator=CategoriesLocators.constant_dropdown)
        outcome_const.category_modal_action("Удалить")

    @allure.title("Delete Category from Temp Outcome list")
    @allure.feature("Dropdown Modal Actions")
    @allure.description("""
    Attempt to delete selected category from Temp Outcome list
    when user click 'Delete' button in modal window.

    Precondition:
    - User uses valid login and password
    - One o more category exist in the list

    Expected Result:
    - The selected category is deleted from Temp Outcome list
    when user click 'Delete' button in modal window.
    """)
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.dropdown_modal_actions
    def test_check_delete_random_temp_outcome(self, outcome_page):
        outcome_temp = outcome_page(list_name="Временные", list_locator=CategoriesLocators.temp_dropdown)
        outcome_temp.category_modal_action("Удалить")

    @allure.title("Delete Category from Saves Outcome list")
    @allure.feature("Dropdown Modal Actions")
    @allure.description("""
    Attempt to delete selected category from Temp Outcome list
    when user click 'Delete' button in modal window.

    Precondition:
    - User uses valid login and password
    - One o more category exist in the Saves list

    Expected Result:
    - The selected category is deleted from Saves Outcome list
    when user click 'Delete' button in modal window.
    """)
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.dropdown_modal_actions
    def test_check_delete_saves_outcome(self, saves_page, outcome_page):
        # precondition
        saves = saves_page(list_name="Накопления", list_locator=CategoriesLocators.saves_dropdown)
        saves.add_category(randomize_latin_string(10))
        # test
        outcome_temp = outcome_page(list_name="Накопления", list_locator=CategoriesLocators.saves_dropdown)
        outcome_temp.category_modal_action("Удалить")

    @allure.title("Archive Category from Saves Outcome list")
    @allure.feature("Dropdown Modal Actions")
    @allure.description("""
    Attempt to archive selected category from Temp Outcome list
    when user click 'Archive' button in modal window.

    Precondition:
    - User uses valid login and password
    - One o more category exist in the Saves list

    Expected Result:
    - The selected category is archived from Saves Outcome list
    when user click 'Archive' button in modal window.
    """)
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.dropdown_modal_actions
    def test_check_archive_saves_outcome(self, saves_page, outcome_page):
        # precondition
        saves = saves_page(list_name="Накопления", list_locator=CategoriesLocators.saves_dropdown)
        saves.add_category(randomize_latin_string(10))
        # test
        outcome_temp = outcome_page(list_name="Накопления", list_locator=CategoriesLocators.saves_dropdown)
        outcome_temp.category_modal_action("В архив")

    @allure.title("Cancel Delete Category operation from Saves Outcome list")
    @allure.feature("Dropdown Modal Actions")
    @allure.description("""
    Attempt to cancel delete selected category operation from Saves Outcome list
    when user click 'Cancel' button in modal window.

    Precondition:
    - User uses valid login and password
    - One o more category exist in the Saves list

    Expected Result:
    - The selected category is not deleted from Saves Outcome list
    when user click 'Cancel' button in modal window.
    """)
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.dropdown_modal_actions
    def test_check_cancel_saves_outcome(self, saves_page, outcome_page):
        # precondition
        saves = saves_page(list_name="Накопления", list_locator=CategoriesLocators.saves_dropdown)
        saves.add_category(randomize_latin_string(10))
        # test
        outcome_temp = outcome_page(list_name="Накопления", list_locator=CategoriesLocators.saves_dropdown)
        outcome_temp.category_modal_action("Отмена")

    # ########################-OPERATION LIST-######################################################

    @allure.title("Shows Added Amount in Operation List (Constant)")
    @allure.feature("Operation list")
    @allure.description("""
    Attempt to add random amount to exist category in Constant Outcome list.
    After user click "Add" button on the page, amount shows adds to category.
    Operation shows in the bottom page section in Operation List.

    Precondition:
    - User uses valid login and password
    - One o more category exist in the list
    - Positive amount

    Expected Result:
    - Amount added to existing category in Constant Outcome list.
    - Added amount shows in Operation list.
    """)
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.operation_list
    @pytest.mark.parametrize("value", params_amount_values)
    def test_check_operation_list_constant_outcome(self, outcome_page, value):
        outcome_const = outcome_page(list_name="Постоянные", list_locator=CategoriesLocators.constant_dropdown,
                                     add_amount_field=CategoriesLocators.add_amount_to_category_field_const,
                                     add_amount_btn=CategoriesLocators.add_amount_to_category_btn_const
                                     )
        outcome_const.operation_add_amount(value)

    @allure.title("Shows Added Amount in Operation List (Temp)")
    @allure.feature("Operation list")
    @allure.description("""
    Attempt to add random amount to exist category in Temp Outcome list.
    After user click "Add" button on the page, amount shows adds to category.
    Operation shows in the bottom page section in Operation List.

    Precondition:
    - User uses valid login and password
    - One o more category exist in the list
    - Positive amount

    Expected Result:
    - Amount added to existing category in Temp Outcome list.
    - Added amount shows in Operation list.
    """)
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.operation_list
    @pytest.mark.parametrize("value", params_amount_values)
    def test_check_operation_list_temp_outcome(self, outcome_page, value):
        outcome_const = outcome_page(list_name="Временные", list_locator=CategoriesLocators.temp_dropdown,
                                     add_amount_field=CategoriesLocators.add_amount_to_category_field_temp,
                                     add_amount_btn=CategoriesLocators.add_amount_to_category_btn_temp
                                     )
        outcome_const.operation_add_amount(value)

    @allure.title("Delete Amount in Operation List")
    @allure.feature("Operation list")
    @allure.description("""
    Attempt to delete amount from Operation list. User click 'x' in the List item line.

    Precondition:
    - User uses valid login and password
    - One o more category exist in the list

    Expected Result:
    - Amount deleted from Operation list after user click 'x' in Item line in the list.
    """)
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.operation_list
    def test_check_operation_del_btn_outcome(self, outcome_page):
        outcome = outcome_page(btn_name_locator=OperationListLocators.oper_modal_delete_btn)
        outcome.operations_del(btn_name="delete")

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
    def test_check_operation_cancel_btn_outcome(self, outcome_page):
        outcome = outcome_page(btn_name_locator=OperationListLocators.oper_modal_cancel_btn)
        outcome.operations_del(btn_name="cancel")

    @allure.title("Edit Amount in Operation List")
    @allure.feature("Operation list")
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
    def test_check_operation_edit_btn_outcome(self, start_page, outcome_page):
        outcome = outcome_page()
        outcome.operation_edit_btn(randomize_float(10000))

    # ###########################CALENDAR########################################################

    @allure.title("Set current date in calendar (Outcome Page)")
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
    def test_calendar_current_btn_outcome(self, outcome_page):
        outcome = outcome_page()
        outcome.calendar_current_btn()

    @allure.title("Clear date in calendar (Outcome Page)")
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
    def test_calendar_clear_btn_outcome(self, outcome_page):
        outcome = outcome_page()
        outcome.calendar_clear_btn()
