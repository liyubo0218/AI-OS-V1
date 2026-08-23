from .queue import EventQueue


class EventBus:
    """
    AI-OS EventBus v2

    负责：
    - 事件订阅
    - 事件发布
    - 事件分发
    - 事件历史记录

    不负责：
    - 业务逻辑
    - 任务执行
    """

    def __init__(
        self
    ):
        self.listeners = {}
        self.queue = EventQueue()
        self.history = []


    def subscribe(
        self,
        event_type,
        handler
    ):
        if event_type not in self.listeners:
            self.listeners[event_type] = []

        self.listeners[event_type].append(
            handler
        )

        return {
            "status": "subscribed"
        }


    def publish(
        self,
        event
    ):
        self.queue.push(
            event
        )

        self.history.append(
            event.to_dict()
        )

        return {
            "status": "published",
            "event_id": event.event_id
        }


    def dispatch(
        self
    ):
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


    def get_history(
        self
    ):
        return self.history
