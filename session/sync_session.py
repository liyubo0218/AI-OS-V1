class SyncSession:


    def __init__(
        self,
        session_id
    ):

        self.session_id = session_id

        self.runtime = "hybrid"

        self.status = "created"



    def activate(self):

        self.status = "active"


        return {
            "session_id": self.session_id,
            "runtime": self.runtime,
            "status": self.status
        }
