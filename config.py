from os import environ 

class Config:
    API_ID = environ.get("API_ID", "8733404")
    API_HASH = environ.get("API_HASH", "f19aed00b0c74abed0359016afc1733f")
    BOT_TOKEN = environ.get("BOT_TOKEN", "7806428506:AAHwGSJiG40k5NyfEUhRPYe1IwjbQQyY5Bg") 
    BOT_SESSION = environ.get("BOT_SESSION", "bot") 
    DATABASE_URI = environ.get("DATABASE", "mongodb+srv://chhjgjkkjhkjhkjh@cluster0.xowzpr4.mongodb.net/")
    DATABASE_NAME = environ.get("DATABASE_NAME", "forward-bot")
    BOT_OWNER_ID = [int(id) for id in environ.get("BOT_OWNER_ID", '807374433').split()]

class temp(object): 
    lock = {}
    CANCEL = {}
    forwardings = 0
    BANNED_USERS = []
    IS_FRWD_CHAT = []
    
