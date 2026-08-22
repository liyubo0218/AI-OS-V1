class DeviceSelector:


    def select(
        self,
        devices,
        capability
    ):


        for device in devices:

            if capability in device.get(
                "capabilities",
                []
            ):

                return device["name"]


        return None
