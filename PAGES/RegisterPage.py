import time

from selenium.webdriver.common.by import By
from PAGES.StartPage import StartPage


class RegisterPage(StartPage):
    def __init__(self, driver):
        super().__init__(driver)

    register_email_field = (By.XPATH, "//input[@name='email']")
    register_login_field = (By.XPATH, "//input[@name='username']")
    register_pass_field = (By.XPATH, "//input[@name='password']")
    register_pass_confirm_field = (By.XPATH, "//input[@name='confirmPassword']")
    register_all_ready_link = (By.LINK_TEXT, "Я уже зарегистрирован")
    register_forward_btn = (By.XPATH, "//button[contains(text(),'Вперед')]")

    register_email_error = (By.XPATH, "//div[contains(text(),'Введен некорректный символ')]")
    register_email_error_empty = (By.XPATH, "//div[contains(text(),'Обязательное полe']")

    register_login_error_6 = (By.XPATH, "//div[contains(text(),'Логин должен состоять из 6 и более символов')]")
    register_login_error_32 = (By.XPATH, "//div[contains(text(),'Логин должен содержать от 6 до 32 символов')]")
    register_login_error_special = (By.XPATH, "//div[contains(text(),'Логин может содержать только латинские буквы "
                                                  "и цифры')]")

    register_pass_error_6 = (By.XPATH, "//div[contains(text(),'Пароль должен состоять из 6 из более символов, "
                                           "среди которых хотя бы одна буква верхнего регистра и хотя бы одна "
                                           "цифра')]")
    register_pass_error_incorrect = (By.XPATH, "//div[contains(text(),'Введен некорректный символ')]")
    register_pass_error_32 = (By.XPATH, "//div[contains(text(),'Не более 32 символов')]")

    register_pass_confirm_error = (By.XPATH, "//div[contains(text(),'Пароли не совпадают')]")

    register_existed_user = (By.XPATH, "//div[contains(text(),'Пользователь с логином qweqwe "
                                           "уже зарегистрирован')]")
    register_error_email = (By.XPATH, f"//div[contains(text(),'Пользователь с таким Email уже зарегистрирован')]")


    def register_check_already_registered_link(self):
        self.do_click("i all ready have registered link", self.register_all_ready_link)
        start = self.get_element(self.startpage_login_field)
        assert start.is_displayed()

    def register_field_validation(self, field_name, field_locator, value, expected_errors):
        result = None
        self.do_element_send_keys(field_name, field_locator, value)
        time.sleep(1)
        for error in expected_errors:
            if not self.wait_not_element_error(error):
                result = False
                break
            else:
                result = True
        return result

    def register_check_email_field_validation(self, val, expected):
        email_errors = [self.register_email_error, self.register_email_error_empty]
        assert expected == self.register_field_validation("Email field", self.register_email_field,
                                                          val, email_errors)

    def register_check_login_field_validation(self, val, expected):
        login_errors = [self.register_login_error_6, self.register_login_error_32,
                        self.register_login_error_special]
        assert expected == self.register_field_validation("Login field", self.register_login_field,
                                                          val, login_errors)

    def register_check_password_field_validation(self, val, expected):
        password_errors = [self.register_pass_error_6, self.register_pass_error_incorrect,
                           self.register_pass_error_32]
        assert expected == self.register_field_validation("Password field", self.register_pass_field,
                                                          val, password_errors)

    def register_check_verify_pass_confirm(self, val, expected, exp):
        self.register_check_password_field_validation(val, expected)

        if exp:
            val2 = val
        else:
            val2 = "123QWEqwe123321"

        self.do_element_send_keys("Password confirm field", self.register_pass_confirm_field, val2)
        assert self.wait_not_element_error(self.register_pass_confirm_error) == exp

    def register_check_exist_user(self, email, login, pwd):
        self.do_element_send_keys("Email field", self.register_email_field, email)
        self.do_element_send_keys("Login field", self.register_login_field, login)
        self.do_element_send_keys("Password field", self.register_pass_field, pwd)
        self.do_element_send_keys("COnfirm password field", self.register_pass_confirm_field, pwd)
        self.do_click("Forward button", self.register_forward_btn)
        register_error_login = (By.XPATH, f"//div[contains(text(),'Пользователь с логином {login} "
                                          "уже зарегистрирован')]")

        assert not self.wait_not_element_error(register_error_login) or \
               not self.wait_not_element_error(self.register_error_email)
