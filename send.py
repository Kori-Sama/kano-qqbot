import httpx
from local_config import base_send_url


def get_send_group(group_id: str):
    def send_group(message: str):
        print(f"send {message} to {group_id}")
        httpx.post(f"{base_send_url}/send_group_msg", json={
            "message": message,
            "group_id": group_id
        })
    return send_group
