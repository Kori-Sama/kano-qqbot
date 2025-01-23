from config import config
from constants import GROUP_IDS, MASTER_ID
from post_type import GroupPost
from send import get_send_group


def handle_debug(event: GroupPost):
    if event.group_id not in GROUP_IDS:
        return

    send_group = get_send_group(event.group_id)

    if event.sender.user_id != MASTER_ID:
        return

    print(event.message)
    for msg in event.message:
        if msg.type == "text":
            cmd = msg.data["text"].strip().split(" ")
            break

    if len(cmd) < 2:
        send_group("参数不足")
        return

    if cmd[0] == "eval":
        try:
            result = eval(cmd[1])
            send_group(str(result))
        except Exception as e:
            send_group(str(e))
    elif cmd[0] == "list":
        if cmd[1] == "config":
            data = ''
            for key, value in config.items():
                data += f"{key}: {value}\n"
            send_group(data[:-1])

    elif cmd[0] == "set":
        return
    else:
        send_group("未知命令")
