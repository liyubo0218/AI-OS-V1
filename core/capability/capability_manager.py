class CapabilityManager:

    def __init__(self):
        self.capabilities = {}


    def register_capability(
        self,
        name,
        capability
    ):
        self.capabilities[name] = capability

        return {
            "status": "registered",
            "capability": name
        }


    def list_capabilities(self):

        return list(
            self.capabilities.keys()
        )


    def execute(
        self,
        capability_name,
        action,
        parameters=None
    ):

        capability = self.capabilities.get(
            capability_name
        )

        if capability is None:
            return {
                "status": "failed",
                "result": "capability_not_found"
            }


        return capability.execute(
            action,
            parameters
        )
