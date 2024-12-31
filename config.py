import os

BOT_TOKEN = os.environ.get("BOT_TOKEN", "6873452469:AAHHNQ1HEXV7ehxL5WqJHxui7YhUzx1-3uU")
API_ID = int(os.environ.get("API_ID", "20353207"))
API_HASH = os.environ.get("API_HASH", "e5b2ac2f9c37bda345fa9fb5ade66961")
LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "-1002138809373"))
AUTH_USERS = set(int(x) for x in os.environ.get("AUTH_USERS", "").split())
DB_URL = os.environ.get("DB_URL", "mongodb+srv://hnyx:wywyw2@cluster0.9dxlslv.mongodb.net/?retryWrites=true&w=majority")
DB_NAME = os.environ.get("DB_NAME", "BroadcastBot")
BROADCAST_AS_COPY = bool(os.environ.get("BROADCAST_AS_COPY", True))
