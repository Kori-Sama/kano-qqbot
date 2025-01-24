
from loguru import logger
from bot_config import config
from local_config import group_ids, master_id
from post_type import GroupPost
from send import get_send_group


def handle_config(event: GroupPost):
    if event is None:
        return

    if event.post_type != "message" or event.message_type != "group":
        return

    if event.group_id not in group_ids:
        return

    send_group = get_send_group(event.group_id)

    if event.sender.user_id != master_id:
        return

    if not event.raw_message.startswith("set ") and \
       not event.raw_message.startswith("unset "):
        return

    cmd, key = event.raw_message.split(" ")

    logger.info(f"cmd: {cmd}, key: {key}")

    if key in config:
        if cmd == "set":
            config[key] = True
            send_group(f"已开启{key}")
        elif cmd == "unset":
            config[key] = False
            send_group(f"已关闭{key}")

        return True
    else:
        send_group(f"未知配置项{key}")

    return False
