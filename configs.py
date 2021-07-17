# (c) @AbirHasan2005

import os


class Config(object):
    API_ID = int(os.environ.get("API_ID", 12345))
    API_HASH = os.environ.get("API_HASH", "")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "")
    SESSION_NAME = os.environ.get("SESSION_NAME", "Rename-Bot-0")
    SLEEP_TIME = int(os.environ.get("SLEEP_TIME", 5))
    BOT_OWNER = os.environ.get("BOT_OWNER", 1445283714)
    CAPTION = "Rename Bot by @{}\n\nMade by @AbirHasan2005"
    UPDATES_CHANNEL = os.environ.get("UPDATES_CHANNEL", None)
    LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", -100))
    MONGODB_URI = os.environ.get("MONGODB_URI", "")
    DOWNLOAD_PATH = os.environ.get("DOWNLOAD_PATH", "./downloads")
    BROADCAST_AS_COPY = bool(os.environ.get("BROADCAST_AS_COPY", False))
    ONE_PROCESS_ONLY = bool(os.environ.get("ONE_PROCESS_ONLY", False))
    START_TEXT = """Hi {user_mention},
I am Telegram Video/File Rename Bot! Created by @shreevish
Please send me any Tg Videos/Files and Send name.extension .
 🚨 ... Note : its support almost all files exept pdisk files ... 🚨
 
🚨 PRON video🔞 gives you PERMANENT BAN 🚨
       ┈┈┈••💙✿❤️✿💚••┈┈┈
**Maintained By:** {bot_owner}
"""
    PROGRESS = """
Percentage : {0}%
Done: {1}
Total: {2}
Speed: {3}/s
ETA: {4}
    """
DONATE_USER = """**__Thanks for showing interest in donation.__**
 
Donate us to keep our services continously alive
You can send any amount 
of 20rs, 30rs, 50rs, 70rs, 100rs, 200rs
 
__--Payment Methods:--__
 
GooglePay / Paytm / PhonPay / paypal / Net Banking
 
**For Donate:** message me @shreevish"""

HELP_USER = """**Follow Below Steps:**
   
☞︎︎︎ Use /mode command to change upload mode.

☞︎︎︎ Send a photo to set as permanent thumbnail.

☞︎︎︎ Now send me the Telegram file you want to rename
.
☞︎︎︎ Send the new name when bot ask.

For source code check about
"""

ABOUT = """**𝖬𝗒 𝖣𝖾𝗍𝖺𝗂𝗅𝗌 :**

** My Name:** {bot_name}
    
** Language:** [Python 3](https://www.python.org/)

** FrameWork:** [Pyrogram](https://github.com)

** Developer:** {bot_owner}

** Channel:** [All Movie Rockers](https://t.me/All_Movie_Rockers)

** Group:** [Creator](https://t.me/shreevish)
"""
