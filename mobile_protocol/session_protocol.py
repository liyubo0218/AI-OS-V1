class SessionProtocol:


    def create_session_request(
        self,
        device_id
    ):

        return {

            "type":
            "session_create",

            "device_id":
            device_id

        }



    def create_session_response(
        self,
        session_id
    ):

        return {

            "session_id":
            session_id,

            "status":
            "active"

        }
