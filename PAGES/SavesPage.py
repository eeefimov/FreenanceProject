from PAGES.PagesMain import PagesMain
from PAGES.Locators import CalendarLocators, CategoriesLocators, OperationListLocators


class SavesPage(PagesMain):

    def __init__(self, driver):
        super().__init__(driver)

    def check_add_category_to_saves(self, name):
        self.add_category(name=name,
                          list_name="Накопления",
                          list_locator=CategoriesLocators.saves_dropdown
                          )

    def check_category_name_length_error_saves(self, name):
        self.error_name_length(name=name,
                               list_name="Накопления",
                               list_locator=CategoriesLocators.saves_dropdown
                               )

    def check_exist_category_name_error_saves(self):
        self.error_name_exist(list_name="Накопления",
                              list_locator=CategoriesLocators.saves_dropdown
                              )

    def check_length_error_repeat_saves(self, name):
        self.repeat_error_name_length(name=name,
                                      list_name="Накопления",
                                      list_locator=CategoriesLocators.saves_dropdown
                                      )

    def check_exist_error_repeat_saves(self):
        self.repeat_error_name_exist(list_name="Накопления",
                                     list_locator=CategoriesLocators.saves_dropdown
                                     )

    def check_random_delete_saves(self):
        self.category_modal_action(list_name="Накопления",
                                   list_locator=CategoriesLocators.saves_dropdown,
                                   action_name="Удалить"
                                   )

    def check_random_archive_saves(self):
        self.category_modal_action(list_name="Накопления",
                                   list_locator=CategoriesLocators.saves_dropdown,
                                   action_name="В архив"
                                   )

    def check_random_cancel_saves(self):
        self.category_modal_action(list_name="Накопления",
                                   list_locator=CategoriesLocators.saves_dropdown,
                                   action_name="Отмена"
                                   )

    def check_operation_saves(self, summ):
        self.operation_add_amount(amount=summ,
                                  list_name="Накопления",
                                  list_locator=CategoriesLocators.saves_dropdown,
                                  add_amount_field=CategoriesLocators.add_amount_to_category_field_const,
                                  add_amount_btn=CategoriesLocators.add_amount_to_category_btn_const
                                  )


