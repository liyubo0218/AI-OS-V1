class CapabilityMapper:


    def __init__(self):

        self.mapping = {}



    def register(
        self,
        device,
        capability
    ):

        self.mapping[device] = capability


        return {
            "status": "registered"
        }



    def get_capability(
        self,
        device
    ):

        return self.mapping.get(
            device
        )
