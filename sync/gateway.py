from sync.storage import SyncStorage



class SyncGateway:


    def __init__(
        self,
        storage=None
    ):

        self.storage = storage or SyncStorage()



    def store_event(
        self,
        event_type,
        payload
    ):


        events = self.storage.load()



        event = {

            "event_id":
            f"evt_{len(events)+1:03d}",

            "type":
            event_type,

            "payload":
            payload

        }



        events.append(
            event
        )


        self.storage.save(
            events
        )


        return {

            "status":
            "stored",

            "event_id":
            event["event_id"]

        }



    def get_events(
        self
    ):

        return self.storage.load()

