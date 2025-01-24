import bot_config
from local_config import group_ids, bot_id
from post_type import NoticePost
from send import get_send_group


def handle_notice(event: NoticePost):
    if event.group_id not in group_ids and bot_config.config["group_limit"]:
        return

    send_group = get_send_group(event.group_id)

    if event.sub_type == "poke" and event.target_id == bot_id:
        send_group("别戳我喵!")
        return
