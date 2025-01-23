from post_type import Post


class EventDispatcher:
    def __init__(self):
        self.handlers = {}

    def register(self, event_type: str, handler: callable):
        if event_type not in self.handlers:
            self.handlers[event_type] = []
        self.handlers[event_type].append(handler)

    def dispatch(self, event: Post):
        event_type = event.post_type
        if event_type in self.handlers:
            for handler in self.handlers[event_type]:
                handler(event)

    def unregister(self, event_type: str, handler: callable):
        if event_type in self.handlers:
            self.handlers[event_type].remove(handler)

    def clear_handlers(self, event_type: str):
        if event_type in self.handlers:
            self.handlers[event_type].clear()

    def clear_all(self):
        self.handlers.clear()
