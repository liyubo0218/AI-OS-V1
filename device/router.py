class DeviceRouter:


    def __init__(
        self,
        registry,
        permission_manager
    ):

        self.registry = registry

        self.permission_manager = permission_manager



    def route(
        self,
        capability
    ):


        devices = self.registry.find_by_capability(
            capability
        )


        for device in devices:


            allowed = self.permission_manager.check_permission(

                device.device_id,

                capability

            )


            if allowed and device.status == "online":

                return {

                    "device_id":
                    device.device_id,

                    "device":
                    device.name,

                    "capability":
                    capability,

                    "status":
                    "available"

                }



        return {

            "status":
            "no_device"

        }
