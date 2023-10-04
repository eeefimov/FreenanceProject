import allure
import pytest

from TESTS.settings import user_login, user_pass
from TESTS.utils import randomize_number
from TESTS.params import params_income_new_category_names_invalid


@allure.suite("Income Page")
class TestIncomePage:

    # ###########################CALENDAR########################################################

    @allure.title("Set current date in calendar")
    @allure.feature("Incomes Calendar")
    @allure.description("""
    Attempt to set current date in calendar using "Today" button:

    Precondition:
    - User uses valid login and password

    Expected Result:
    - Current date set in calendar when user click 'Today' button in calendar.
    """)
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.calendar_incomes
    def test_calendar_current_btn(self, incomepage):
        incomepage.income_check_calendar_current_btn(user_login, user_pass, True)

    @allure.title("Clear date in calendar")
    @allure.feature("Incomes Calendar")
    @allure.description("""
    Attempt to clear date in calendar using "Clear" button:

    Precondition:
    - User uses valid login and password

    Expected Result:
    - Current date cleared in calendar when user click 'Clear' button in calendar.
    """)
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.calendar_incomes
    def test_calendar_clear_btn(self, incomepage):
        incomepage.income_check_calendar_clear_btn(user_login, user_pass, True)

    @allure.title("Set random date in calendar")
    @allure.feature("Incomes Calendar")
    @allure.description("""
      Attempt to set random date in calendar:

      Precondition:
      - User uses valid login and password

      Expected Result:
      - Random date set in calendar.
      """)
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.calendar_incomes
    def test_calendar_randome_date(self, incomepage):
        incomepage.income_check_calendar_random_date_current_month(user_login, user_pass, True)

    # ###########################CATEGORIES ADD###############################################
    @allure.title("Add new category to Constant income")
    @allure.feature("Incomes dropdown list")
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
    @pytest.mark.dropdown_incomes
    def test_income_check_add_category_to_constant(self, incomepage):
        incomepage.income_check_add_category_to_constant(user_login, user_pass, True, 10, True)

    @allure.title("Add new category to Temp income")
    @allure.feature("Incomes dropdown list")
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
    @pytest.mark.dropdown_incomes
    def test_income_check_add_category_to_temp(self, incomepage):
        incomepage.income_check_add_category_to_temp(user_login, user_pass, True, 10, True)

    # #########################CATEGORIES ERRORS CHECK############################################################

    @allure.title("Error Message in Modal Window When New Category Name Already Exists in the List (Constant)")
    @allure.feature("Incomes dropdown list")
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
    @pytest.mark.dropdown_incomes
    def test_income_check_exist_category_name_error_constant(self, incomepage):
        incomepage.income_check_exist_category_name_error_constant(user_login, user_pass, True, False)

    @allure.title("Error Message in Modal Window When New Category Name Already Exists in the List (Temp)")
    @allure.feature("Incomes dropdown list")
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
    @pytest.mark.dropdown_incomes
    def test_income_check_exist_category_name_error_temp(self, incomepage):
        incomepage.income_check_exist_category_name_error_temp(user_login, user_pass, True, False)

    @allure.title("Error Message in Modal Window When New Category Name Is More Than 14 Characters (Constant list)")
    @allure.feature("Incomes dropdown list")
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
    @pytest.mark.dropdown_incomes
    def test_income_check_category_name_length_error_constant(self, incomepage):
        incomepage.income_check_category_name_length_error_constant(user_login, user_pass, True, 15, False)

    @allure.title("Error Message in Modal Window When New Category Name Is More Than 14 Characters (Temp list)")
    @allure.feature("Incomes dropdown list")
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
    @pytest.mark.dropdown_incomes
    def test_income_check_category_name_length_error_temp(self, incomepage):
        incomepage.income_check_category_name_length_error_temp(user_login, user_pass, True, 15, False)

    # #########################CATEGORIES ERRORS CHECK REPEAT######################################################

    @allure.title("Length Error Message does not shows in Modal Window repeat open(Constant)")
    @allure.feature("Incomes dropdown list")
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
    @pytest.mark.dropdown_incomes
    def test_income_check_length_error_repeat_constant(self, incomepage):
        incomepage.income_check_length_error_repeat_constant(user_login, user_pass, True, 15, False)

    @allure.title("Length Error Message does not shows in Modal Window repeat open(Temp)")
    @allure.feature("Incomes dropdown list")
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
    @pytest.mark.dropdown_incomes
    def test_income_check_length_error_repeat_temp(self, incomepage):
        incomepage.income_check_length_error_repeat_temp(user_login, user_pass, True, 15, False)

    @allure.title("Exists Error Message does not shows in Modal Window repeat open(Constant)")
    @allure.feature("Incomes dropdown list")
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
    @pytest.mark.dropdown_incomes
    def test_income_check_exist_error_repeat_constant(self, incomepage):
        incomepage.income_check_exist_error_repeat_constant(user_login, user_pass, True, False)

    @allure.title("Exists Error Message does not shows in Modal Window repeat open(Temp)")
    @allure.feature("Incomes dropdown list")
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
    @pytest.mark.dropdown_incomes
    def test_income_check_exist_error_repeat_temp(self, incomepage):
        incomepage.income_check_exist_error_repeat_temp(user_login, user_pass, True, False)

    # #########################CATEGORIES DELETE ######################################################
    @allure.title("Archive Category from Constant Income list")
    @allure.feature("Incomes dropdown list")
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
    @pytest.mark.delete_incomes
    def test_income_check_archive_random_constant(self, incomepage):
        incomepage.income_check_random_archive_constant(user_login, user_pass, True)

    @allure.title("Archive Category from Temp Income list")
    @allure.feature("Incomes dropdown list")
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
    @pytest.mark.delete_incomes
    def test_income_check_archive_random_temp(self, incomepage):
        incomepage.income_check_random_archive_temp(user_login, user_pass, True)

    @allure.title("Cancel Delete Category operation from Constant Income list")
    @allure.feature("Incomes dropdown list")
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
    @pytest.mark.delete_incomes
    def test_income_check_cancel_random_constant(self, incomepage):
        incomepage.income_check_random_cancel_constant(user_login, user_pass, True)

    @allure.title("Cancel Delete Category operation from Temp Income list")
    @allure.feature("Incomes dropdown list")
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
    @pytest.mark.delete_incomes
    def test_income_check_cancel_random_temp(self, incomepage):
        incomepage.income_check_random_cancel_temp(user_login, user_pass, True)

    @allure.title("Delete Category from Constant Income list")
    @allure.feature("Incomes dropdown list")
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
    @pytest.mark.delete_incomes
    def test_income_check_delete_random_constant(self, incomepage):
        incomepage.income_check_random_delete_constant(user_login, user_pass, True)

    @allure.title("Delete Category from Temp Income list")
    @allure.feature("Incomes dropdown list")
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
    @pytest.mark.delete_incomes
    def test_income_check_delete_random_temp(self, incomepage):
        incomepage.income_check_random_delete_temp(user_login, user_pass, True)

    # #########################-ADD AMOUNT-######################################################
    @allure.title("Add Amount to exist Category in Constant Income list")
    @allure.feature("Incomes dropdown list")
    @allure.description("""
    Attempt to add random amount to exist category in Constant Income list.

    Precondition:
    - User uses valid login and password
    - One o more category exist in the list
    - Positive amount 

    Expected Result:
    - Amount added to existing category in Constant Income list.
    """)
    @allure.severity(allure.severity_level.CRITICAL)
    def test_income_check_add_value_conctant(self, incomepage):
        incomepage.income_check_add_value_constant(user_login, user_pass, True, randomize_number(100000))

    @allure.title("Add Amount to exist Category in Temp Income list")
    @allure.feature("Incomes dropdown list")
    @allure.description("""
    Attempt to add random amount to exist category in Temp Income list.

    Precondition:
    - User uses valid login and password
    - One o more category exist in the list
    - Positive amount 

    Expected Result:
    - Amount added to existing category in Temp Income list.
    """)
    @allure.severity(allure.severity_level.CRITICAL)
    def test_income_check_add_value_temp(self, incomepage):
        incomepage.income_check_add_value_temp(user_login, user_pass, True, randomize_number(100000))

    #########################-OPERATION LIST-######################################################

    @allure.title("Shows Added Amount in Operation List (Constant)")
    @allure.feature("Incomes Operation list")
    @allure.description("""
    Attempt to add random amount to exist category in Constant Income list.
    After user click "Add" button on the page, amount shows adds to category.
    Operation shows in the bottom page section in Operation List.

    Precondition:
    - User uses valid login and password
    - One o more category exist in the list
    - Positive amount

    Expected Result:
    - Amount added to existing category in Constant Income list.
    - Added amount shows in Operation list.
    """)
    @allure.severity(allure.severity_level.NORMAL)
    def test_income_check_operation_list_constant(self, incomepage):
        incomepage.income_check_operation_constant(user_login, user_pass, True, randomize_number(100000))

    @allure.title("Shows Added Amount in Operation List (Constant)")
    @allure.feature("Incomes Operation list")
    @allure.description("""
    Attempt to add random amount to exist category in Constant Income list.
    After user click "Add" button on the page, amount shows adds to category.
    Operation shows in the bottom page section in Operation List.

    Precondition:
    - User uses valid login and password
    - One o more category exist in the list
    - Positive amount

    Expected Result:
    - Amount added to existing category in Constant Income list.
    - Added amount shows in Operation list.
    """)
    @allure.severity(allure.severity_level.NORMAL)
    def test_income_check_operation_list_temp(self, incomepage):
        incomepage.income_check_operation_temp(user_login, user_pass, True, randomize_number(10000))

    @allure.title("Delete Amount in Operation List")
    @allure.feature("Incomes Operation list")
    @allure.description("""
    Attempt to delete amount from Operation list. User clic 'x' in the List item line.

    Precondition:
    - User uses valid login and password
    - One o more category exist in the list

    Expected Result:
    - Amount deleted from Operation list after user click 'x' in Item line in the list.
    """)
    @allure.severity(allure.severity_level.NORMAL)
    def test_income_check_operation_del_btn(self, incomepage):
        incomepage.income_check_operation_x_del_btn(user_login, user_pass, True)

    @allure.title("Cancel Deleting Amount in Operation List")
    @allure.feature("Incomes Operation list")
    @allure.description("""
    Attempt to delete amount from Operation list. User clic 'x' in the List item line.

    Precondition:
    - User uses valid login and password
    - One o more category exist in the list

    Expected Result:
    - Amount deleted from Operation list after user click 'x' in Item line in the list.
    """)
    @allure.severity(allure.severity_level.NORMAL)
    def test_income_check_operation_cancel_btn(self, incomepage):
        incomepage.income_check_operation_x_cancel_btn(user_login, user_pass, True)

    @allure.title("Edit Amount in Operation List")
    @allure.feature("Incomes Operation list")
    @allure.description("""
    Attempt to edit amount in Operation list. User clic 'edit' icon in the List item line.

    Precondition:
    - User uses valid login and password
    - One o more category exist in the list

    Expected Result:
    - Amount edited and updated in Operation list after user click 'edit' icon in Item line in the list.
    """)
    def test_income_check_operation_edit_btn(self, incomepage):
        incomepage.income_check_operation_edit_btn(user_login, user_pass, True)