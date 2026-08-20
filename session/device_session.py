class DeviceSession:


    def __init__(
        self,
        device_id
    ):

        self.device_id = device_id

        self.status = "offline"



    def connect(self):

        self.status = "online"


        return {
            "device_id": self.device_id,
            "status": self.status
        }



    def disconnect(self):

        self.status = "offline"


        return {
            "device_id": self.device_id,
            "status": self.status
        }
