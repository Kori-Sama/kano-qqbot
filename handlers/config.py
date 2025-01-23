
from config import config
from constants import GROUP_IDS, MASTER_ID
from post_type import GroupPost
from send import get_send_group


def handle_config(event: GroupPost):
    if event.post_type != "message" or event.message_type != "group":
        return

    if event.group_id not in GROUP_IDS:
        return

    send_group = get_send_group(event.group_id)

    if event.sender.user_id != MASTER_ID:
        return

    if not event.raw_message.startswith("set ") and \
       not event.raw_message.startswith("unset "):
        return

    cmd, key = event.raw_message.split(" ")

    print(f"cmd: {cmd}, key: {key}")

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
