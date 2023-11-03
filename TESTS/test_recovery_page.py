import allure
import pytest
from allure_commons.types import Severity
from TESTS.params import params_recovery_page_email_validation


@allure.suite("Recovery Page")
class TestRecoveryPage:
    @allure.title("Open Recovery Page")
    @allure.feature("Recovery")
    @allure.description("""
    Redirect to the recovery page after 'password recovery' click on start page. 

    Precondition:
    - Navigate to the start page.

    Expected Result:
    - The recovery page opens successfully in the browser.
    - All necessary elements are visible.
    """)
    @allure.severity(Severity.BLOCKER)
    @pytest.mark.recovery_page
    def test_recovery_page_go_to_site(self, recovery_page):
        recovery_page.start_page_redirect("recovery")

    @allure.title("Check Recovery Return link")
    @allure.feature("Return link")
    @allure.description("""
    Redirect back to start page after 'return back' link click.

    Precondition:

    Expected Result:
    - User redirected back to start page after 'return back' link click.
    """)
    @allure.severity(Severity.NORMAL)
    @pytest.mark.recovery_page
    def test_recovery_check_return_link(self, recovery_page):
        recovery_page.recovery_check_return_link()

    @allure.title("Check Recovery Email validation")
    @allure.feature("Email validation")
    @allure.description("""
    If user setup invalid values or empty to Email field in recovery page 
    error message shows 'Обязательное поле' or 'Введёт некорректный email'.

    Params:
    - Empty field
    - Wrong email (unregistered in the system)

    Expected Result:
    - After user filed email field in recovery form and click 'Recovery' button
    error message shows up ('Обязательное поле' or 'Введёт некорректный email')
    """)
    @allure.severity(Severity.NORMAL)
    @pytest.mark.recovery_page
    @pytest.mark.parametrize("value, expected", params_recovery_page_email_validation)
    def test_recovery_check_email_validation(self, recovery_page, value, expected):
        recovery_page.recovery_check_email_validation(value, expected)

    @allure.title("Check Recovery Send Email confirm msg")
    @allure.feature("Send Email confirm msg")
    @allure.description("""
    Check Notification message shows up, when user setup valid Email to Email field
    and press 'Восстановить' button.

    Params:
    - Valid email

    Expected Result:
    - Notification message is shows up, when user setup valid Email to Email field
    and press 'Восстановить' button.
    """)
    @allure.severity(Severity.NORMAL)
    @pytest.mark.recovery_page
    def test_recovery_check_send_mail_msg(self, recovery_page):
        recovery_page.recovery_check_send_mail_msg()