class SyncManager:


    def __init__(self):

        self.events = []



    def add_event(
        self,
        event
    ):

        self.events.append(
            event
        )


        return {
            "status":"stored",
            "event_id":event.event_id
        }



    def get_events(self):

        return [
            event.to_dict()
            for event in self.events
        ]
