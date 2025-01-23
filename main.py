import uvicorn
from fastapi import FastAPI, Request

import bot_config
from dispatch import EventDispatcher
from handlers.config import handle_config
from handlers.debug import handle_debug
from handlers.group import handle_group
from handlers.notice import handle_notice
from post_type import parse_post


app = FastAPI()
dispatcher = EventDispatcher()


def register_events():
    dispatcher.register("message", handle_group)
    dispatcher.register("notice", handle_notice)


register_events()


def on_debug():
    if not bot_config.config["debug"]:
        dispatcher.clear_all()
        print("normal mode")
        register_events()
        return

    print("debug mode")
    dispatcher.clear_all()
    dispatcher.register("message", handle_debug)


@app.post("/event")
async def root(request: Request):
    data = await request.json()
    print(data)

    event = parse_post(data)

    is_set = handle_config(event)

    if is_set:
        on_debug()

    dispatcher.dispatch(event)

    return {}

if __name__ == "__main__":
    uvicorn.run("main:app", port=5120, reload=True)
