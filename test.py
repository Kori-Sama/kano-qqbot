import httpx

from llm import llm_with_ctx
from post_type import GroupPost

BASE_SEND_URL = "http://127.0.0.1:3000"
GROUP_IDs = [107455393, 839356963]


def group_history():
    # print(f"get history from {107455393}")
    r = httpx.get(f"{BASE_SEND_URL}/get_group_msg_history", params={
        "group_id": 1025022925
    },
        timeout=10)
    return [GroupPost.parse(x) for x in r.json()["data"]["messages"]]


# httpx.post(f"{BASE_SEND_URL}/send_private_msg", json={
#     "message": "hello",
#     "user_id": 2923038671
# })

r = llm_with_ctx(group_history())
print(r)
