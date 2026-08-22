class TaskRouter:


    def route(
        self,
        task,
        device
    ):


        return {

            "task": task,

            "device": device,

            "status": "routed"

        }
