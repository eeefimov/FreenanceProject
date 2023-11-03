from selenium.webdriver.common.by import By
from PAGES.StartPage import StartPage
from TESTS.settings import user_email


class RecoveryPage(StartPage):
    def __init__(self, driver):
        super().__init__(driver)

    recovery_email_field = (By.XPATH, "//div[@class='App']//input")
    recovery_forward_btn = (By.XPATH, "//div[@class='App']//button")
    recovery_return_link = (By.XPATH, "//div[@class='App']//a")

    recovery_email_error = (By.XPATH, "//div[contains(text(),'Обязательное поле')]")
    recovery_email_error_incorect = (By.XPATH, "//div[contains(text(),'Введёт некорректный email')]")
    recovery_email_send_msg = (By.XPATH, "//div[contains(text(),'На указанный вами адрес почты отправлено письмо дл')]")

    def recovery_check_return_link(self):
        self.start_page_redirect("recovery")
        self.do_click("return back", self.recovery_return_link)
        login_field = self.get_element(self.startpage_login_field)
        assert login_field.is_displayed()

    def recovery_check_email_validation(self, value, expected):
        self.start_page_redirect("recovery")
        self.do_element_send_keys("Email field", self.recovery_email_field, value)
        self.do_click("'Forward' button", self.recovery_forward_btn)

        if not expected:
            if self.wait_not_element_error(self.recovery_email_error) == expected:
                if self.wait_not_element_error(self.recovery_email_error_incorect):
                    assert True
            else:
                if self.wait_not_element_error(self.recovery_email_error_incorect) == expected:
                    assert True

    def recovery_check_send_mail_msg(self):
        self.start_page_redirect("recovery")
        self.do_element_send_keys("Email field", self.recovery_email_field, user_email)
        self.do_click("'Forward' button", self.recovery_forward_btn)
        assert self.wait_element(self.recovery_email_send_msg)
