class OperationManager:
    @staticmethod
    def operation_list_check_amount(item_id):
        list_element_locator = ("xpath", f"//div[@class='transactions']//*[@id='{item_id}']//div[3]")
        return list_element_locator

    @staticmethod
    def operation_list_btn(btn_name: str, item_id):
        i = 1 if btn_name in ["delete", "cancel"] else 2
        btn_locator = ("xpath", f"//div[@class='transactions']//*[@id='{item_id}']//div[4]//button[{i}]")
        print(i)
        return btn_locator

    @staticmethod
    def check_amount(added_amount: str) -> float:
        cleaned_amount_str = "".join(char for char in added_amount if char.isnumeric() or char == '.')
        amount_float = float(cleaned_amount_str) / 100
        return amount_float
