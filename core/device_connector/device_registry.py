class DeviceRegistry:


    def __init__(self):

        self.devices = {}



    def register(
        self,
        name,
        device
    ):

        self.devices[name] = device


        return {
            "status": "registered"
        }



    def get(
        self,
        name
    ):

        return self.devices.get(
            name
        )
