class DeviceIntegration:


    def __init__(
        self,
        task_router
    ):

        self.task_router = task_router



    def run(
        self,
        understanding
    ):


        result = self.task_router.execute(
            understanding
        )


        return {

            "status":
            "completed",

            "result":
            result

        }
