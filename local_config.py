import os
from dotenv import load_dotenv

load_dotenv()


base_send_url = os.getenv("BASE_SEND_URL")
group_ids = [int(x) for x in os.getenv("GROUP_IDS").split(",")]

master_id = int(os.getenv("MASTER_ID"))
bot_id = int(os.getenv("BOT_ID"))
bot_name = os.getenv("BOT_NAME")
