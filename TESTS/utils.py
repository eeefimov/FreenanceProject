import random
import string
from datetime import datetime, timedelta
from selenium.webdriver.common.by import By


def randomize_float(n):
    random_float = random.uniform(1.0, n)
    return round(random_float, 2)


def randomize_int(n):
    random_number = random.randint(1, n)
    return random_number


def randomize_latin_string(number: int):
    symbols = string.ascii_letters
    random_string = "".join(random.choice(symbols) for _ in range(number))
    return random_string


def randomize_string(str_type, number: int):
    """Generate a random string of the specified type and length."""
    symbols = str_type
    random_string = "".join(random.choice(symbols) for _ in range(number))
    return random_string


def randomize_cyrillic_string(number: int):
    """Generate a random Cyrillic string of the specified length."""
    cyrillic_chars = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
    random_string = "".join(random.choice(cyrillic_chars) for _ in range(number))
    return random_string


def randomize_chinese_string(number: int):
    """Generate a random Chinese string of the specified length."""
    chinese_chars = '的一是不了人我在有他这为之大来以个中上们'
    random_string = "".join(random.choice(chinese_chars) for _ in range(number))
    return random_string


def randomize_special_string(number: int):
    special_chars = '|\\/!@#$%^&*()-_=+`~?"№;:[]{}'
    random_string = "".join(random.choice(special_chars) for _ in range(number))
    return random_string


def randomize_password(up: int, low: int, variant: int):
    # Define character sets
    uppercase_letters = randomize_string(string.ascii_uppercase, up)
    lowercase_letters = randomize_string(string.ascii_lowercase, low)
    digits = randomize_int(9)

    # Ensure at least one uppercase letter and one digit
    password = [uppercase_letters + lowercase_letters + str(digits),
                lowercase_letters + uppercase_letters,
                lowercase_letters + str(digits),
                uppercase_letters + str(digits)
                ]
    return password[variant]


def randomize_date():
    today = datetime.today()
    days_in_current_month = (today.replace(day=1, month=today.month % 12 + 1) - timedelta(days=1)).day
    random_day = random.randint(1, days_in_current_month)
    return random_day


def current_date():
    date = datetime.now()
    formatted_date = date.strftime("%d.%m.%Y")
    return formatted_date


def calendar_date():
    n = randomize_int(30)
    income_calendar_date = (
    By.XPATH, f"//div[@class='air-datepicker-body--cells -days-']//div[contains(text(),'{n}')]")
    return income_calendar_date




