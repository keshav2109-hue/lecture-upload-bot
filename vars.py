#🇳‌🇮‌🇰‌🇭‌🇮‌🇱‌
# Add your details here and then deploy by clicking on HEROKU Deploy button
import os
from os import environ

API_ID = int(environ.get("API_ID", "25149550"))
API_HASH = environ.get("API_HASH", "67b06e7a112cb9b9a5365c5f4fce2495")
BOT_TOKEN = environ.get("BOT_TOKEN", "8242068774:AAGlIxq_Ft3RbzvnHW0Tx9L9R3jmx3aTVrw")

OWNER = int(environ.get("OWNER", "7899819345"))
CREDIT = environ.get("CREDIT", "𝙎𝙩𝙪𝙙𝙮𝙑𝙚𝙧𝙨𝙚")

TOTAL_USER = os.environ.get('TOTAL_USERS', '7899819345').split(',')
TOTAL_USERS = [int(user_id) for user_id in TOTAL_USER]

AUTH_USER = os.environ.get('AUTH_USERS', '7899819345').split(',')
AUTH_USERS = [int(user_id) for user_id in AUTH_USER]
if int(OWNER) not in AUTH_USERS:
    AUTH_USERS.append(int(OWNER))
  
#WEBHOOK = True  # Don't change this
#PORT = int(os.environ.get("PORT", 8080))  # Default to 8000 if not set


