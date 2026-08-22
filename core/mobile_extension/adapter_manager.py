class MobileAdapterManager:

    def __init__(self):
        self.adapters = {}


    def register_adapter(
        self,
        device_type,
        adapter
    ):

        self.adapters[device_type] = adapter

        return {
            "status": "registered"
        }


    def execute(
        self,
        device_type,
        action,
        payload
    ):

        adapter = self.adapters.get(
            device_type
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
