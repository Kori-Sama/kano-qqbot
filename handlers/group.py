import bot_config
from post_type import GroupPost
from local_config import bot_id, group_ids
from send import get_send_group


def handle_group(event: GroupPost):
    if event.group_id not in group_ids and bot_config.config["group_limit"]:
        return

    send_group = get_send_group(event.group_id)

    content = ""
    is_at_self = False
    for msg in event.message:
        if msg.type == "at" and msg.data["qq"] == str(bot_id):
            is_at_self = True
        if msg.type == "text":
            content += msg.data["text"]

    if not is_at_self:
        return

    content = content.strip()
