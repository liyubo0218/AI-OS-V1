from sync.sync_event import SyncEvent



class LocalSyncBridge:


    def __init__(
        self,
        sync_gateway,
        offline_queue
    ):

        self.sync_gateway = sync_gateway

        self.offline_queue = offline_queue



    def sync_pending_events(
        self
    ):

        results = []


        events = list(
            self.offline_queue.get_all()
        )


        for index, event in enumerate(events):


            sync_event = SyncEvent(

                "local_evt_" + str(index),

                event["type"],

                event

            )


            result = self.sync_gateway.receive_event(
                sync_event
            )


            if result["status"] == "stored":

                self.offline_queue.remove(
                    event
                )


            results.append(
                result
            )


        return results
