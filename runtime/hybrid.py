class HybridRuntime:


    def __init__(
        self,
        session_manager,
        runtime,
        sync_gateway
    ):

        self.session_manager = session_manager

        self.runtime = runtime

        self.sync_gateway = sync_gateway



    def app_open(
        self,
        device_id
    ):


        self.session_manager.create_session(

            "session_001",

            device_id

        )


        session = self.session_manager.open_session(

            "session_001"

        )


        self.runtime.start()



        return {

            "mode":
            "online",

            "session":
            session

        }



    def app_close(
        self
    ):


        event = self.sync_gateway.store_event(

            "runtime_status",

            {

                "status":
                "continue_running"

            }

        )


        return {

            "mode":
            "offline",

            "event":
            event

        }



    def recover(
        self
    ):


        return self.sync_gateway.get_events()

