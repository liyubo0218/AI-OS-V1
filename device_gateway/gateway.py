class DeviceGateway:

    def __init__(self):

        self.devices = {}


    def register_device(
        self,
        device
    ):

        self.devices[
            device.name
        ] = device


        return {
            "status": "registered",
            "device": device.name
        }



    def get_device(
        self,
        name
    ):

        return self.devices.get(
            name
        )



    def execute_device(
        self,
        device_name,
        command
    ):

        device = self.get_device(
            device_name
        )


        if device:

            return device.execute(
                command
            )


        return {
            "status":"error",
            "message":"device not found"
        }
