class VehicleAdapterManager:

    def __init__(self):
        self.adapters = {}


    def register_adapter(
        self,
        vehicle_type,
        adapter
    ):

        self.adapters[vehicle_type] = adapter

        return {
            "status": "registered"
        }


    def execute(
        self,
        vehicle_type,
        action,
        payload
    ):

        adapter = self.adapters.get(
            vehicle_type
        )

        if adapter is None:
            return {
                "status": "failed",
                "error": "adapter_not_found"
            }


        return adapter.execute(
            action,
            payload
        )
