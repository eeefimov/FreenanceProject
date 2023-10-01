from PAGES.main import Main


class CalendarManager(Main):
    def __init__(self, driver):
        super().__init__(driver)

    def set_calendar(self, select_data: str, select_date_locator):
        self.do_element_click(select_data, select_date_locator)

    def set_date(self, date_selector: str, date_btn_locator, month_locator):
        self.do_element_click(date_selector, date_btn_locator)
        dt = self.get_element(month_locator)
        return dt.get_attribute("value")


