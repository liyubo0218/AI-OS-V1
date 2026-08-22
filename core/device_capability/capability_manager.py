from .capability_registry import CapabilityRegistry
from .capability_status import CapabilityStatus



class CapabilityManager:


    def __init__(self):

        self.registry = CapabilityRegistry()

        self.status = CapabilityStatus()



    def add_capability(
        self,
        name,
        capability
    ):

        return self.registry.register(
            name,
            capability
        )



    def enable(
        self,
        name
    ):

        capability = self.registry.get(
            name
        )


        if capability is None:

            return {
                "status": "not_found"
            }


        self.status.update(
            name,
            "enabled"
        )


        return {
            "status": "enabled"
        }



    def get_status(
        self,
        name
    ):

        return self.status.get(
            name
        )
