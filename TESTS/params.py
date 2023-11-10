import pytest
from TESTS.utils import randomize_latin_string, randomize_float, \
    randomize_special_string, randomize_cyrillic_string, \
    randomize_password, randomize_int
from TESTS.settings import key


from TESTS.settings import user_login, user_pass, user_email

params_start_page_login_invalid = [
    pytest.param("", "", True, id="Empty fields"),
    pytest.param(user_login, "", True, id="Empty password"),
    pytest.param("", user_pass, True, id="Empty login"),
    pytest.param(randomize_latin_string(6), randomize_password(3, 3, 0), True, id="Wrong user data values"),
    pytest.param(user_login, randomize_password(3, 3, 0), True, id="Wrong password"),
    pytest.param(randomize_latin_string(6), user_pass, True, id="Wrong login")
]

params_income_new_category_names_invalid = [
    pytest.param(randomize_latin_string(15), id="String 15"),
    pytest.param("", id="Empty")
]

params_income_new_category_names_valid = [
    pytest.param(randomize_latin_string(10), id="Valid 10")
]

params_recovery_page_email_validation = [
    pytest.param("", False, id="Empty field"),
    pytest.param(f"{randomize_latin_string(5)}@{randomize_latin_string(5)}.{randomize_latin_string(5)}",
                 False, id="Invalid email")
]

params_register_page_verify_email_field = [
    pytest.param(randomize_latin_string(5), False, id="Format: string"),
    pytest.param(randomize_float(100), False, id="Format: float"),
    pytest.param(f"@{randomize_latin_string(3)}.{randomize_latin_string(3)}", False, id="Format: @chars.chars"),
    pytest.param(f"{randomize_latin_string(3)}@", False, id="Format: chars@"),
    pytest.param(f"{randomize_latin_string(3)}@{randomize_latin_string(3)}", False, id="Format: chars@chars")
]

params_register_page_verify_login_field = [
    pytest.param(randomize_latin_string(5), False, id="Format: invalid value (5 chars)"),
    pytest.param(randomize_latin_string(33), False, id="Format: invalid value (33 chars)"),
    pytest.param(randomize_special_string(10), False, id="Format: invalid special"),
    pytest.param(randomize_cyrillic_string(10), False, id="Format: invalid cyrillic")
]

params_register_page_verify_pass_field = [
    pytest.param(randomize_latin_string(5), False, id="Format: invalid value (5 chars)"),
    pytest.param(randomize_password(2, 2, 0), False, id="Format: invalid value (5 chars),2 up 2 low 1 int"),
    pytest.param(randomize_password(1, 31, 0), False, id="Format: invalid value (33 chars),1 up 31 low 1 int"),
    pytest.param(randomize_password(5, 5, 1), False, id="Format: invalid value (10 chars),5 up 5 low 0 int"),
    pytest.param(randomize_password(5, 5, 2), False, id="Format: invalid value (6 chars),0 up 5 low 1 int")
]

params_register_page_verify_pass_confirm_field = [
    pytest.param(randomize_password(3, 3, 0), True, True, id="Format: valid pass: 3 low 3 up int"),
    pytest.param(randomize_password(3, 3, 0), True, False, id="Format: valid pass: 3 low 3 up int")
]

params_register_page_exist_user_values = [
    pytest.param(f"{randomize_latin_string(5)}@{randomize_latin_string(5)}.{randomize_latin_string(5)}",
                 user_login,
                 randomize_password(3, 3, 0), id="Exist login"),
    pytest.param(user_email,
                 randomize_latin_string(10),
                 randomize_password(3, 3, 0),
                 id="Exist Email"),
    pytest.param(user_email, user_login, randomize_password(3, 3, 0), id="Exist email and login")
]

params_amount_values = [
    pytest.param(0.1, id="0.1"),
    pytest.param(randomize_float(10000), id="random float")
]

# ####################-API PARAMS-##########################
data = {'id': randomize_int(10000),
        'user': randomize_latin_string(10),
        'category_id': randomize_int(10000),
        'categoryName': randomize_latin_string(10)
        }

post_data_response = {'categoryName': None,
                      'category_id': None,
                      'category_type': None,
                      'income_outcome': None,
                      'is_hidden': None,
                      'user_id': None
                      }

endpoints = ["income-categories/", "last-5-incomecash/", "last-5-outcomecash/",
             "money-box-categories/", "outcome-categories/"]
params_api_get = []

for endpoint in endpoints:
    params_api_get.append(
        pytest.param("get", key, endpoint, None, 200, id=f"Valid key for {endpoint}")
    )
    params_api_get.append(
        pytest.param("get", randomize_latin_string(20), endpoint, None, 401, id=f"Invalid key for {endpoint}")
    )
    params_api_get.append(
        pytest.param("get", None, endpoint, None, 401, id=f"No key for {endpoint}")
    )
    params_api_get.append(
        pytest.param("post", key, endpoint, data, 405, id=f"post for {endpoint}")
    )
    params_api_get.append(
        pytest.param("put", key, endpoint, data, 405, id=f"put for {endpoint}")
    )

# #################-POST DATA CATEGORY-###########################
#type: "constant", "once"
# choice = ["constant", "once", "income", "outcome"]
params_api_post_category = [
    # income
    pytest.param(randomize_latin_string(10), "income", 201, id="post_data, name 10"),
    pytest.param(randomize_latin_string(1), "income", 201, id="post_data, name 1"),
    pytest.param(randomize_latin_string(100), "income", 400, id="post_data, name 100"),
    pytest.param("", "income", 400, id="post_data name """),
    # outcome
    pytest.param(randomize_latin_string(10), "outcome", 201, id="post_data, name 10"),
    pytest.param(randomize_latin_string(1), "outcome", 201, id="post_data, name 1"),
    pytest.param(randomize_latin_string(100), "outcome", 400, id="post_data, name 100"),
    pytest.param("", "outcome", 400, id="post_data name """),
    # wrong come
    pytest.param(randomize_latin_string(10), randomize_latin_string(10), 400, id="wrong come 10"),
    pytest.param(randomize_latin_string(1), randomize_latin_string(10), 400, id="wrong come 1"),
    pytest.param(randomize_latin_string(100), randomize_latin_string(10), 400, id="wrong come 100"),
    pytest.param("", randomize_latin_string(10), 400, id="wrong come name ''")
]