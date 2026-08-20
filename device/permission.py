class DevicePermissionManager:


    def __init__(self):

        self.permissions = {}



    def set_permission(
        self,
        device_id,
        capability,
        allowed
    ):

        if device_id not in self.permissions:

            self.permissions[device_id] = {}


        self.permissions[device_id][capability] = allowed


        return {
            "status":"updated",
            "device_id":device_id,
            "capability":capability,
            "allowed":allowed
        }



    def check_permission(
        self,
        device_id,
        capability
    ):

        device_permissions = self.permissions.get(
            device_id,
            {}
        )


        return device_permissions.get(
            capability,
            False
        )
