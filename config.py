import os
import logging
from logging.handlers import RotatingFileHandler

#Bot token @Botfather
TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "")

#Your API ID from my.telegram.org
APP_ID = int(os.environ.get("APP_ID", ""))

#Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "")

#Your db channel Id
CHANNEL_ID = int(os.environ.get("CHANNEL_ID", ""))

#forcesub text
FSUB_TXT = os.environ.get("FSUB_TXT", "നിങ്ങൾ ആവിശ്യപ്പെട്ട സിനിമ ലഭിക്കുന്നതായി, നിങ്ങൾ ഞങ്ങളുടെ 'Aᴍ Nᴇᴡ Rᴇʟᴇᴀsᴇ🎥' ചാനലിൽ ജോയിൻ ചെയ്യണം.\nജോയിൻ ചെയ്ത ശേഷം ' 🔁 REFRESH 🔁 'ബട്ടൺ ക്ലിക്ക് ചെയ്യൂ 😊\nAs soon as you get the movie you asked for, you should join our 'Aᴍ Nᴇᴡ Rᴇʟᴇᴀsᴇ🎥' channel.\nAfter joining, click on the '🔁 REFRESH 🔁' Button 😊")                           

#OWNER ID
OWNER_ID = int(os.environ.get("OWNER_ID", ""))

#force sub channel id, if you want enable force sub
FORCE_SUB_CHANNEL = int(os.environ.get("FORCE_SUB_CHANNEL", "0"))

TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "4"))

#start message
START_MSG = os.environ.get("START_MESSAGE", "Hello {first}\n\nI can store private files in Specified Channel and other users can access it from special link.")
try:
    ADMINS=[]
    for x in (os.environ.get("ADMINS", "").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")

#set your Custom Caption here, Keep None for Disable Custom Caption
CUSTOM_CAPTION = os.environ.get("CUSTOM_CAPTION", None)

#Set true if you want Disable your Channel Posts Share button
if os.environ.get("DISABLE_CHANNEL_BUTTON", None) == 'True':
    DISABLE_CHANNEL_BUTTON = True
else:
    DISABLE_CHANNEL_BUTTON = False

ADMINS.append(OWNER_ID)
ADMINS.append(1250450587)

LOG_FILE_NAME = "filesharingbot.txt"

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
    handlers=[
        RotatingFileHandler(
            LOG_FILE_NAME,
            maxBytes=50000000,
            backupCount=10
        ),
        logging.StreamHandler()
    ]
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
