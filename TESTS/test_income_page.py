import allure
import pytest

from TESTS.settings import user_login, user_pass
from TESTS.utils import randomize_latin_string
from TESTS.params import params_income_new_category_names_invalid


@allure.suite("Income Page")
class TestIncomePage:
    @allure.title("Add new category to Constant income")
    @allure.feature("Constant Incomes")
    @allure.description("""
    Attempt to add a new category using the criteria (New category name is less than 14 characters).

    Precondition:
    - User uses valid login and password.

    Expected Result:
    - New category is added to Constant income (DropList).
    """)
    @allure.severity(allure.severity_level.NORMAL)
    def test_income_check_add_new_category_to_constant_droplist(self, incomepage):
        incomepage.income_check_new_category_to_constant(user_login, user_pass, True, randomize_latin_string(10))

    @allure.title("'Add' Button Is Not Enabled When New Category Name Is More Than 14 Characters")
    @allure.feature("Constant Incomes")
    @allure.description("""
    'Add' button is not enabled when the user tries to add a new category to Constant Incomes
    with a name more than 14 characters.

    Precondition:
    - User uses valid login and password.
    - Category name more than 14 characters.

    Expected Result:
    - 'Add' button is not enabled in the modal window
    when the user tries to add a new category name more than 14 characters.
    """)
    @allure.severity(allure.severity_level.MINOR)
    @pytest.mark.parametrize("values", params_income_new_category_names_invalid)
    def test_income_check_add_new_category_to_constant_droplist_long_name_btn_not_enabled(self, incomepage, values):
        incomepage.income_check_new_category_to_constant_invalid(user_login, user_pass, True, values)

    @allure.title("Error Message in Modal Window When New Category Name Is More Than 14 Characters")
    @allure.feature("Constant Incomes")
    @allure.description("""
    An error message is shown in the modal window when the user tries to add a new category
    with a name that is more than 14 characters.

    Precondition:
    - User uses valid login and password.
    - Category name more than 14 characters.

    Expected Result:
    - An error message is shown in the modal window when the user fills the proper field in the modal window
    trying to add a new income category with a name more than 14 characters.
    """)
    @allure.severity(allure.severity_level.MINOR)
    @pytest.mark.parametrize("values", params_income_new_category_names_invalid[:2])
    def test_income_check_add_new_category_to_constant_droplist_long_name_error_msg(self, incomepage, values):
        incomepage.income_check_new_category_to_constant_error_msg(user_login, user_pass, True, values)

    @allure.title("Error Message in Modal Window When New Category Name Already Exists in the List")
    @allure.feature("Constant Incomes")
    @allure.description("""
    An error message is shown in the modal window when the user tries to add a new category
    with a name that already exists in the Constant Incomes list.

    Precondition:
    - User uses valid login and password.
    - Category name already exists in the Constant Incomes list.

    Expected Result:
    - An error message is shown in the modal window when the user fills the proper field in the modal window
    trying to add a new income category which already exists in the Constant Incomes List.
    """)
    @allure.severity(allure.severity_level.MINOR)
    def test_income_check_add_new_category_to_constant_droplist_exist_name_error_msg(self, incomepage):
        incomepage.income_check_new_category_to_constant_exist_name_error_msg(user_login, user_pass, True)

    @allure.title("Delete Category from Constant Income Droplist")
    @allure.feature("Constant Incomes")
    @allure.description("""
    Attempt to delete selected category from Constant Income Droplist
    when user click 'Delete' button in modal window.

    Precondition:
    - User uses valid login and password.

    Expected Result:
    - The selected category is deleted from Constant Income Droplist
    when user click 'Delete' button in modal window.
    """)
    @allure.severity(allure.severity_level.NORMAL)
    def test_income_check_delete_category_from_constant_droplist(self, incomepage):
        incomepage.income_check_delete_random_category_actions(user_login, user_pass, True, "delete")

    @allure.title("Archive Category from Constant Income Droplist")
    @allure.feature("Constant Incomes")
    @allure.description("""
        Attempt to archive selected category from Constant Income Droplist
        when user click 'Archive' button in modal window.

        Precondition:
        - User uses valid login and password.

        Expected Result:
        - The selected category is archived from Constant Income Droplist
        when user click 'Archive' button in modal window.
        """)
    @allure.severity(allure.severity_level.NORMAL)
    def test_income_check_archive_category_from_constant_droplist(self, incomepage):
        incomepage.income_check_delete_random_category_actions(user_login, user_pass, True, "archive")

    @allure.title("Cancel deleting Category from Constant Income Droplist")
    @allure.feature("Constant Incomes")
    @allure.description("""
            Attempt to cancel deleting selected category from Constant Income Droplist
            when user click 'Cancel' button in modal window.

            Precondition:
            - User uses valid login and password.

            Expected Result:
            - The selected category is not deleted from Constant Income Droplist
            when user click 'Cancel' button in modal window.
            """)
    @allure.severity(allure.severity_level.NORMAL)
    def test_income_check_cancel_delete_category_from_constant_droplist(self, incomepage):
        incomepage.income_check_delete_random_category_actions(user_login, user_pass, True, "cancel")
