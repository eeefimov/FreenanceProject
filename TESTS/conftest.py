import time

import allure
import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from PAGES.PagesMain import PagesMain
from PAGES.StartPage import StartPage
from PAGES.SavesPage import SavesPage
from PAGES.RecoveryPage import RecoveryPage
from PAGES.RegisterPage import RegisterPage
from TESTS.settings import user_login, user_pass
from PAGES.Locators import PageLinks
import datetime

@pytest.fixture(scope="function")
def browser():
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--incognito")
    options.add_argument('--disable-blink-features=AutomationControlled')
    options.add_argument('--user-data-dir=tmp/chrome_profile')
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")
    options.add_argument("--start-maximized")
    driver = webdriver.Chrome(options=options)
    driver.delete_all_cookies()
    driver.set_window_size(1280, 1024)

    yield driver

    time.sleep(1)
    attach = driver.get_screenshot_as_png()
    allure.attach(attach, name=f"Screenshot {datetime.datetime}", attachment_type=allure.attachment_type.PNG)
    browser_logs = driver.get_log("browser")
    allure.attach(str(browser_logs), name="Browser Logs", attachment_type=allure.attachment_type.TEXT)

    driver.quit()


@pytest.fixture(scope="function")
def start_page(browser):
    start = StartPage(browser)
    return start


@pytest.fixture(scope="function")
def income_page(browser, start_page):
    def create_income_page(list_name=None, list_locator=None, add_amount_field=None,
                           add_amount_btn=None, btn_name_locator=None):
        income = PagesMain(browser, list_name, list_locator,
                 add_amount_field, add_amount_btn, btn_name_locator)
        start_page.start_page_login(user_login, user_pass, True)
        return income
    return create_income_page


@pytest.fixture(scope="function")
def outcome_page(browser, start_page):
    def create_outcome_page(list_name=None, list_locator=None, add_amount_field=None,
                           add_amount_btn=None, btn_name_locator=None):
        outcome = PagesMain(browser, list_name, list_locator,
                 add_amount_field, add_amount_btn, btn_name_locator)
        start_page.start_page_login(user_login, user_pass, True)
        start_page.do_click("Outcome", PageLinks.outcome_link_btn)
        time.sleep(1)
        return outcome
    return create_outcome_page


@pytest.fixture(scope="function")
def saves_page(browser, start_page):
    def create_saves_page(list_name=None, list_locator=None, add_amount_field=None,
                           add_amount_btn=None, btn_name_locator=None):
        saves = PagesMain(browser, list_name, list_locator,
                 add_amount_field, add_amount_btn, btn_name_locator)
        start_page.start_page_login(user_login, user_pass, True)
        start_page.do_click("Saves", PageLinks.saves_link_btn)
        time.sleep(1)
        return saves
    return create_saves_page


@pytest.fixture(scope="function")
def recovery_page(browser):
    recovery = RecoveryPage(browser)
    return recovery


@pytest.fixture(scope="function")
def register_page(browser, start_page):
    start_page.start_page_redirect("register")
    register = RegisterPage(browser)
    return register


