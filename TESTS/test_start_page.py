import allure
import pytest
from TESTS.settings import user_login, user_pass
from TESTS.params import params_start_page_login_invalid
from allure_commons.types import Severity


@allure.suite("Start Page")
class TestStartPage:
    @allure.title("Open Start Page")
    @allure.suite("Start Page")
    @allure.feature("Open Page")
    @allure.description("""
    Go to the start page of the website and verify the presence of essential elements.

    Precondition:
    - Navigate to the start page.

    Expected Result:
    - The start page opens successfully in the browser.
    - All necessary elements are visible.
    """)
    @allure.severity(Severity.BLOCKER)
    @pytest.mark.start_page
    def test_start_page_go_to_site(self, start_page):
        start_page.start_page_go_to_page()

    @allure.title("Start Page Login with Valid Credentials")
    @allure.suite("Start Page")
    @allure.feature("Login")
    @allure.description("""
    Attempt to log in using valid user credentials on the Start page.

    Precondition:
    - Navigate to the Start page.

    Expected Result:
    - Login with valid credentials passes.
    """)
    @allure.severity(Severity.NORMAL)
    @pytest.mark.start_page
    def test_start_page_login_valid(self, start_page):
        start_page.start_page_login(user_login, user_pass, False)

    @allure.title("Start Page Login with Invalid Credentials")
    @allure.suite("Start Page")
    @allure.feature("Login")
    @allure.description("""
    Attempt to log in using various combinations of invalid credentials on the Start page.

    Precondition:
    - Navigate to the Start page.

    Expected Result:
    - Login with invalid credentials fails.
    - The login error message is displayed for invalid login and/or password combinations and empty fields.
    """)
    @pytest.mark.parametrize("login, passwd, expected", params_start_page_login_invalid)
    @allure.severity(Severity.CRITICAL)
    @pytest.mark.start_page
    def test_start_page_login_invalid(self, start_page, login, passwd, expected):
        start_page.start_page_login(login, passwd, expected)
