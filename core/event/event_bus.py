from .queue import EventQueue


class EventBus:

    def __init__(self):

        self.listeners = {}

        self.queue = EventQueue()


    def subscribe(
        self,
        event_type,
        handler
    ):

        if event_type not in self.listeners:

            self.listeners[event_type] = []

        self.listeners[event_type].append(handler)

        return {
            "status": "subscribed"
        }


    def publish(
        self,
        event
    ):

        self.queue.push(event)

        return {
            "status": "published",
            "event_id": event.event_id
        }


    def dispatch(self):

        event = self.queue.pop()

        if event is None:

            return {
                "status": "empty"
            }


        handlers = self.listeners.get(
            event.event_type,
            []
        )


        results = []

        for handler in handlers:

            results.append(
                handler(event)
            )


        return {
            "status": "completed",
            "results": results
        }
