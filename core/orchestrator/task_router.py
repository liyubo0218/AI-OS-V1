class TaskRouter:


    def __init__(
        self,
        device_orchestrator,
        normal_executor
    ):

        self.device_orchestrator = device_orchestrator

        self.normal_executor = normal_executor



    def execute(
        self,
        understanding
    ):


        if "拍照" in understanding.get(
            "goal",
            ""
        ):


            return self.device_orchestrator.execute(
                understanding
            )



        return self.normal_executor.execute(
            understanding
        )
