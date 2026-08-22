class CapabilityStatus:


    def __init__(self):

        self.status = {}



    def update(
        self,
        name,
        value
    ):

        self.status[name] = value


        return {
            "status": "updated"
        }



    def get(
        self,
        name
    ):

        return self.status.get(
            name,
            "unknown"
        )
