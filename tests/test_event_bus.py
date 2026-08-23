from core.event.event import Event
from core.event.event_bus import EventBus


def test_event_publish():

    bus = EventBus()

    event = Event(
        "task.created",
        {
            "task": "test"
        }
    )

    result = bus.publish(event)

    assert result["status"] == "published"

    assert bus.queue.size() == 1


def test_event_dispatch():

    bus = EventBus()

    received = []

    def handler(event):
        received.append(
            event.payload
        )
        return "ok"


    bus.subscribe(
        "task.created",
        handler
    )

    event = Event(
        "task.created",
        {
            "id": 1
        }
    )

    bus.publish(event)

    result = bus.dispatch()

    assert result["status"] == "completed"

    assert received[0]["id"] == 1
