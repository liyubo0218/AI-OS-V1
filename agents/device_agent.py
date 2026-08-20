from agents.base_agent import BaseAgent


class DeviceAgent(BaseAgent):

    def __init__(
        self,
        device_gateway
    ):

        super().__init__(
            "DeviceAgent",
            "device_control"
        )

        self.device_gateway = device_gateway


    def execute(
        self,
        task
    ):

        device = task.get(
            "device"
        )

        command = task.get(
            "command"
        )


        result = self.device_gateway.execute_device(
            device,
            command
        )


        return {
            "agent": self.name,
            "device_result": result
        }
