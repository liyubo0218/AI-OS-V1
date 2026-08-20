class Session:


    def __init__(
        self,
        session_id,
        device_id
    ):

        self.session_id = session_id

        self.device_id = device_id

        self.status = "created"



    def activate(
        self
    ):

        self.status = "active"



    def close(
        self
    ):

        self.status = "closed"



    def to_dict(
        self
    ):

        return {

            "session_id":
            self.session_id,

            "device_id":
            self.device_id,

            "status":
            self.status

        }
