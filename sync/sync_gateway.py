from sync.sync_manager import SyncManager

from sync.conflict import ConflictResolver



class SyncGateway:


    def __init__(self):

        self.manager = SyncManager()

        self.conflict = ConflictResolver()



    def receive_event(
        self,
        event
    ):

        return self.manager.add_event(
            event
        )



    def sync(self):

        return {
            "status":"synced",
            "events":
            self.manager.get_events()
        }
