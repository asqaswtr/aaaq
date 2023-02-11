from os import getenv
from dotenv import load_dotenv

admins = {}
load_dotenv()

# client vars
API_ID = int(getenv("API_ID", "7452578")) #لا تغير هاذة القيمة
API_HASH = getenv("API_HASH", "061d67ee8eed9368c5cadabb4aa21efc")#لا تغير هاذة القيمة
BOT_TOKEN = getenv("BOT_TOKEN", "6225090835:AAFI8qZe-WS5iLLrql8g222unIQ4lO_a4us")
SESSION_NAME = getenv("SESSION_NAME", "AQCNWeB_xUoZRyCbSN15pQCwGfB_9Ery2gPwXWp_rT6Mgs4Gu7Ntin0phdH31kw2Ffwbc4ypcaorf3JijDW3327mbXjQC9kI2-tYkazsd0ohEkTDdxV66WqBTXbUEJvY_Ggf28f4kF4sMS-J72TvW_X2Xcs_5asbsq-uVCl_MGmnFIpmIsVrNnACQa7oizUsoa4ZQZKQWzv8W13iwJaed9jcHw4DcQ48CBxh8xC8ABkE8IAVGRY2NAH27ApflOW-0XeZfHSmncdB6Uhcje39DKnU0JGvdgbSnNhANY09yPtE8S9pSA8WmgostjaIZT8M-JyKeg50UPRJMi4MJteK_GHFAAAAAU4RUK4A")

# mandatory vars
OWNER_USERNAME = getenv("OWNER_USERNAME", "I_0_AB") # @ هنا ضع يوزر حسابك بدون 
ALIVE_NAME = getenv("ALIVE_NAME", "𝘼′𝙇 𝙎′𝙃′𝘼′𝙔′𝙀′𝘽 ➪🇳🇱") # هنا ضع اسم حسابك
BOT_USERNAME = getenv("BOT_USERNAME", "S_43_ybot") # @ هنا ضع يوزر البوت بدون 
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/X02lx/RrRRR") 
UPSTREAM_BRANCH = getenv("UPSTREM_BRANCH", "main") #لا تغير هاذة القيمة
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "60")) #لا تغير هاذة القيمة
GROUP_SUPPORT = getenv("GROUP_SUPPORT", "") # @ هنا ضغ يوزر كروبك بدون 
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "") # @ هنا ضغ يوزر قناتك بدون

# database, decorators, handlers mandatory vars
MONGODB_URL = getenv("MONGODB_URL", "mongodb+srv://veez:mega@cluster0.heqnd.mongodb.net/veez?retryWrites=true&w=majority")
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! . $").split())
OWNER_ID = list(map(int, getenv("OWNER_ID", "5817770061").split()))
                                             #هنا ضع ايدي المطور فوق و الاعلئ
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "5817770061").split()))

# image resources vars
IMG_1 = getenv("IMG_1", "https://te.legra.ph/file/2a726c634dbc3b9e8f451.png")
IMG_2 = getenv("IMG_2", "https://te.legra.ph/file/90e3b3aeb77e3e598d66d.png")
IMG_3 = getenv("IMG_3", "https://te.legra.ph/file/d70bb6fa92728763c671f.png")
IMG_4 = getenv("IMG_4", "https://te.legra.ph/file/430dcf25456f2bb38109f.png")
IMG_5 = getenv("IMG_5", "https://te.legra.ph/file/cd5c96a3c7e8ae1913ef3.png")
ALIVE_IMG = getenv("ALIVE_IMG", "https://telegra.ph/file/c83b000f004f01897fe18.png")
