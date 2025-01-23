import httpx

BASE_SEND_URL = "http://127.0.0.1:3000"
GROUP_IDs = [107455393, 839356963]

r = httpx.post(f"{BASE_SEND_URL}/send_group_msg", json={
    "message": "hello",
    "group_id": GROUP_IDs[0]
})

print(r)

# httpx.post(f"{BASE_SEND_URL}/send_private_msg", json={
#     "message": "hello",
#     "user_id": 2923038671
# })
