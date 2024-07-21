import os

#Bot token @Botfather
BOT_TOKEN = os.environ.get("BOT_TOKEN", "")

#Your API ID from my.telegram.org
API_ID = int(os.environ.get("API_ID", "29695860"))

#Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "d3fab651846ecb63f2736ab65fbceac8")

#Database 
DB_URI = os.environ.get("DB_URI", "mongodb+srv://jaatdinesh680:ueIYuMZUReM5meK1@cluster0.rj68k3u.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
