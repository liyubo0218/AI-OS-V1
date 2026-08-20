class LocalDeviceAgent:


    def __init__(
        self,
        device_name
    ):

        self.device_name = device_name



    def execute(
        self,
        command
    ):

        return {

            "device":
            self.device_name,

            "command":
            command,

            "result":
            "本地执行成功"

        }
