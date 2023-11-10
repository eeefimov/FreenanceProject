import os
from dotenv import load_dotenv
load_dotenv()


user_login = os.getenv("user_login")
user_pass = os.getenv("user_pass")
user_email = os.getenv("user_email")
key = os.getenv("key")