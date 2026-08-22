class ServiceAdapterManager:

    def __init__(self):
        self.adapters = {}


    def register_adapter(
        self,
        service_type,
        adapter
    ):

        self.adapters[service_type] = adapter

        return {
            "status": "registered"
        }


    def execute(
        self,
        service_type,
        action,
        payload
    ):

        adapter = self.adapters.get(
            service_type
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
