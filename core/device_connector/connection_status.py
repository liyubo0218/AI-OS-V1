class ConnectionStatus:


    def __init__(self):

        self.status = {}



    def update(
        self,
        device,
        value
    ):

        self.status[device] = value


        return {
            "status": "updated"
        }



    def get(
        self,
        device
    ):

        return self.status.get(
            device,
            "offline"
        )
