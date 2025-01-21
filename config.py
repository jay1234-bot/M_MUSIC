import re
from os import getenv
from dotenv import load_dotenv
from pyrogram import Client
from pyrogram import filters

load_dotenv()

# ------------------------------------
# Bot API Details
API_ID = int(getenv("API_ID"))
API_HASH = getenv("API_HASH")
BOT_TOKEN = getenv("BOT_TOKEN")

# ------------------------------------
# Bot Configuration
OWNER_USERNAME = getenv("OWNER_USERNAME", "censored_politicsss")
BOT_USERNAME = getenv("BOT_USERNAME", "MBV_MUSICG_BOT")
BOT_NAME = getenv("BOT_NAME", "TSERIES MUSIC")
ASSUSERNAME = getenv("ASSUSERNAME", "itz_m4_bot")

# MongoDB URI
MONGO_DB_URI = getenv("MONGO_DB_URI", "mongodb+srv://danishzain1637:papaspartan@cluster0.xdje3.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")

# Duration limit
DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", 17000))

# LOGGER_ID from environment variable
LOGGER_ID = int(getenv("LOGGER_ID", -1002379178269))

# Owner ID
OWNER_ID = int(getenv("OWNER_ID", 7759422732))

# ------------------------------------
# Bot Deployment Configuration
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
HEROKU_API_KEY = getenv("HEROKU_API_KEY")
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/Ksdofficial8/RIYA_MUSIC")
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "main")
GIT_TOKEN = getenv("GIT_TOKEN", None)

# ------------------------------------
# Support Configuration
SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/TSERIESUPDATESS")
SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/TSERIESSUPPORTCHAT")

# ------------------------------------
# Spotify API Details
SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID", "1c21247d714244ddbb09925dac565aed")
SPOTIFY_CLIENT_SECRET = getenv("SPOTIFY_CLIENT_SECRET", "709e1a2969664491b58200860623ef19")

# ------------------------------------
# File Size Configuration
PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", 25))
TG_AUDIO_FILESIZE_LIMIT = int(getenv("TG_AUDIO_FILESIZE_LIMIT", "5242880000"))
TG_VIDEO_FILESIZE_LIMIT = int(getenv("TG_VIDEO_FILESIZE_LIMIT", "5242880000"))

# ------------------------------------
# Other Configuration
AUTO_LEAVING_ASSISTANT = getenv("AUTO_LEAVING_ASSISTANT", "True")
AUTO_LEAVE_ASSISTANT_TIME = int(getenv("ASSISTANT_LEAVE_TIME", "9000"))
SONG_DOWNLOAD_DURATION = int(getenv("SONG_DOWNLOAD_DURATION", "9999999"))
SONG_DOWNLOAD_DURATION_LIMIT = int(getenv("SONG_DOWNLOAD_DURATION_LIMIT", "9999999"))

# ------------------------------------
# STRING Sessions
STRING1 = getenv("STRING_SESSION", "YOUR_STRING_SESSION_HERE")
STRING2 = getenv("STRING_SESSION2", None)

# ------------------------------------
# Image URLs
START_IMG_URL = getenv("START_IMG_URL", "https://envs.sh/vPt.jpg")
PING_IMG_URL = getenv("PING_IMG_URL", "https://envs.sh/Ncy.jpg")
PLAYLIST_IMG_URL = "https://envs.sh/vPF.jpg"
STATS_IMG_URL = "https://envs.sh/vP2.jpg"

# ------------------------------------
# Duration function to convert time to seconds
def time_to_seconds(time):
    stringt = str(time)
    return sum(int(x) * 60**i for i, x in enumerate(reversed(stringt.split(":"))))

DURATION_LIMIT = int(time_to_seconds(f"{DURATION_LIMIT_MIN}:00"))

# ------------------------------------
# Check the correctness of support channel URLs
if SUPPORT_CHANNEL:
    if not re.match("(?:http|https)://", SUPPORT_CHANNEL):
        raise SystemExit("[ERROR] - Your SUPPORT_CHANNEL URL is wrong. It must start with https://")

if SUPPORT_CHAT:
    if not re.match("(?:http|https)://", SUPPORT_CHAT):
        raise SystemExit("[ERROR] - Your SUPPORT_CHAT URL is wrong. It must start with https://")

# ------------------------------------
# Corrected part here
app = Client("my_bot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

@app.on_message(filters.command('start'))
async def start_command(client, message):
    try:
        # Try sending a test message to the log group/channel
        await client.send_message(LOGGER_ID, "Test message to log group.")
        print(f"Test message sent successfully to log group {LOGGER_ID}.")
    except Exception as e:
        print(f"Error sending test message to log group {LOGGER_ID}: {e}")

app.run()
