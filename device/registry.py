class DeviceRegistry:


    def __init__(self):

        self.devices = {}



    def register(
        self,
        device
    ):

        self.devices[
            device.device_id
        ] = device


        return {

            "status":"registered",

            "device":
            device.device_id

        }



    def get_device(
        self,
        device_id
    ):

        return self.devices.get(
            device_id
        )



    def find_by_capability(
        self,
        capability
    ):

        results = []


        for device in self.devices.values():

            if capability in device.capabilities:

                results.append(
                    device
                )


        return results



    def list_devices(
        self
    ):

        return [

            device.to_dict()

            for device in self.devices.values()

        ]
