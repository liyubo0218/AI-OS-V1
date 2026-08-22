class DeviceState:


    def __init__(self):

        self.devices = {}



    def update(
        self,
        device,
        state
    ):

        self.devices[device] = state


        return {
            "status": "updated"
        }



    def get(
        self,
        device
    ):

        return self.devices.get(
            device,
            "unknown"
        )
