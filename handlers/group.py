import bot_config
from llm import llm, llm_with_ctx
from post_type import GroupPost
from local_config import bot_id, bot_name, group_ids, master_id
from send import get_send_group, group_history


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

    if bot_config.config["ctx"]:
        ctx = group_history(event.group_id)

        r = llm_with_ctx(ctx)
        print("with ctx:", r)
        send_group(r)
    else:
        r = llm(event.sender.nickname, content)
        print("single reply:", r)
        send_group(r)

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
