import httpx
from loguru import logger
from local_config import base_send_url
from post_type import GroupPost


def get_send_group(group_id: str):
    def send_group(message: str):
        logger.info(f"send {message} to {group_id}")
        httpx.post(f"{base_send_url}/send_group_msg", json={
            "message": message,
            "group_id": group_id
        })
    return send_group


def group_history(group_id: int) -> list[GroupPost]:
    logger.info(f"get history from {group_id}")
    r = httpx.get(f"{base_send_url}/get_group_msg_history", params={
        "group_id": group_id
    })
    return [GroupPost.parse(x) for x in r.json()["data"]["messages"]]
