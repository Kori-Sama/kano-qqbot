import bot_config
from post_type import GroupPost
from local_config import group_ids
from send import get_send_group
from welcome import set_template


def handle_group(event: GroupPost):
    if event.group_id not in group_ids and bot_config.config["group_limit"]:
        return

    send_group = get_send_group(event.group_id)

    # Concatenate all text segments to form the message content
    text_parts = [msg.data["text"] for msg in event.message if msg.type == "text"]
    content = "".join(text_parts).strip() if text_parts else ""

    # Handle setting welcome template (admin or owner only)
    if content.startswith("setwelcome") and event.sender.role in {"admin", "owner"}:
        parts = content.split(maxsplit=1)
        if len(parts) == 1 or not parts[1].strip():
            send_group(
                "用法: setwelcome 欢迎模板\n示例: setwelcome 欢迎 <user> 加入本群！"
            )
            return
        welcome_msg = parts[1].strip()
        try:
            set_template(event.group_id, welcome_msg)
            send_group("已更新本群欢迎词 ✅")
        except Exception:
            send_group("更新欢迎词失败，请稍后重试。")
        return

    # content = ""
    # is_at_self = False
    # for msg in event.message:
    #     if msg.type == "at" and msg.data["qq"] == str(bot_id):
    #         is_at_self = True
    #     if msg.type == "text":
    #         content += msg.data["text"]

    # if not is_at_self:
    #     return

    # content = content.strip()
