import time
import random
from PAGES.Main import Main
from PAGES.Features.DropDownManager import DropDownManager
from PAGES.Features.OperationManager import OperationManager
from PAGES.Locators import CalendarLocators, CategoriesLocators, OperationListLocators
from TESTS.utils import current_date, calendar_date

#NEW TRY!!!!!!!!


class PagesMain(Main):

    def __init__(self, driver, list_name=None, list_locator=None,
                 add_amount_field = None, add_amount_btn = None,
                 btn_name_locator = None):
        super().__init__(driver)
        self.list_name = list_name
        self.list_locator = list_locator
        self.add_amount_field = add_amount_field
        self.add_amount_btn = add_amount_btn
        self.btn_name_locator = btn_name_locator

    # ################-Categories-#####################################################################################
    def add_category(self, name):
        self.do_click(self.list_name, self.list_locator)
        self.do_click("Добавить категорию", CategoriesLocators.list_add_value_btn)
        time.sleep(1)
        self.do_element_send_keys(locator_name="Название категории",
                                  by_locator=CategoriesLocators.modal_window_add_name_value_field,
                                  text_keys=name
                                  )
        self.do_click(name_element="Добавить", by_locator=CategoriesLocators.modal_window_add_name_value_btn)
        time.sleep(2)

        self.do_click(self.list_name, self.list_locator)
        time.sleep(1)
        assert DropDownManager.check_added_value_in_category(self, name, CategoriesLocators.list_elements)

    def error_name_length(self, name):
        self.do_click(self.list_name, self.list_locator)
        self.do_click("Добавить категорию", CategoriesLocators.list_add_value_btn)
        time.sleep(1)
        self.do_element_send_keys(locator_name="Название категории",
                                  by_locator=CategoriesLocators.modal_window_add_name_value_field,
                                  text_keys=name
                                  )
        self.do_click(name_element="Добавить", by_locator=CategoriesLocators.modal_window_add_name_value_btn)
        time.sleep(1)

        assert self.wait_element(by_locator=CategoriesLocators.length_error)

    def error_name_exist(self):
        self.do_click(self.list_name, self.list_locator)
        exist_name = DropDownManager.get_exist_name_from_the_list(self,
                                                                  list_values_locator=CategoriesLocators.list_elements)
        self.do_click("Добавить категорию", CategoriesLocators.list_add_value_btn)
        time.sleep(1)

        self.do_element_send_keys(locator_name="Название категории",
                                  by_locator=CategoriesLocators.modal_window_add_name_value_field,
                                  text_keys=exist_name
                                  )
        self.do_click("Добавить", CategoriesLocators.modal_window_add_name_value_btn)
        time.sleep(1)

        assert self.wait_element(by_locator=CategoriesLocators.exist_name_error)

    def repeat_error_name_length(self, name):
        self.do_click(self.list_name, self.list_locator)
        self.do_click("Добавить категорию", CategoriesLocators.list_add_value_btn)
        time.sleep(1)
        self.do_element_send_keys(locator_name="Название категории",
                                  by_locator=CategoriesLocators.modal_window_add_name_value_field,
                                  text_keys=name
                                  )
        self.do_click("x", CategoriesLocators.modal_window_add_x_btn)
        time.sleep(1)

        self.do_click(self.list_name, self.list_locator)
        self.do_click("Добавить категорию", CategoriesLocators.list_add_value_btn)
        time.sleep(1)

        assert self.wait_not_element_error(CategoriesLocators.length_error)

    def repeat_error_name_exist(self):
        self.do_click(self.list_name, self.list_locator)
        exist_name = DropDownManager.get_exist_name_from_the_list(self,
                                                                  list_values_locator=CategoriesLocators.list_elements)
        self.do_click("Добавить категорию", CategoriesLocators.list_add_value_btn)
        time.sleep(1)

        self.do_element_send_keys(locator_name="Название категории",
                                  by_locator=CategoriesLocators.modal_window_add_name_value_field,
                                  text_keys=exist_name
                                  )
        self.do_click("Добавить", CategoriesLocators.modal_window_add_name_value_btn)
        time.sleep(1)

        self.do_click("x", CategoriesLocators.modal_window_add_x_btn)
        time.sleep(1)

        self.do_click(self.list_name, self.list_locator)
        self.do_click("Добавить категорию", CategoriesLocators.list_add_value_btn)

        assert self.wait_not_element_error(CategoriesLocators.exist_name_error)

    def category_modal_action(self, action_name):
        self.do_click(self.list_name, self.list_locator)
        element_index = random.choice(self.get_elements_from_list(values_locator=CategoriesLocators.list_elements,
                                                                  attribute="index"))
        name = (self.get_element(DropDownManager.list_selected_element(element_index))).text
        print(name)

        del_btn_locator = DropDownManager.list_selected_del_btn(element_index)
        self.do_click('x', del_btn_locator)
        time.sleep(2)

        self.do_click(action_name, DropDownManager.modal_action(action_name))
        time.sleep(2)

        if action_name == "Отмена":
            ls_locator = DropDownManager.set_selected_name_locator(name)
            self.do_click(self.list_name, ls_locator)

        if action_name == "Удалить" or "В архив":
            time.sleep(1)
            assert not DropDownManager.check_added_value_in_category(self,
                                                                     name=name,
                                                                     list_items=CategoriesLocators.list_elements
                                                                     )
        else:
            assert DropDownManager.check_added_value_in_category(self,
                                                                 name=name,
                                                                 list_items=CategoriesLocators.list_elements
                                                                 )

    # ################-OPERATION List-############################

    def operation_add_amount(self, amount):
        self.do_click(self.list_name, self.list_locator)
        time.sleep(1)

        item_index = random.choice(self.get_elements_from_list(values_locator=CategoriesLocators.list_elements,
                                                               attribute="index"))
        item_locator = DropDownManager.set_selected_index_locator(item_index)
        self.do_click("Random item", item_locator)
        time.sleep(1)

        self.do_element_send_keys("Amount field", self.add_amount_field, amount)
        time.sleep(1)

        self.do_click("Add", self.add_amount_btn)
        time.sleep(2)

        item_id = max(self.get_elements_from_list(values_locator=OperationListLocators.oper_list_values,
                                                  attribute="id"))
        last_operation_locator = OperationManager.operation_list_check_amount(item_id)
        added_amount = self.get_element(last_operation_locator)
        assert amount == OperationManager.check_amount(added_amount.text)

    def operations_del(self, btn_name):
        time.sleep(1)

        item_id = max(self.get_elements_from_list(values_locator=OperationListLocators.oper_list_values,
                                                  attribute="id"))
        btn_locator = OperationManager.operation_list_btn(btn_name=btn_name,
                                                          item_id=item_id
                                                          )
        self.do_click("x", btn_locator)
        time.sleep(2)

        if btn_name == "delete" or "cancel":
            self.do_click(btn_name, self.btn_name_locator)
            time.sleep(2)

        updated_id = max(self.get_elements_from_list(values_locator=OperationListLocators.oper_list_values,
                                                     attribute="id"))
        if btn_name == "delete":
            assert updated_id != item_id
        elif btn_name == "cancel":
            assert updated_id == item_id

    def operation_edit_btn(self, amount):
        time.sleep(2)

        item_id = max(self.get_elements_from_list(values_locator=OperationListLocators.oper_list_values,
                                                  attribute="id"))
        btn_locator = OperationManager.operation_list_btn(btn_name="edit",
                                                          item_id=item_id
                                                          )
        self.do_click("edit", btn_locator)
        time.sleep(2)

        edit_field = self.get_element(OperationListLocators.oper_modal_edit_field)
        edit_field.clear()
        time.sleep(1)

        self.do_element_send_keys("Field with old amount",
                                  OperationListLocators.oper_modal_edit_field,
                                  amount
                                  )
        self.do_click("Add", OperationListLocators.oper_modal_add_btn)
        time.sleep(2)

        amount_locator = OperationManager.operation_list_check_amount(item_id=item_id)
        new = self.get_element(amount_locator)
        assert amount == OperationManager.check_amount(new.text)

    # ################-Calendar-##################################

    def calendar_current_btn(self):
        time.sleep(1)

        self.do_click("Выбор даты", CalendarLocators.calendar)
        time.sleep(2)

        self.do_click("Сегодня", CalendarLocators.calendar_today_btn)
        today = self.get_element(CalendarLocators.calendar)
        assert current_date() == today.get_attribute("value")

    def calendar_clear_btn(self):
        self.calendar_current_btn()
        self.do_click("Chosen date", CalendarLocators.calendar)
        time.sleep(2)

        self.do_click("Очистить", CalendarLocators.calendar_clear_btn)
        today = self.get_element(CalendarLocators.calendar)
        assert current_date() != today.get_attribute("value")

    def calendar_set_random_date(self):
        time.sleep(1)

        self.do_click("Выбор даты", CalendarLocators.calendar)
        date = calendar_date()
        self.do_click("Random date", date)

    # #######-TOTAL AMOUNT-######################
    def total_amount(self, total):
        time.sleep(3)
        value = self.get_element(total)
        float_value = OperationManager.check_amount(value.get_attribute("value"))
        return float_value
