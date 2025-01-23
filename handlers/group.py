from post_type import GroupPost
from constants import BOT_ID, BOT_NAME, GROUP_IDS, MASTER_ID
from send import get_send_group


def handle_group(event: GroupPost):
    if event.group_id not in GROUP_IDS:
        return

    send_group = get_send_group(event.group_id)

    content = ""
    is_at_self = False
    for msg in event.message:
        if msg.type == "at" and msg.data["qq"] == str(BOT_ID):
            is_at_self = True
        if msg.type == "text":
            content += msg.data["text"]

    if not is_at_self:
        return

    content = content.strip()

    send_group(content)

    # if "我喜欢你" in event.raw_message:
    #     if event.sender.user_id == MASTER_ID:
    #         send_group("我也喜欢你喵主人~")
    #     else:
    #         send_group("我不喜欢你!")
    #     return

    # if event.sender.user_id == MASTER_ID:
    #     send_group("喵~")
    # else:
    #     send_group("哈!!!")
    # return
