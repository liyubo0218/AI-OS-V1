class DeviceIdentity:


    def __init__(
        self,
        device_id,
        name,
        device_type,
        capabilities
    ):

        self.device_id = device_id

        self.name = name

        self.type = device_type

        self.capabilities = capabilities

        self.status = "offline"



    def online(self):

        self.status = "online"



    def offline(self):

        self.status = "offline"



    def to_dict(self):

        return {

            "device_id":
            self.device_id,

            "name":
            self.name,

            "type":
            self.type,

            "capabilities":
            self.capabilities,

            "status":
            self.status

        }
