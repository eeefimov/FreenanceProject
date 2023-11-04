# from PAGES.PagesMain import PagesMain
# from PAGES.Locators import CategoriesLocators, OperationListLocators
#
#
# class IncomePage(PagesMain):
#     def __init__(self, driver):
#         super().__init__(driver)
#
#     # def check_add_category_to_constant(self, name):
#     #     self.add_category(name=name,
#     #                       list_name="Постоянные",
#     #                       list_locator=CategoriesLocators.constant_dropdown
#     #                       )
#     #
#     # def check_add_category_to_temp(self, name):
#     #     self.add_category(name=name,
#     #                      list_name="Временные",
#     #                      list_locator=CategoriesLocators.temp_dropdown
#     #                      )
#     #
#     # def check_category_name_length_error_constant(self, name):
#     #     self.error_name_length(name=name,
#     #                            list_name="Постоянные",
#     #                            list_locator=CategoriesLocators.constant_dropdown
#     #                            )
#     #
#     # def check_category_name_length_error_temp(self, name):
#     #     self.error_name_length(name=name,
#     #                            list_name="Временные",
#     #                            list_locator=CategoriesLocators.temp_dropdown
#     #                            )
#     #
#     # def check_exist_category_name_error_constant(self):
#     #     self.error_name_exist(list_name="Постоянные",
#     #                           list_locator=CategoriesLocators.constant_dropdown
#     #                           )
#     #
#     # def check_exist_category_name_error_temp(self):
#     #     self.error_name_exist(list_name="Временные",
#     #                           list_locator=CategoriesLocators.temp_dropdown
#     #                           )
#     #
#     # def check_length_error_repeat_constant(self, name):
#     #     self.repeat_error_name_length(name=name,
#     #                                   list_name="Постоянные",
#     #                                   list_locator=CategoriesLocators.constant_dropdown
#     #                                   )
#     #
#     # def check_length_error_repeat_temp(self, name):
#     #     self.repeat_error_name_length(name=name,
#     #                                   list_name="Временные",
#     #                                   list_locator=CategoriesLocators.temp_dropdown
#     #                                   )
#     #
#     # def check_exist_error_repeat_constant(self):
#     #     self.repeat_error_name_exist(list_name="Постоянные",
#     #                                  list_locator=CategoriesLocators.constant_dropdown
#     #                                  )
#     #
#     # def check_exist_error_repeat_temp(self):
#     #     self.repeat_error_name_exist(list_name="Временные",
#     #                                  list_locator=CategoriesLocators.temp_dropdown
#     #                                  )
#
#     # def check_random_delete_constant(self):
#     #     self.category_modal_action(list_name="Постоянные",
#     #                                list_locator=CategoriesLocators.constant_dropdown,
#     #                                action_name="Удалить"
#     #                                )
#     #
#     # def check_random_archive_constant(self):
#     #     self.category_modal_action(list_name="Постоянные",
#     #                                list_locator=CategoriesLocators.constant_dropdown,
#     #                                action_name="В архив"
#     #                                )
#     #
#     # def check_random_cancel_constant(self):
#     #     self.category_modal_action(list_name="Постоянные",
#     #                                list_locator=CategoriesLocators.constant_dropdown,
#     #                                action_name="Отмена"
#     #                                )
#     #
#     # def check_random_delete_temp(self):
#     #     self.category_modal_action(list_name="Временные",
#     #                                list_locator=CategoriesLocators.temp_dropdown,
#     #                                action_name="Удалить"
#     #                                )
#     #
#     # def check_random_archive_temp(self):
#     #     self.category_modal_action(list_name="Временные",
#     #                                list_locator=CategoriesLocators.temp_dropdown,
#     #                                action_name="В архив"
#     #                                )
#     #
#     # def check_random_cancel_temp(self):
#     #     self.category_modal_action(list_name="Временные",
#     #                                list_locator=CategoriesLocators.temp_dropdown,
#     #                                action_name="Отмена"
#     #                                )
#
#     def check_operation_constant(self, summ):
#         self.operation_add_amount(amount=summ,
#                                   list_name="Постоянные",
#                                   list_locator=CategoriesLocators.constant_dropdown,
#                                   add_amount_field=CategoriesLocators.add_amount_to_category_field_const,
#                                   add_amount_btn=CategoriesLocators.add_amount_to_category_btn_const
#                                   )
#
#     def check_operation_temp(self, summ):
#         self.operation_add_amount(amount=summ,
#                                   list_name="Временные",
#                                   list_locator=CategoriesLocators.temp_dropdown,
#                                   add_amount_field=CategoriesLocators.add_amount_to_category_field_temp,
#                                   add_amount_btn=CategoriesLocators.add_amount_to_category_btn_temp
#                                   )
#
#     def check_operation_x_del_btn(self):
#         self.operations_del(btn_name="delete",
#                             btn_name_locator=OperationListLocators.oper_modal_delete_btn
#                             )
#
#     def check_operation_x_cancel_btn(self):
#         self.operations_del(btn_name="cancel",
#                             btn_name_locator=OperationListLocators.oper_modal_cancel_btn
#                             )
#
#     def check_operation_edit_btn(self, amount):
#         self.operation_edit_btn(amount=amount)
#
#     def check_calendar_current_btn(self):
#         self.calendar_current_btn()
#
#     def check_calendar_clear_btn(self):
#         self.calendar_clear_btn()
