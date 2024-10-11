# safe_repo
# Note if you are trying to deploy on vps then directly fill values in ("")

from os import getenv

API_ID = int(getenv("API_ID", "24185318"))
API_HASH = getenv("API_HASH", "04957fbc90479bcbf4d64bfefb65adc9")
BOT_TOKEN = getenv("BOT_TOKEN", "7592107730:AAEG4g1jRg9b71aXQXgVCjhPgrHpoM1kXA0")
OWNER_ID = list(map(int, getenv("OWNER_ID", "6733983659").split()))
MONGO_DB = getenv("MONGO_DB", "mongodb://ahmedalsaltani30:ahmedabcd074@cluster0-shard-00-00.quu8v.mongodb.net:27017,cluster0-shard-00-01.quu8v.mongodb.net:27017,cluster0-shard-00-02.quu8v.mongodb.net:27017/?ssl=true&replicaSet=atlas-s98j2a-shard-0&authSource=admin&retryWrites=true&w=majority&appName=Cluster0")
LOG_GROUP = getenv("LOG_GROUP", "-1002327497511")
CHANNEL_ID = int(getenv("CHANNEL_ID", "-1002327497511"))
