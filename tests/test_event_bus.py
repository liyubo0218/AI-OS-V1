from core.event import (
    Event,
    EventBus
)


def test_event_bus():

    bus = EventBus()


    result = []


    def handler(event):

        result.append(
            event.payload["value"]
        )

        return "received"


    bus.subscribe(
        "test_event",
        handler
    )


    event = Event(
        "test_event",
        {
            "value": 100
        }
    )


    publish_result = bus.publish(
        event
    )


    assert publish_result["status"] == "published"


    dispatch_result = bus.dispatch()


    assert dispatch_result["status"] == "completed"

    assert result[0] == 100


    print(
        "Event Bus PASS"
    )


if __name__ == "__main__":

    test_event_bus()
