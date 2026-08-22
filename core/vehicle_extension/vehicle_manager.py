class VehicleExtensionManager:

    def __init__(self):
        self.capabilities = {}


    def register_capability(
        self,
        capability_id,
        capability
    ):
        self.capabilities[capability_id] = capability

        return {
            "status": "registered"
        }


    def execute(
        self,
        capability_id,
        action,
        context
    ):

        capability = self.capabilities.get(
            capability_id
        )

        if capability is None:
            return {
                "status": "failed",
                "error": "capability_not_found"
            }


        result = capability.execute(
            action,
            context
        )

        return {
            "status": "completed",
            "result": result
        }


    def get_status(
        self,
        capability_id
    ):

        if capability_id in self.capabilities:
            return {
                "status": "available"
            }

        return {
            "status": "unavailable"
        }
