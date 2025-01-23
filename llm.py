import httpx


def llm(user: str, message: str) -> str:
    r = httpx.post("http://127.0.0.1:11434/api/generate", json={
        "model": "glm4",
        "prompt": f"{user}: {message}",
        "stream": False,
    })
    print(r.json())
    return r.json()["response"]


if __name__ == "__main__":
    try:
        r = llm("user", "你好")
    except Exception as e:
        r = str(e)
    print(r)
