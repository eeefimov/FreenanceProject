import allure
from selenium.webdriver.support.ui import WebDriverWait as WdW
from selenium.webdriver.support import expected_conditions as Ec
from selenium.common import ElementNotVisibleException, NoSuchElementException, \
    TimeoutException, StaleElementReferenceException
from selenium.common.exceptions import WebDriverException


class Main:
    def __init__(self, driver, timeout = 1):
        self.driver = driver
        self.base_url = "https://dev.freenance.store/"
        self.driver.implicitly_wait(timeout)

    def go_to_site(self) -> None:
        with allure.step(f"Go to site: {self.base_url}"):
            try:
                self.driver.get(self.base_url)
            except WebDriverException:
                print("PAGE DOWN")

    def wait_exaption(self):
        """
        Creates and returns a WebDriverWait instance with custom exceptions.
        """
        wait = WdW(self.driver, timeout=5, poll_frequency=1,
                   ignored_exceptions=[ElementNotVisibleException, NoSuchElementException,
                                       TimeoutException, StaleElementReferenceException])
        return wait

    def wait_element(self, by_locator) -> bool:
        try:
            wait = self.wait_exaption()
            wait.until(Ec.presence_of_element_located(by_locator))
            return True
        except TimeoutException:
            return False

    def get_element(self, by_locator):
        handle_element = self.wait_exaption()
        if handle_element:
            element = WdW(self.driver, timeout=10, poll_frequency=1.5).until(Ec.visibility_of_element_located(by_locator))
            return element

    def do_click(self, name_element: str, by_locator):
        with allure.step(f"Click '{name_element}'"):
            element = self.get_element(by_locator)
            element.click()

    def do_element_send_keys(self, locator_name: str, by_locator, text_keys):
        with allure.step(f"Send {text_keys} to {locator_name} field"):
            element = self.get_element(by_locator)
            element.send_keys(text_keys)

    def wait_not_element_error(self, by_locator) -> bool:
        """
        Waits for an element identified by the given locator to disappear.
        """
        try:
            wait = self.wait_exaption()
            wait.until_not(Ec.presence_of_element_located(by_locator))
            return True
        except TimeoutException:
            return False

    def get_elements_from_list(self, values_locator, attribute: str) -> list:
        list_items = self.driver.find_elements(*values_locator)
        list_of_indexes = []
        for item in list_items:
            list_of_indexes.append(item.get_attribute(attribute))

        return list_of_indexes

