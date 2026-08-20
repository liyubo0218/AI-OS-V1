from sync.sync_event import SyncEvent



class RuntimeEventPublisher:


    def __init__(
        self,
        sync_gateway
    ):

        self.sync_gateway = sync_gateway



    def publish_task_result(
        self,
        task_id,
        result
    ):


        event = SyncEvent(

            "runtime_evt_001",

            "task_update",

            {
                "task_id": task_id,

                "result": result
            }
        )


        return self.sync_gateway.receive_event(
            event
        )
