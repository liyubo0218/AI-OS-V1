from sync.sync_event import SyncEvent


class MobileGateway:


    def __init__(
        self,
        orchestrator,
        sync_gateway
    ):

        self.orchestrator = orchestrator

        self.sync_gateway = sync_gateway



    def handle_request(
        self,
        request
    ):


        user_input = request.get(
            "user_input",
            ""
        )


        event = SyncEvent(
            "mobile_evt_001",
            "user_input",
            {
                "text": user_input
            }
        )


        sync_result = self.sync_gateway.receive_event(
            event
        )


        result = self.orchestrator.run(
            user_input
        )


        return {
            "status":"success",

            "sync":sync_result,

            "data":result
        }
