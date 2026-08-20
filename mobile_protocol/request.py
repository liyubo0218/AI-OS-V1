class MobileRequest:


    def __init__(
        self,
        request_id,
        session_id,
        request_type,
        payload
    ):

        self.request_id = request_id

        self.session_id = session_id

        self.type = request_type

        self.payload = payload



    def to_dict(self):

        return {

            "request_id":
            self.request_id,

            "session_id":
            self.session_id,

            "type":
            self.type,

            "payload":
            self.payload

        }
