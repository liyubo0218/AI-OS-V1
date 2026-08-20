class RuntimeSyncBridge:


    def __init__(
        self,
        local_runtime,
        cloud_runtime
    ):

        self.local = local_runtime

        self.cloud = cloud_runtime



    def sync_task(
        self,
        task
    ):


        # Local -> Cloud

        self.cloud.add_task(

            task

        )


        return {

            "status":
            "synced",

            "task":
            task

        }



    def sync_result(
        self,
        result
    ):


        self.local.add_task(

            result

        )


        return {

            "status":
            "updated",

            "result":
            result

        }

