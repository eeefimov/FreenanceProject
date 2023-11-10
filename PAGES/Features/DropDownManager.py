import random
from PAGES.Main import Main


class DropDownManager(Main):
    def __init__(self, driver):
        super().__init__(driver)

    def check_added_value_in_category(self, name, list_items):
        item_names = set(item.text for item in self.driver.find_elements(*list_items))
        if name in item_names:
            print("New category name: ", name)
            return True
        else:
            return False

    def get_exist_name_from_the_list(self, list_values_locator):
        item_names = set(item.text for item in self.driver.find_elements(*list_values_locator))
        category_name = random.choice(list(item_names))
        return category_name

    @staticmethod
    def list_selected_element(index):
        list_element_idexed = ("xpath", f"//div[@class='dropdown-item false' and @index='{index}']")
        return list_element_idexed

    @staticmethod
    def list_selected_del_btn(index):
        del_btn_locator = ("xpath", f"//div[@index='{index}']//span[@title='Удаление категории']")
        return del_btn_locator

    @staticmethod
    def modal_action(action_name):
        locator = ("xpath", f"//div[contains(@class, 'Modal_active')]//button[text()= '{action_name}']")
        return locator

    @staticmethod
    def set_selected_name_locator(name):
        locator = ("xpath", f"//div[@class='dropdown-selected-value' and contains(text(), '{name}')]")
        return locator

    @staticmethod
    def set_selected_index_locator(index):
        locator = ("xpath", f"//div[@index='{index}']")
        return locator
