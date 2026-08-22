class CapabilityRegistry:


    def __init__(self):

        self.capabilities = {}



    def register(
        self,
        name,
        capability
    ):

        self.capabilities[name] = capability


        return {
            "status": "registered"
        }



    def get(
        self,
        name
    ):

        return self.capabilities.get(
            name
        )
