import allure
import pytest
from TESTS.utils import randomize_latin_string
from PAGES.Locators import CategoriesLocators, OperationListLocators


@allure.suite("Saves Page")
class TestSavesPage:
    # ##########################CATEGORIES ADD###############################################
    @allure.title("Add new category to Saves list")
    @allure.feature("Dropdown list")
    @allure.description("""
    Attempt to add a new category to Saves list using the criteria:
    - New category name is less than 14 characters
    - New category name is not exist in the list

    Precondition:
    - User uses valid login and password

    Expected Result:
    - New category is added to Saves list.
    """)
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.dropdown_list
    def test_check_add_category_to_saves(self, saves_page):
        saves = saves_page(list_name="Накопления", list_locator=CategoriesLocators.saves_dropdown)
        saves.add_category(randomize_latin_string(10))

    # #########################CATEGORIES ERRORS CHECK############################################################

    @allure.title("Error Message in Modal Window When New Category Name Already Exists in the List (Saves)")
    @allure.feature("Dropdown errors")
    @allure.description("""
    An error message is shown in the modal window when the user tries to add a new category
    with a name that already exists in the Saves list.

    Precondition:
    - User uses valid login and password
    - Category name already exists in the Saves list

    Expected Result:
    - An error message is shown in the modal window when the user fills the proper field in the modal window
    trying to add a new income category which already exists in the Saves List.
    """)
    @allure.severity(allure.severity_level.MINOR)
    @pytest.mark.dropdown_list
    def test_check_exist_category_name_error_saves(self, saves_page):
        saves = saves_page(list_name="Накопления", list_locator=CategoriesLocators.saves_dropdown)
        saves.error_name_exist()

    @allure.title("Error Message in Modal Window When New Category Name Is More Than 14 Characters (Saves list)")
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
    def test_check_category_name_length_error_saves(self, saves_page):
        saves = saves_page(list_name="Накопления", list_locator=CategoriesLocators.saves_dropdown)
        saves.error_name_length(randomize_latin_string(15))

    # #########################CATEGORIES ERRORS CHECK REPEAT######################################################

    @allure.title("Length Error Message does not shows in Modal Window repeat open(Saves)")
    @allure.feature("Dropdown errors")
    @allure.description("""
    An exist error message is does not shows in the modal window when the user tries to add a new category
    with a name that more then 14 chars in Saves list then close window and repeat.

    Precondition:
    - User uses valid login and password
    - Category name is more then 14 chars

    Expected Result:
    - An error message does not shows in the modal window when the user fills the proper field in the modal window
    trying to add a new income category which already exists in Saves List,
    then close window and try again.
    """)
    @allure.severity(allure.severity_level.MINOR)
    @pytest.mark.dropdown_errors
    def test_check_length_error_repeat_saves(self, saves_page):
        saves = saves_page(list_name="Накопления", list_locator=CategoriesLocators.saves_dropdown)
        saves.repeat_error_name_length(randomize_latin_string(15))

    @allure.title("Exists Error Message does not shows in Modal Window repeat open (Saves)")
    @allure.feature("Dropdown list")
    @allure.description("""
    An exist error message is does not shows in the modal window when the user tries to add a new category
    with a name that already exists in Saves list then close window and repeat.

    Precondition:
    - User uses valid login and password
    - Category name already exists in Saves list

    Expected Result:
    - An error message does not shows in the modal window when the user fills the proper field in the modal window
    trying to add a new income category which already exists in Saves List,
    then close window and try again.
    """)
    @allure.severity(allure.severity_level.MINOR)
    @pytest.mark.dropdown_list
    def test_check_exist_error_repeat_saves(self, saves_page):
        saves = saves_page(list_name="Накопления", list_locator=CategoriesLocators.saves_dropdown)
        saves.repeat_error_name_exist()

    # #########################CATEGORIES DELETE ######################################################
    @allure.title("Archive Category from Saves list")
    @allure.feature("Dropdown Modal Actions")
    @allure.description("""
    Attempt to archive selected category from Saves list
    when user click 'Archive' button in modal window.

    Precondition:
    - User uses valid login and password
    - One o more category exist in the list

    Expected Result:
    - The selected category is archived from Saves list
    when user click 'Archive' button in modal window.
    """)
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.dropdown_modal_actions
    def test_check_archive_random_saves(self, saves_page):
        saves = saves_page(list_name="Накопления", list_locator=CategoriesLocators.saves_dropdown)
        saves.category_modal_action("В архив")

    @allure.title("Cancel Delete Category operation from Saves list")
    @allure.feature("Dropdown Modal Actions")
    @allure.description("""
    Attempt to cancel delete selected category operation from Saves list
    when user click 'Cancel' button in modal window.

    Precondition:
    - User uses valid login and password
    - One o more category exist in the list

    Expected Result:
    - The selected category is not deleted from Saves list
    when user click 'Cancel' button in modal window.
    """)
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.dropdown_modal_actions
    def test_check_cancel_random_saves(self, saves_page):
        saves = saves_page(list_name="Накопления", list_locator=CategoriesLocators.saves_dropdown)
        saves.category_modal_action("Отмена")

    @allure.title("Delete Category from Saves list")
    @allure.feature("Dropdown Modal Actions")
    @allure.description("""
    Attempt to delete selected category from Saves list
    when user click 'Delete' button in modal window.

    Precondition:
    - User uses valid login and password
    - One o more category exist in the list

    Expected Result:
    - The selected category is deleted from Saves list
    when user click 'Delete' button in modal window.
    """)
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.dropdown_modal_actions
    def test_check_delete_random_saves(self, saves_page):
        saves = saves_page(list_name="Накопления", list_locator=CategoriesLocators.saves_dropdown)
        saves.category_modal_action("Удалить")

    # ###########################CALENDAR########################################################

    @allure.title("Set current date in calendar (Saves Page)")
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
    def test_calendar_current_btn_saves(self, saves_page):
        saves = saves_page()
        saves.calendar_current_btn()

    @allure.title("Clear date in calendar (Saves Page)")
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
    def test_calendar_clear_btn_saves(self, saves_page):
        saves = saves_page()
        saves.calendar_clear_btn()
        

