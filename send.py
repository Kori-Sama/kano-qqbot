import httpx
from constants import BASE_SEND_URL


def get_send_group(group_id: str):
    def send_group(message: str):
        print(f"send {message} to {group_id}")
        httpx.post(f"{BASE_SEND_URL}/send_group_msg", json={
            "message": message,
            "group_id": group_id
        })
    return send_group
