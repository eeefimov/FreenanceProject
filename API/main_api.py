import requests
import json
from TESTS.settings import user_login, user_pass


class MainApi:
    def __init__(self):
        self.main_url = "https://dev.freenance.store/api/"
        self.login = user_login,
        self.password = user_pass
        self.header = {}
        self.auth_key = None

    def get_api_key(self):
        api_url = self.main_url + str("auth/token/login/")
        self.header["Content-Type"] = "application/json"

        data = {
            'username': 'newtestuser',
            'password': '123QWEqwe',
            'auth_token': '01dc3b27c45fe9dcbd0c3c59d604e7539bdd5af1'
        }
        req = requests.post(api_url, json=data, headers=self.header)
        status = req.status_code
        try:
            result = req.json()
            self.auth_key = result
        except json.decoder.JSONDecodeError:
            result = req.text

        api_url = self.main_url + str("last-5-incomecash/")
        req = requests.get()

        return status, result

    def get_last_five(self):
        api_url = self.main_url + str("last-5-incomecash/")
        self.header["Content-Type"] = "application/json"
        self.header["authorization"] = "Token 01dc3b27c45fe9dcbd0c3c59d604e7539bdd5af1"
        req = requests.get(api_url, headers=self.header)
        status = req.status_code
        try:
            result = req.json()
        except json.decoder.JSONDecodeError:
            result = req.text

        return status, result

    def delete_last_one(self):
        api_url = self.main_url + str("delete-incomecash/1975")
        self.header["Content-Type"] = "application/json"
        self.header["authorization"] = "Token 01dc3b27c45fe9dcbd0c3c59d604e7539bdd5af1"
        req = requests.delete(api_url, headers=self.header)
        status = req.status_code
        return status

    def delete_last_five(self):
        api_url = self.main_url + str("last-5-incomecash/")
        self.header["Content-Type"] = "application/json"
        self.header["authorization"] = "Token 01dc3b27c45fe9dcbd0c3c59d604e7539bdd5af1"
        req = requests.get(api_url, headers=self.header)
        result = req.json()
        for item in result:
            id = item["id"]
            print(id)
            api_url = self.main_url + str(f"delete-incomecash/{id}")
            self.header["Content-Type"] = "application/json"
            self.header["authorization"] = "Token 01dc3b27c45fe9dcbd0c3c59d604e7539bdd5af1"
            req = requests.delete(api_url, headers=self.header)
            status = req.status_code
        return status

    def get_categories(self):
        api_url = self.main_url + str("categories/")
        self.header["Content-Type"] = "application/json"
        self.header["authorization"] = "Token 01dc3b27c45fe9dcbd0c3c59d604e7539bdd5af1"
        req = requests.get(api_url, headers=self.header)
        result = req.json()
        for item in result:
            print(item)
            # print(item['categoryName'], item["category_id"])
        status = req.status_code
        return status

    def post_categories(self):
        api_url = self.main_url + str("categories/")
        self.header["Content-Type"] = "application/json"
        self.header["accept-language"] = "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7"
        self.header["authorization"] = "Token 01dc3b27c45fe9dcbd0c3c59d604e7539bdd5af1"

        data = {
            'categoryName': '123456789 01234512345 6789012345',
            'category_type': 'constant',
            'income_outcome': 'income',
        }
        req = requests.post(api_url, json=data, headers=self.header)
        status = req.status_code
        return status

    def del_categories(self):
        api_url = self.main_url + str(f"del-category/5132")
        self.header["Content-Type"] = "application/json"
        self.header["authorization"] = "Token 01dc3b27c45fe9dcbd0c3c59d604e7539bdd5af1"
        req = requests.delete(api_url, headers=self.header)
        status = req.status_code
        return status

    def arhives_categories(self):
        api_url = self.main_url + str(f"update-category/5129")
        self.header["Content-Type"] = "application/json"
        self.header["authorization"] = "Token 01dc3b27c45fe9dcbd0c3c59d604e7539bdd5af1"
        req = requests.put(api_url, headers=self.header)
        status = req.status_code
        return status



