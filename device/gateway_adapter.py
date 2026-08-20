class DeviceGatewayAdapter:


    def __init__(
        self,
        executor
    ):

        self.executor = executor



    def execute_device_task(
        self,
        capability,
        command
    ):


        result = self.executor.execute(

            capability,

            command

        )


        return {

            "type":
            "device_result",

            "data":
            result

        }
