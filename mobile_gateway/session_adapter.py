class MobileSessionAdapter:


    def __init__(
        self,
        session_manager
    ):

        self.session_manager = session_manager



    def handle(
        self,
        request
    ):


        action = request.get(
            "action"
        )


        device_id = request.get(
            "device_id"
        )


        session_id = request.get(
            "session_id",
            "session_001"
        )



        if action == "open":


            self.session_manager.create_session(

                session_id,

                device_id

            )


            return self.session_manager.open_session(

                session_id

            )



        if action == "close":


            return self.session_manager.close_session(

                session_id

            )



        return {

            "status":
            "unknown_action"

        }
