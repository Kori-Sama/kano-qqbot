from constants import GROUP_IDS
from post_type import NoticePost
from send import get_send_group


def handle_notice(event: NoticePost):
    if event.group_id not in GROUP_IDS:
        return

    send_group = get_send_group(event.group_id)

    if event.sub_type == "poke":
        send_group("别戳我喵!")
        return
