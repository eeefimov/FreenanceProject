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

    # @allure.title("Add new category (valid name length)")
    # def test_income_check_constant_add_category_valid(self, incomepage):
    #     param = params_income_new_category_names_valid[0]
    #     category_name = param.values[0]
    #     incomepage.income_check_add_category_to_droplist_valid(user_login, user_pass, True, True, category_name)
    #
    # @allure.title("Error message show when add new category of Constant income with name length more then 14 chars")
    # @allure.description("""
    #              Attempt to add new category using criteria (category name is less then 14 chars).
    #              Display error message in modal window when user add new category name to the proper edit field.
    #              New category name is more then 14 chars.
    #
    #              Precondition:
    #              - User use valid login and password.
    #
    #              Expected Result:
    #              - Error message displayed in modal windows when user added new category of Constant Income
    #              with name more then 14 chars.
    #          """)
    # def test_income_check_add_category_length_name_error(self, incomepage):
    #     param = params_income_new_category_names_invalid[0]
    #     category_name = param.values[0]
    #     incomepage.income_check_add_category_length_name_error(user_login, user_pass, True, False, category_name)
    #
    # @allure.title("Add new category to Constant income INVALID")
    # @allure.description("""
    #          Attempt to add new category using criteria (category name is less then 14 chars).
    #          If income's name more then 14 chars category do not add to Constant Income list.
    #
    #          Precondition:
    #          - User use valid login and password.
    #          - Category's name more then 14 chars.
    #
    #          Expected Result:
    #          - New category do not added to Constant income (DropList)
    #      """)
    # @pytest.mark.parametrize("new_categoty", params_income_new_category_names_invalid)
    # def test_income_check_constant_add_category_invalid(self, incomepage, new_categoty):
    #     incomepage.income_check_add_category_to_droplist_valid(user_login, user_pass, True, False, new_categoty)
    #
    #
    # @allure.title("Add category Close modal window using x")
    # @allure.description("""
    #          Close modal window using 'x' when user try to add new category to Constant Income.
    #
    #          Precondition:
    #          - User use valid login and password.
    #
    #          Expected Result:
    #          - Modal window close after click to 'x'.
    #          - New category did not add to Constant Incomes list.
    #      """)
    # @allure.title("Chec cancel X add new category")
    # def test_income_check_add_category_to_droplist_cancel_x(self, incomepage):
    #     incomepage.income_check_add_category_to_droplist_cancel_x(user_login, user_pass, 10, True, False)
    #
    # def test_income_check_position(self, incomepage):
    #     incomepage.income_check_position(user_login, user_pass, True)
