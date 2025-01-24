import os
from dotenv import load_dotenv
from loguru import logger

load_dotenv(verbose=True)


base_send_url = os.getenv("BASE_SEND_URL")
group_ids = [int(x) for x in os.getenv("GROUP_IDS").split(",")]

master_id = int(os.getenv("MASTER_ID"))
bot_id = int(os.getenv("BOT_ID"))
bot_name = os.getenv("BOT_NAME")

logger.info(f"""
            config loaded:
            base_send_url: {base_send_url}
            group_ids: {group_ids}
            master_id: {master_id}
            bot_id: {bot_id}
            bot_name: {bot_name}
            """)
