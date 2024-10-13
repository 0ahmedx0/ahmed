from os import environ 

class Config:
    API_ID = environ.get("API_ID", "24185318")
    API_HASH = environ.get("API_HASH", "04957fbc90479bcbf4d64bfefb65adc9")
    BOT_TOKEN = environ.get("BOT_TOKEN", "7918296315:AAH3yQuf11D6ahvJPajjr9W2rgL3NB4r7cw") 
    BOT_SESSION = environ.get("BOT_SESSION", "bot") 
    DATABASE_URI = environ.get("DATABASE", "mongodb://ahmedalsaltani30:ahmedabcd074@cluster0-shard-00-00.quu8v.mongodb.net:27017,cluster0-shard-00-01.quu8v.mongodb.net:27017,cluster0-shard-00-02.quu8v.mongodb.net:27017/?ssl=true&replicaSet=atlas-s98j2a-shard-0&authSource=admin&retryWrites=true&w=majority&appName=Cluster0")
    DATABASE_NAME = environ.get("DATABASE_NAME", "forward-bot")
    BOT_OWNER_ID = [int(id) for id in environ.get("BOT_OWNER_ID", '6733983659').split()]

class temp(object): 
    lock = {}
    CANCEL = {}
    forwardings = 0
    BANNED_USERS = []
    IS_FRWD_CHAT = []
    
