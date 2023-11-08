import pytest
from icecream import ic
from TESTS.settings import key
from API.main_api import MainApi
from TESTS.params import params_api_get, params_api_post_category


class TestApiGet:

    @pytest.mark.parametrize("method, key, endpoint, data, expected", params_api_get)
    def test_check_get_method(self, method, key, endpoint, data, expected):
        ma = MainApi(key, endpoint, data)
        response = ma.set_requests(method)
        assert ma.print_requests(response) == expected

    @pytest.mark.parametrize("name, come, expected", params_api_post_category)
    def test_check_post_method(self, name, come, expected):
        post_data = {
            'categoryName': name,
            'category_type': 'constant',
            'income_outcome': come,
            'target': ''
        }
        ma = MainApi(key, "categories/", data=post_data)
        response = ma.set_requests("post")
        assert ma.print_requests(response) == expected
        assert 'Content-Type' in ma.header
        assert 'Authorization' in ma.header
        assert ma.header['Content-Type'] == 'application/json'
        assert ma.header['Authorization'] == ma.token
        if len(name) > 0:
            ic(response.json())
            assert ma.check_playload_with_data(post_data, response.json())
