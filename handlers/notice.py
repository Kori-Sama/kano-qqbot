import bot_config
from local_config import group_ids
from post_type import NoticePost
from send import get_send_group
from welcome import get_template


def handle_notice(event: NoticePost):
    if event.group_id not in group_ids and bot_config.config["group_limit"]:
        return

    send_group = get_send_group(event.group_id)

    # if event.sub_type == "poke" and event.target_id == bot_id:
    #     send_group("别戳我喵!")
    #     return

    if event.sub_type == "approve" or event.sub_type == "invite":
        # Load template for this group if present
        tpl = get_template(event.group_id)
        if not tpl:
            tpl = "欢迎 <user> 加入本群！"
        # Replace <user> token with CQ at code
        mention = f"[CQ:at,qq={event.user_id}]"
        msg = tpl.replace("<user>", mention)
        send_group(msg)
