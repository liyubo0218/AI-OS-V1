class ChatGPTDeviceWorkflow:


    def __init__(
        self,
        adapter,
        orchestrator,
        memory,
        goal_monitor
    ):

        self.adapter = adapter

        self.orchestrator = orchestrator

        self.memory = memory

        self.goal_monitor = goal_monitor



    def run(
        self,
        user_input
    ):


        task = self.adapter.convert(
            user_input
        )


        result = self.orchestrator.execute_device_task(
            task
        )


        self.memory.save(

            "device_task",

            user_input

        )


        return {

            "task":
            task,

            "result":
            result,

            "memory":
            "saved"

        }
