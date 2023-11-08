import requests
import json
from functools import wraps


class MainApi:
    def __init__(self, key, endpoint, data=None):
        self.main_url = "https://dev.freenance.store/api/"
        self.token = key
        self.endpoint = endpoint
        self.header = {
            "Content-Type": "application/json",
            "Authorization": self.token
        }
        self.api_url = self.main_url + str(endpoint)
        self.data = data

    def set_requests(self, method: str):
        if method == "get":
            req = requests.get(self.api_url, headers=self.header, data=self.data)
        elif method == "post":
            req = requests.post(self.api_url, headers=self.header, json=self.data)
        elif method == "put":
            req = requests.put(self.api_url, headers=self.header, data=self.data)
        elif method == "del":
            req = requests.delete(self.api_url, headers=self.header, data=self.data)

        return req

    def print_requests(self, request):
        status = request.status_code
        try:
            result = request.json()
        except json.decoder.JSONDecodeError:
            result = request.text
        return status

    def playload_values(self, playload: dict):
        return playload.values()

    def playload_keys(self, playload: dict):
        return playload.keys()

    def check_playload_with_data(self, data: dict, playload: dict):
        common_keys = set(data.keys()).intersection(playload.keys())
        return bool(common_keys)


    def delete_last_one(self):
        api_url = self.main_url + str("delete-incomecash/1975")
        self.header["Content-Type"] = "application/json"
        self.header["authorization"] = "Token 01dc3b27c45fe9dcbd0c3c59d604e7539bdd5af1"
        req = requests.delete(api_url, headers=self.header)
        status = req.status_code
        return status
    #
    # def delete_last_five(self):
    #     api_url = self.main_url + str("last-5-incomecash/")
    #     self.header["Content-Type"] = "application/json"
    #     self.header["authorization"] = "Token 01dc3b27c45fe9dcbd0c3c59d604e7539bdd5af1"
    #     req = requests.get(api_url, headers=self.header)
    #     result = req.json()
    #     for item in result:
    #         id = item["id"]
    #         print(id)
    #         api_url = self.main_url + str(f"delete-incomecash/{id}")
    #         self.header["Content-Type"] = "application/json"
    #         self.header["authorization"] = "Token 01dc3b27c45fe9dcbd0c3c59d604e7539bdd5af1"
    #         req = requests.delete(api_url, headers=self.header)
    #         status = req.status_code
    #     return status

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