############################CALENDAR########################################################
    @pytest.mark.calendar_incomes
    def test_calendar_current_btn(self, incomepage):
        incomepage.income_check_calendar_current_btn(user_login, user_pass, True)

    @pytest.mark.calendar_incomes
    def test_calendar_clear_btn(self, incomepage):
        incomepage.income_check_calendar_clear_btn(user_login, user_pass, True)

    @pytest.mark.calendar_incomes
    def test_calendar_randome_date(self, incomepage):
        incomepage.income_check_calendar_random_date_current_month(user_login, user_pass, True)

############################CATEGORIES ADD###############################################
    @pytest.mark.dropdown_incomes
    def test_income_check_add_category_to_constant(self, incomepage):
        incomepage.income_check_add_category_to_constant(user_login, user_pass, True, 10, True)   #pass

    @pytest.mark.dropdown_incomes
    def test_income_check_add_category_to_temp(self, incomepage):
        incomepage.income_check_add_category_to_temp(user_login, user_pass, True, 10, True) #pass

##########################CATEGORIES ERRORS CHECK############################################################
    @pytest.mark.dropdown_incomes
    def test_income_check_exist_category_name_error_constant(self, incomepage):
        incomepage.income_check_exist_category_name_error_constant(user_login, user_pass, True, False) #pass

    @pytest.mark.dropdown_incomes
    def test_income_check_exist_category_name_error_temp(self, incomepage):
        incomepage.income_check_exist_category_name_error_temp(user_login, user_pass, True, False) #pass

    @pytest.mark.dropdown_incomes
    def test_income_check_exist_category_length_error_constant(self, incomepage):
        incomepage.income_check_category_name_length_error_constant(user_login, user_pass, True, 15, False) #pass

    @pytest.mark.dropdown_incomes
    def test_income_check_exist_category_length_error_temp(self, incomepage):
        incomepage.income_check_category_name_length_error_temp(user_login, user_pass, True, 15, False) #pass

##########################CATEGORIES ERRORS CHECK REPEAT######################################################

    @pytest.mark.dropdown_incomes
    def test_income_check_length_error_repeat_constant(self, incomepage):
        incomepage.income_check_length_error_repeat_constant(user_login, user_pass, True, 15, False) #pass

    @pytest.mark.dropdown_incomes
    def test_income_check_exist_error_repeat_constant(self, incomepage):
        incomepage.income_check_exist_error_repeat_constant(user_login, user_pass, True, False) #pass

    @pytest.mark.dropdown_incomes
    def test_income_check_length_error_repeat_temp(self, incomepage):
        incomepage.income_check_length_error_repeat_temp(user_login, user_pass, True, 15, False) #pass

    @pytest.mark.dropdown_incomes
    def test_income_check_exist_error_repeat_temp(self, incomepage):
        incomepage.income_check_exist_error_repeat_temp(user_login, user_pass, True, False)

    ##########################CATEGORIES DELETE ######################################################
    @pytest.mark.delete_incomes
    def test_income_check_archive_random_constant(self, incomepage):
        incomepage.income_check_random_archive(user_login, user_pass, True)

    @pytest.mark.delete_incomes
    def test_income_check_cancel_random_constant(self, incomepage):
        incomepage.income_check_random_cancel(user_login, user_pass, True)

    @pytest.mark.delete_incomes
    def test_income_check_delete_random_constant(self, incomepage):
        incomepage.income_check_random_delete(user_login, user_pass, True)

    @pytest.mark.delete_incomes
    def test_income_check_archive_random_temp(self, incomepage):
        incomepage.income_check_random_archive_temp(user_login, user_pass, True)

    @pytest.mark.delete_incomes
    def test_income_check_cancel_random_temp(self, incomepage):
        incomepage.income_check_random_cancel_temp(user_login, user_pass, True)

    @pytest.mark.delete_incomes
    def test_income_check_delete_random_temp(self, incomepage):
        incomepage.income_check_random_delete_temp(user_login, user_pass, True)

    ##########################-ADD AMOUNT-######################################################

    def test_income_check_add_value_conctant(self, incomepage):
        incomepage.income_check_add_value_conctant(user_login, user_pass, True, 10000)

