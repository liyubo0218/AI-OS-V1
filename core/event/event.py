from datetime import datetime
import uuid


class Event:

    def __init__(
        self,
        event_type,
        payload=None
    ):
        self.event_id = str(uuid.uuid4())

        self.event_type = event_type

        self.payload = payload or {}

        self.timestamp = datetime.utcnow()


    def to_dict(self):

        return {
            "event_id": self.event_id,
            "event_type": self.event_type,
            "payload": self.payload,
            "timestamp": self.timestamp.isoformat()
        }
