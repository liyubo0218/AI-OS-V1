class SyncEvent:


    def __init__(
        self,
        event_id,
        event_type,
        payload
    ):

        self.event_id = event_id

        self.event_type = event_type

        self.payload = payload



    def to_dict(self):

        return {
            "event_id": self.event_id,
            "type": self.event_type,
            "payload": self.payload
        }
